from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time
import argparse
import datetime

from magic import send_text

from input_scraper import client, twilio_num, user_num, url

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
