from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pytz
from src.assistant import speak, get_audio

# Date and weeks
MONTH = ['January','February','march','april',"may",'june','july','august','september','october','november','december']
DAYS = ["monday", 'tuesday','wednesday','thursday','friday','saturday','sunday']
DAYS_EXT = ["rd","th","st","nd"]

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
                'src/api/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
       
        with open('src/api/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service
    

def get_events(day, service):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next n events on the user's calendar.
    """

    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(
        calendarId='primary', 
        timeMin=date.isoformat(),
        timeMax=end_date.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        speak('No upcoming events found.')
    else:
        speak(f'You have {len(events)} events this day')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "AM"

            else:
                start_time = str(int(start.split("T")[1].split("-")[0]) - 12) + start_time.split(":")[1]
                start_time = start_time + "PM"

            speak(f"{events['summary']} At {start_time}")   


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
            month = MONTH.index(word) - 1

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

    if month < today.month and month != -1:
        year = year + 1

    if day < today.day and month == -1 and day != -1:
        month = month + 1

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()  # 0 - 6
        diference = day_of_week - current_day_of_week

        if diference < 0:
            diference += 7  # go to next week
            if text.count("next") >= 1:
                diference += 7

        return today + datetime.timedelta(diference)

    if month == -1 and day == -1:
        return None

    else:
        return datetime.date(month=month, day=day, year=year)
