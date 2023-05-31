import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

# Set up the Google Calendar API client
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('calendar', 'v3', credentials=creds)

while True:
    try:
        # Get the current time and format it for querying the calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        # Query the Google Calendar API for events in the next hour
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              timeMax=(datetime.datetime.utcnow() + 
                                                       datetime.timedelta(seconds=3600)).isoformat() + 'Z',
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # Display the upcoming events
        if not events:
            print('No upcoming events.')
        else:
            print('Upcoming events:')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                start_time = datetime.datetime.fromisoformat(start).strftime('%m/%d/%Y %I:%M %p')
                print(f'{start_time} - {event["summary"]}')

    except HttpError as error:
        print(f'An error occurred: {error}')
        break

    # Refresh every minute
    time.sleep(60)
