# Download the helper library from https://www.twilio.com/docs/python/install
import os
import xlwt
from twilio.rest import Client
from xlwt import Workbook

# execute "source ./twilio.env" in REPL to set environment parameters

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

recordings = client.recordings.list(limit=20)

# create Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Call Data')

# write header row
sheet1.write(0, 0, 'Recording No')
sheet1.write(0, 1, 'Recording SID')
sheet1.write(0, 2, 'Recording URI')
sheet1.write(0, 3, 'Transcription URI')

# iteratively add row with recording details
i = 1

for record in recordings:
    print("Call " + str(i) + " - SID:" + record.sid + "\t URI: " + record.uri)
    sheet1.write(i, 0, str(i))
    sheet1.write(i, 1, record.sid)
    sheet1.write(i, 2, 'https://api.twilio.com/2010-04-01/Accounts/' + record.account_sid + '/Recordings/' + record.sid + '.mp3') #record.uri is .json not .mp3
    i = i+1

wb.save('Recordings.xls')