import json
from utils.text_processing import preprocess_comments

with open('data/raw/comments_raw.json', 'r', encoding='utf-8') as f:
    comments = json.load(f)

preprocessed_comments = preprocess_comments(comments)

with open('data/processed/comments_preprocessed.json', 'w', encoding='utf-8') as f:
    json.dump(preprocessed_comments, f, ensure_ascii=False, indent=4)
