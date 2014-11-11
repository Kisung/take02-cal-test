__author__ = 'kisung.yun'

import httplib2
import sys

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets

from pprint import pprint
import argparse
from oauth2client import tools

argparser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])

flags = argparser.parse_args(sys.argv[1:])

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret can be found in Google Developers Console

FLOW = flow_from_clientsecrets('client_secrets.json',
                               scope='https://www.googleapis.com/auth/calendar')


# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('calendar.dat')
credentials = storage.get()
if (credentials is None) or (credentials.invalid is True):
    # credentials = run(FLOW, storage)
    credentials = tools.run_flow(FLOW, storage, flags)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google Developers Console
# to get a developerKey for your own application.

service = build(serviceName='calendar', version='v3', http=http)

'''
# Calendar Get
calendar = service.calendars().get(calendarId='primary').execute()
print calendar
'''

'''
# Calendar List
page_token = None

while True:
    calendar_list = service.calendarList().list(pageToken=page_token).execute()
    for calendar_list_entry in calendar_list['items']:
        print calendar_list_entry['id'], calendar_list_entry['summary']
    page_token = calendar_list.get('nextPageToken')
    if not page_token:
        break
'''

'''
# Calendar Delete
calendar_list = [
    '0segbo80kk80b3vu15fvfa92jg@group.calendar.google.com',
    'hsv0e0nodg00f3ug91jatmelak@group.calendar.google.com',
    'i4ua9lhakrbkqlh1257hqug1sg@group.calendar.google.com',
    'hrr6gb4047ua8fg90972imooa4@group.calendar.google.com',
    '6pp70a6inubr33htrlpgq3pgfk@group.calendar.google.com',
    'ca2i23ok9b9kcmi71ar2i12a78@group.calendar.google.com'
]


for ci in calendar_list:
    print 'calendar Delete : ', ci
    service.calendarList().delete(calendarId=ci).execute()
'''

'''
# Events: list
page_token = None
while True:
    events = service.events().list(calendarId='primary', pageToken=page_token).execute()
    for event in events['items']:
        # print event  # event['summary']
        pprint.pprint(event)
    page_token = events.get('nextPageToken')
    if not page_token:
        break
'''

event = {
    'summary': '[PROBLEM]gzip compression is off for connector http-8080 on eu-fim-was05',
    'start': {
        'dateTime': '2014-11-11T10:27:00.000+09:00',
        'timeZone': 'Asia/Seoul'
        },
    'end': {
        'dateTime': '2014-11-11T10:27:30.000+09:00',
        'timeZone': 'Asia/Seoul'
        },
    'description': 'gzip compression is off for connector http-8080 on eu-fim-was05',
    'reminders': {
        'overrides': [
            # {'method': 'sms', 'minutes': 1},
            # {'method': 'popup', 'minutes': 4},
            # {'method': 'email', 'minutes': 3},
            {'method': 'sms', 'minutes': 1}
        ],
        'useDefault': False},
    }

# """
created_event = service.events().insert(calendarId='primary', body=event).execute()

pprint(created_event)  # created_event['id']
# """
