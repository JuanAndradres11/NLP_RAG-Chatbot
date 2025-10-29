import nltk

# Download required NLTK resources
try:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')
    print("NLTK resources downloaded successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
