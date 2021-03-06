from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time
import argparse
import datetime

from magic import send_text

# specific variable names still needed?
from input import (
    client,
    # user_end_after_success,
    # user_max_checks,
    # user_duration,
    user_interval,
    twilio_phone,
    user_phone,
)

# Getting time  and date for when change is detected
time_checked = datetime.datetime.now().time()
date_checked = datetime.datetime.now().date()

# String for text messages and terminal messages
change_detected = "We have detected a change at " + time_checked + date_checked + "!"

# The number of successful checks so far
# user_num_checks = 0


def found_change():
    if send_text == True:
        # Message to the client's phone and terminal for if change detected
        client.message.create(body=change_detected, from_=twilio_phone, to=user_phone)
        print(change_detected)
        # If the user decides to have the program continue running, program sleeps and then runs again
        # if user_end_after_success == False:
        #     user_num_checks += 1
        #     # Checks if program has reached the maximum checks
        #     if user_num_checks != user_max_checks:
        #         time.sleep(user_interval)
        #         found_change()
        #     else:
        #         pass
        # else:
        #     pass
        # Only terminal message for if not text message
    else:
        print(change_detected)
