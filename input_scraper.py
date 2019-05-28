import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import argparse
import html2text

parser = argparse.ArgumentParser(description='Monitor a webpage.')
parser.add_argument('--dur', dest='user_max_checks', default=0, type=int, help='(optional) add a certain number of checks after which to automatically stop checking')
parser.add_argument('--dur', dest='user_duration', default=0, type=float, help='(optional) add a duration after which to automatically stop checking (in minutes)')
parser.add_argument('--dur', dest='user_infinite', default=0, type=float, help='(optional) have the program run forever (true/false)')

args = parser.parse_args()

user_max_checks = args.user_max_checks
user_duration = args.user_duration
user_infinite = args.user_infinite

url = input("Url to monitor:")
user_interval = input("Number of seconds between checks:")
user_tolerance = input("Max number of acceptable differences before notification:")
user_end_after_success = input("Stop checking after first notification? (y/n)")
user_num = input("Phone number to text to:)
twilio_num = input("Twilio phone number to text from:")
account_sid = input("Twilio Account SID:")
auth_token = input("Twilio Auth Token:")

if(user_end_after_success=="y")||(user_end_after_success=="Y"):
                user_end_after_success = true
else:
                user_end_after_success = false

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
