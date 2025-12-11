from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(logs, top_k=5):
    """
    Extract important keywords from a list of log messages.
    """
    messages = [log["message"] for log in logs]

    vectorizer = TfidfVectorizer(stop_words="english", max_features=50)
    tfidf_matrix = vectorizer.fit_transform(messages)

    features = vectorizer.get_feature_names_out()

    return features[:top_k].tolist()

