import pandas as pd
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy for NLP preprocessing
nlp = spacy.load("en_core_web_sm")

# Load dataset
data = pd.read_csv('data/government_schemes.csv')
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
data.fillna('', inplace=True)

# Combine searchable fields
data['combined_text'] = data.apply(
    lambda x: f"{x['scheme_name']} {x['category']} {x['eligibility']} {x['benefits']} {x['age_group']}", axis=1
)

# Build TF-IDF vectors for retrieval
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(data['combined_text'])


# ---------------------------------------------------
# 🔹 NLP helper: clean + extract keywords from query
# ---------------------------------------------------
def extract_keywords(query):
    doc = nlp(query.lower())
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(keywords)


# ---------------------------------------------------
# 🔹 Find scheme info using RAG logic
# ---------------------------------------------------
def find_scheme_info(query):
    clean_query = extract_keywords(query)

    # Convert query to vector and compute similarity
    query_vec = vectorizer.transform([clean_query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    # Get best match index
    best_idx = cosine_similarities.argmax()
    best_score = cosine_similarities[best_idx]

    if best_score < 0.2:
        return "No matching scheme found. Try rephrasing your query."

    matched_row = data.iloc[best_idx]
    scheme_name = matched_row.get('scheme_name', '').capitalize()
    benefits = matched_row.get('benefits', '')
    eligibility = matched_row.get('eligibility', '')
    category = matched_row.get('category', '')
    website = matched_row.get('website_url', '')

    # Decide what the user asked for
    if re.search(r'eligibility|eligible|criteria', query):
        response = f"The eligibility criteria for **{scheme_name}** are: {eligibility or 'not specified.'}"
    elif re.search(r'benefit|provide|offer|help', query):
        response = f"The main benefits of **{scheme_name}** are: {benefits or 'not specified.'}"
    elif re.search(r'category|type|group', query):
        response = f"The scheme **{scheme_name}** falls under the category: {category or 'not specified.'}"
    elif re.search(r'website|apply|link|application', query):
        response = f"You can learn more or apply for **{scheme_name}** here: {website or 'link not available.'}"
    else:
        response = (
            f"**{scheme_name}** is a government scheme under the category '{category}'. "
            f"It aims to provide the following benefits: {benefits or 'N/A'}. "
            f"Eligibility: {eligibility or 'not specified.'}"
        )

    return response
