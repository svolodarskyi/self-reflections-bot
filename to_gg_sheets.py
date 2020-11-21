from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()

'''
to get started with google sheets https://www.youtube.com/watch?v=4ssigWmExak
'''

def append_record(fields):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    current_file_location = os.path.dirname(os.path.abspath(__file__))
    SERVICE_ACCOUNT_FILE = os.path.join(current_file_location,'keys.json')

    creds = None
    creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets() # pylint: disable=maybe-no-member"

    #record should be a list of lists 
    data = [fields]

    sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                            range="self_reflections!A1:C1", valueInputOption='USER_ENTERED',
                            insertDataOption='INSERT_ROWS', body={"values": data}).execute()
# values = result.get('values', [])
