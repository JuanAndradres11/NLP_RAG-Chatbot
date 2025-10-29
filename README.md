Sure — here’s a **complete, compact README** you can just copy-paste directly into your project folder:

```markdown
# 🧠 NLP + RAG-Based Government Schemes Chatbot

A simple NLP and Retrieval-Augmented Generation (RAG)-based chatbot that retrieves relevant information about government schemes using keyword extraction and similarity search — **no large model used**.

---

## 🚀 Project Structure
```

project/
│
├── app.py               # Flask backend API for chatbot
├── chatbot.py           # NLP + RAG logic (retrieval + dynamic response)
├── dataloader.py        # Loads and preprocesses CSV dataset
├── data/
│   └── schemes.csv      # Dataset of government schemes
└── README.md

````

---

## 🧩 Requirements

Install the required dependencies:

```bash
pip install flask pandas spacy scikit-learn
python -m spacy download en_core_web_sm
````

---

## ▶️ Run the Chatbot

Start the Flask app:

```bash
python app.py
```

The server will run by default at:

```
http://127.0.0.1:5000
```

---

## 💬 Send a Request (from terminal)

Use `curl` to send a JSON query:

```bash
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d "{\"query\": \"What are the benefits of the farmer insurance scheme?\"}"
```

You’ll get a response like:

```json
{
  "response": "The Farmer Insurance Scheme provides coverage against crop loss due to natural calamities..."
}
```

---

## 🧠 How It Works

1. **Data Preprocessing (`dataloader.py`)**

   * Cleans, normalizes, and lemmatizes scheme data using spaCy.

2. **Query Handling (`chatbot.py`)**

   * Uses TF-IDF vectorization + cosine similarity to find the most relevant scheme(s).
   * Constructs a dynamic response using retrieved text (like eligibility, benefits, etc).

3. **API Endpoint (`app.py`)**

   * Exposes a `/chat` route that accepts user queries via JSON POST request.


---

## 🧰 Notes

* No external LLM or WandB setup needed.
* Works completely offline with your CSV dataset.
* Modify similarity threshold or combine multiple columns to refine retrieval.

---

**Author:** Juann
**License:** MIT
**Description:** Lightweight RAG + NLP chatbot for scheme information retrieval.

```

