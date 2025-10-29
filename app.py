from flask import Flask, request, jsonify
import pandas as pd
import re
import os
import csv
from chatbot import find_scheme_info  # NLP + RAG based function (we'll modify that file too)

app = Flask(__name__)

# Load CSV data once during app initialization
data = pd.read_csv('data/government_schemes.csv')

# Clean column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
data.fillna('', inplace=True)

# Normalize text
data['scheme_name'] = data['scheme_name'].str.lower()
data['eligibility'] = data['eligibility'].str.lower()

# Feedback file path
feedback_file_path = 'data/feedback.csv'

# Ensure feedback file exists
if not os.path.exists(feedback_file_path):
    with open(feedback_file_path, 'w', newline='') as feedback_file:
        writer = csv.writer(feedback_file)
        writer.writerow(['Question', 'Answer', 'Feedback'])  # Create header

# Function to store feedback
def store_feedback(question, answer, feedback):
    with open(feedback_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([question, answer, feedback])

# -------------------------------
# 🔹 Route to handle user queries
# -------------------------------
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or 'user_input' not in data:
        return jsonify({"error": "No input provided"}), 400

    user_input = data['user_input'].lower().strip()
    print(f"Data received: {user_input}")

    # Handle greetings
    if re.search(r'\b(hello|hi|hey)\b', user_input):
        response = "Hello! How can I assist you with government schemes today?"
        return jsonify({"response": response})

    # Handle "help" or "what can you do" type queries
    if re.search(r'what can you do|what are you able to do|what are you for|what information|info you have', user_input):
        response = (
            "You can ask me about various government schemes. Example queries:\n"
            "1. Tell me about the midday meal scheme\n"
            "2. What are the benefits of PM Kisan scheme?\n"
            "3. Schemes available for students or farmers\n"
            "4. Eligibility criteria for scholarship schemes"
        )
        return jsonify({"response": response})

    # Find relevant info using RAG logic
    response = find_scheme_info(user_input)

    return jsonify({"response": response})


# -------------------------------
# 🔹 Route to handle feedback
# -------------------------------
@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_data = request.get_json()

    if not feedback_data or 'question' not in feedback_data or 'answer' not in feedback_data or 'feedback' not in feedback_data:
        return jsonify({"error": "Invalid input. 'question', 'answer', and 'feedback' fields are required."}), 400

    store_feedback(feedback_data['question'], feedback_data['answer'], feedback_data['feedback'])
    return jsonify({"message": "Feedback submitted successfully."}), 200


# -------------------------------
# 🔹 Run app
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
