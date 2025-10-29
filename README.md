# 🤖 Chatbot Backend (Flask API + Finetuning Notebook)

This project is a **Flask-based chatbot API** scaffold, designed to serve a fine-tuned LLM. It includes:

* ✅ A clean **Flask REST API** to interact with your model (via Postman or other clients)
* 🧠 A **Jupyter notebook** used to fine-tune the model (for reference purposes only)
* 🧳 A folder (`finetuned_model/`) where your trained model should be placed

---

## ⚙️ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatbot-flask-framework.git
cd chatbot-flask-framework
```

---

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Add the Model

* If you’ve already fine-tuned a model using the included notebook or elsewhere:

  * Place the model files (like `pytorch_model.bin`, `config.json`, `tokenizer/`) inside the `finetuned_model/` directory.

---

### 4. Run the Flask App

```bash
python main.py
```

The server will run at `http://127.0.0.1:5000/`

---

## 📬 Postman API Usage

### Endpoint: `POST /chat`

#### Request:

```json
{
  "query": "What are the benefits of the XYZ scheme?"
}
```

#### Response:

```json
{
  "response": "The XYZ scheme offers free medical treatment to eligible citizens..."
}
```

---

## 🧪 Testing with Postman

* Method: `POST`
* URL: `http://127.0.0.1:5000/chat`
* Body → `raw` → `JSON`:

```json
{
  "query": "Tell me about government education schemes"
}
```

---

## 🧠 Notebook: `notebooks/fine_tuning.ipynb`

* This notebook was used to fine-tune a language model on government scheme data.
* **Note:** Model training is not done in the Flask app — it’s decoupled.
* Once training is complete, export the model to `finetuned_model/` to use it in the API.

---

## 🛡️ License

MIT License. Use it, build on it, tweak it. Just remember: this repo doesn’t come with a built-in conscience — your model's responses are your responsibility.
