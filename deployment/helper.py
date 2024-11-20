import re
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

load_dotenv()

api_key = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def get_all_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        # Make API call to get comments
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token  # Use pagination token for next set of comments
        )
        
        # Execute the request
        response = request.execute()

        # Loop through the comments in the response
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            timestamp = item['snippet']['topLevelComment']['snippet']['publishedAt']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            comments.append({
                'author': author.strip(),
                'comment': comment.strip(),
                'timestamp': timestamp.strip(),
                'like_count': like_count,
            })
        
        # Check if there's another page of comments (pagination)
        next_page_token = response.get('nextPageToken')

        if not next_page_token or len(comments) >= 100:  # If no more pages, break the loop
          break

    return comments

def extract_youtube_id(url_or_id):
    pattern = r'(?:v=|\/)([a-zA-Z0-9_-]{11})(?:&|$)?'
    
    if re.fullmatch(r'[a-zA-Z0-9_-]{11}', url_or_id):
        return url_or_id
    
    match = re.search(pattern, url_or_id)
    if match:
        return match.group(1)
    return None  