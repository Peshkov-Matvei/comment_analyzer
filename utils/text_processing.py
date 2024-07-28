import re


def preprocess_comments(comments):
    preprocessed_comments = []
    for comment in comments:
        comment = re.sub(r"http\S+|www\S+|https\S+",
                         '', comment, flags=re.MULTILINE)
        comment = re.sub(r'\@\w+|\#', '', comment)
        comment = re.sub(r'[^A-Za-z0-9\s]+', '', comment)
        preprocessed_comments.append(comment)
    return preprocessed_comments
