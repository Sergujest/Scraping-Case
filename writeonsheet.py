from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def write(listofProducts,rangeB,rangeE,creds):

    spreadSheetID = '1Ut5ObFO6cXEZaMAoRcZHwViaVDjuejoLQCd-4PsA7uQ'
    rangeE=rangeB+rangeE-1
    sheetRange = 'Sheet1!A{}:D{}'.format(rangeB,rangeE)
    service = build('sheets', 'v4', credentials=creds)

    body = {
        'majorDimension': 'ROWS',
        'values': listofProducts,
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadSheetID, range=sheetRange,
        valueInputOption='RAW', body=body).execute()
        

    return 