import requests

url = 'http://localhost:9696/predict'

claim_data = {"#": 13,
              "video_id": 3609761483,
              "video_duration_sec": 51,
              "video_transcription_text": "someone shared with me that the longest recorded cricket match lasted 14 days",
              "verified_status": "not verified", 
              "author_ban_status": "active", 
              "video_view_count": 700081.0,
              "video_like_count": 434565.0, 
              "video_share_count": 97995.0, 
              "video_download_count": 2408.0,
              "video_comment_count": 1411.0}

response = requests.post(url, json=claim_data).json()
print(response)
