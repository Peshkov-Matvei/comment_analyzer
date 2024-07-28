import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


with open('data/processed/comments_preprocessed.json', 'r', encoding='utf-8') as f:
    preprocessed_comments = json.load(f)


vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(preprocessed_comments)

n_topics = 5
lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)
lda_model.fit(X)

with open('models/lda_model.pkl', 'wb') as f:
    pickle.dump(lda_model, f)


def print_topics(model, vectorizer, top_n=10):
    for idx, topic in enumerate(model.components_):
        print(f"Тема {idx}:")
        print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-top_n - 1:-1]])


print_topics(lda_model, vectorizer)
