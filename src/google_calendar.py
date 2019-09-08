from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTH = ['January','February','march','april',"may",'june','july','august','september','octuber','novenber','december']
DAYS = ["monday", 'tuesday','wednesday','thursday','friday','saturday','sunday']
DAYS_EXT = ["rd","th","st"]

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
                'src/api/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
       
        with open('src/api/token.pickle', 'wb') as token:
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


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTH:
            month = MONTH.index(month) - 1

        elif word in DAYS:
            day_of_week = DAYS.index(word)

        elif word.isdigit():
            day = int(word)

        else:
            for ext in DAYS_EXT:
                found = word.find(ext)

                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass