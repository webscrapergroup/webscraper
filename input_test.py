import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import argparse
import html2text

parser.add_argument('--dur', dest='duration', default=-1, type=float, help='(optional) add a duration after which to automatically stop checking')

args = parser.parse_args()

duration = args.duration

url = input("Url to monitor:")
secs = input("Number of seconds between checks:")
phoneTo = input("Phone number to text to:)
phoneFrom = input("Twilio phone number to text from:")
account_sid = input("Twilio Account SID:")
auth_token = input("Twilio Auth Token:")

client = Client(account_sid, auth_token)


x = "jknv qwdklb alkwjef aljfln sdfnklsjnal aglwkgn asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdaflkjk awlkjfbklwabfkjln awfkljbwablk"
y = "jknv qwdulb alkwjef aljfln sdfnklsjnal aglwkgm asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdajlkjk awlkjfbklwabfkjln awfoojbwablk"
x_segment = x[50:100]
y_segment = y[50:100]
print(len(x_segment))
