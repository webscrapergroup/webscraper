import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import argparse
import html2text

parser = argparse.ArgumentParser(description='Monitor a webpage.')
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

# Things needed by magic.py:
# 1. Functions:
#     1. get_page_contents
# 2. variables:
#     1. user_interval (int - time (seconds) between checks)
#     2. user_tolerance (int - max number of acceptable differences)
#     3. user_end_after_success (boolean - stop process after a change has been found)
#     4. One of the following (have these as options for user to choose from - output ones not chosen as 0):
#       a. user_max_checks (int - max checks before stopping)
#       b. user_duration (int - time (minutes) before stopping process)
#       c. user_infinite (boolean - go forever, no limit to time or checks)
# Things needed by output.py:
# 1. Variables:
#     1. twilio_num
#     2. user_num
#     3. account_sid
#     4. auth_token
#     5. user_interval
#     6. user_end_after_success
#     7. user_max_checks
