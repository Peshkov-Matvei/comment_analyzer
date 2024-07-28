import json
from utils.youtube_api import get_comments
from googleapiclient.discovery import build

api_key = 'YOUR_API_KEY'
video_id = 'YOUR_VIDEO_ID'

comment = get_comments(api_key, video_id)

with open('data/raw/comments_raw.json', 'w', encoding='utf-8') as f:
    json.dump(comment, f, ensure_ascii=False, indent=4)
