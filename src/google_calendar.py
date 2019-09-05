from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def authenticate_google():
    '''
    Authenticate with google (OAuth2)
    '''

    creds = None

    if os.path.exists('src/api/token.pickle'):
        with open('src/api/token.pickle', 'rb') as token:
            creds = pickle.load(token)
   
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../api/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
       
        with open('api/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service
    

def get_events(n, service):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next n events on the user's calendar.
    """

    now = datetime.datetime.utcnow().isoformat() + 'Z' 
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=n, singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
