from googleapiclient.discovery import build


def get_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    results = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        if 'nextPageToken' in results:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=results['nextPageToken'],
                textFormat='plainText'
            ).execute()
        else:
            break

    return comments
