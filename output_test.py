from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time
import argparse

from magic import send_text
from input import (
    client,
    user_end_after_success,
    user_duration,
    user_interval,
    twilio_phone,
    user_phone,
)

# Strings for text messages and terminal messages
change_detected = "We have detected a change!"
change_not_detected = "We did not detect a change."


def found_change():
    if send_text == True:
        # Message to the client's phone and terminal for if change detected
        client.message.create(body=change_detected, from_=twilio_phone, to=user_phone)
        print(change_detected)
        # If the user decides to have the program continue running, program sleeps and then runs again
        if user_end_after_success == False:
            time.sleep(user_interval)
            found_change()
        else:
            continue
        # Only terminal message for if not text message
    else:
        print(change_detected)


def no_change():
    if send_text == True:
        # Message to the client's phone and terminal for if change not detected
        client.message.create(
            body=change_not_detected, from_=twilio_phone, to=user_phone
        )
        print(change_not_detected)
        # If the user decides to have the program continue running, program sleeps and then runs again
        if user_end_after_success == False:
            time.sleep(user_interval)
            found_change()
        else:
            continue
        # Only terminal message instead of text message
    else:
        print(change_not_detected)
