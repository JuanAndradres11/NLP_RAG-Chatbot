import pandas as pd
import re
import spacy

# Load SpaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

def load_data(file_path):
    data = pd.read_csv(file_path)
    
    # Clean column names
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Handle missing values
    data.fillna('', inplace=True)
    
    # Normalize text
    data['scheme_name'] = data['scheme_name'].str.lower()
    data['eligibility'] = data['eligibility'].str.lower()
    
    # Remove special characters
    data['scheme_name'] = data['scheme_name'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]', '', x))
    data['eligibility'] = data['eligibility'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]', '', x))
    
    # Advanced NLP processing (optional)
    data['scheme_name'] = data['scheme_name'].apply(lambda x: " ".join([token.lemma_ for token in nlp(x)]))
    data['eligibility'] = data['eligibility'].apply(lambda x: " ".join([token.lemma_ for token in nlp(x)]))
    
    return data
