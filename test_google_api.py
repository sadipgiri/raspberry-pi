"""
    test_google_api.py - Python3 program to use Google API services
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 05/06/2018
"""

import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Sensors-4a1d06cfbafe.json', scope)

gc = gspread.authorize(credentials)

work_sheet = gc.open('Sensors').sheet1

print(work_sheet.get_all_records())

"""
References:
    - Went through Google API Managers Tutorial
    - Why? It will be easier to visualize, makes changes, call an api...
"""

"""
    Roadblock: still need to figure out some issues. So, for now, I am saving it in local file.
"""