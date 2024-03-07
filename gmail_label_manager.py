from googleapiclient.discovery import build
from gmail_api_auth import authenticate_gmail_api

def get_label_id_by_name(label_name):
    creds = authenticate_gmail_api()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    for label in labels:
        if label['name'] == label_name:
            return label['id']
    return None
