import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import argparse
import html2text
import datetime

parser = argparse.ArgumentParser(description="Monitor a webpage.")
parser.add_argument(
    "--chk",
    dest="user_max_checks",
    default=0,
    type=int,
    help="(optional) add a certain number of checks after which to automatically stop checking",
)
parser.add_argument(
    "--dur",
    dest="user_duration",
    default=0,
    type=float,
    help="(optional) add a duration after which to automatically stop checking (in minutes)",
)
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

url = input("Url to monitor:")
user_interval = input("Number of seconds between checks:")
user_tolerance = input("Max number of acceptable differences before notification:")
user_end_after_success = input("Stop checking after first notification? (y/n)")
user_num = input("Phone number to text to:")
twilio_num = input("Twilio phone number to text from:")
account_sid = input("Twilio Account SID:")
auth_token = input("Twilio Auth Token:")

if (user_end_after_success == "y") or (user_end_after_success == "Y"):
    user_end_after_success = true
else:
    user_end_after_success = false

client = Client(account_sid, auth_token)
quote_page = "https://github.com/webscrapergroup/webscraper"
r = requests.get(url)
print(r.status_code)
print(r.text)
page = urllib2.urlopen(quote_page)
name_box = soup.find("h1", attrs={"class": "name"})
name = name_box.text.strip()
print(name)


def tag_from_html(body):
    soup = BeautifulSoup(page.content, "html.parser")
    inner_text = soup.find("div", id="commits").content
    page.status_code = 200
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)


# send text while this var is true
send_text = False
# internal var for num of checks made
check_count = 0

# checks for one of three conditions
while (
    (check_count < user_max_checks)
    or ((user_interval * check_count / 60) < user_duration)
) or (user_forever == True):
    # reset differences
    differences_count = 0
    # get page contents
    contents_old = get_page_contents()
    # wait
    time.sleep(user_interval)
    # get contents
    contents_new = get_page_contents()
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
        found_changes()
        if user_end_after_success == True:
            break
        else:
            continue
    else:
        continue


# Time and date checked for text message
time_checked = datetime.datetime.now().time()
date_checked = datetime.datetime.now().date()

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
        client.message.create(body=change_detected, from_=phoneFrom, to=phoneTo)
        print(change_detected)
    else:
        # Prints to console if not texting
        print(change_detected)
