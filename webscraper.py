# import various libs
import requests

# pulls from website
from bs4 import BeautifulSoup

# sends texts
from twilio.rest import Client

# for time options
import time

# for parsing website data
import argparse
import html2text
import datetime

# for getting urls
import urllib.request

# One of these is required for program to work
parser = argparse.ArgumentParser(description="Monitor a webpage.")
# Sets maximum amount of checks
parser.add_argument(
    "--chk",
    dest="user_max_checks",
    default=0,
    type=int,
    help="(optional) add a certain number of checks after which to automatically stop checking",
)
# Sets program to run for certain amount of time in minutes
parser.add_argument(
    "--dur",
    dest="user_duration",
    default=0,
    type=float,
    help="(optional) add a duration after which to automatically stop checking (in minutes)",
)
# Sets program to run until stopped
parser.add_argument(
    "--inf",
    dest="user_infinite",
    default=0,
    type=float,
    help="(optional) have the program run forever (true/false)",
)
args = parser.parse_args()

user_max_checks = args.user_max_checks
user_duration = args.user_duration
user_infinite = args.user_infinite

# Inputs from user upon starting
url = input("Url to monitor: ")
user_interval = int(input("Number of seconds between checks: "))
user_tolerance = int(
    input("Max number of acceptable differences before notification: ")
)
user_end_after_success = input("Stop checking after first notification? (y/n): ")
user_num = input("Phone number to text to: ")
twilio_num = input("Twilio phone number to text from: ")
account_sid = input("Twilio Account SID: ")
auth_token = input("Twilio Auth Token: ")

# checks if user wants to keep scraper running after a change is detected
if (user_end_after_success == "y") or (user_end_after_success == "Y"):
    user_end_after_success = True
else:
    user_end_after_success = False

client = Client(account_sid, auth_token)
quote_page = "https://github.com/webscrapergroup/webscraper"

# Function for grabbing page contents
def get_page_contents(url):
    page = requests.get(url)
    print("Page status code: " + str(page.status_code))
    # print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")
    name_box = soup.find("section", {"id": "inst3522"})
    # Goes 3 tags deep in HTML code of CS Moodle home page
    text_box1 = list(name_box.children)[1]
    text_box2 = list(text_box1.children)[1]
    text_box3 = list(text_box2.children)[1]
    # print(text_box3.get_text())
    return text_box3.get_text()


# send text while this var is true
send_text = False
# internal var for num of checks made
check_count = 0
# Time and date checked for text message
time_checked = str(datetime.datetime.now().time())
date_checked = str(datetime.datetime.now().date())

# String for text message when successfully checked
change_detected = (
    "We detected a change at "
    + time_checked
    + " on "
    + date_checked
    + " on "
    + url
    + "!"
)

# Function for when a change is found
def found_change():
    # If you want it to send a text
    if send_text == True:
        client.messages.create(body=change_detected, from_=twilio_num, to=user_num)
        print(change_detected)
    else:
        # Prints to console if not texting
        print(change_detected)


# checks for one of three conditions
while (
    (check_count < user_max_checks)
    or ((user_interval * check_count / 60) < user_duration)
) or (user_infinite == True):
    send_text = False
    # reset differences
    differences_count = 0
    # get page contents
    contents_old = get_page_contents(url)
    # wait
    time.sleep(user_interval)
    # get contents
    contents_new = get_page_contents(url)
    # update check count
    check_count += 1
    # check differences between slices of page contents strings
    differences_count = sum(1 for a, b in zip(contents_old, contents_new) if a != b)
    # check if the differences are greater than what the user specifies
    if (
        differences_count >= user_tolerance
        or (abs(len(contents_old)) - len(contents_new)) > user_tolerance
    ):
        send_text = True
        found_change()
        if user_end_after_success == True:
            break
        else:
            continue
    else:
        continue
# this is the end of the code
