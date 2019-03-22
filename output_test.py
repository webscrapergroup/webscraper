from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time
import argparse

from magic import send_text
from input import client, user_end_after_success, duration, user_interval, twilio_phone, user_phone

def found_change():
    if(send_text == True):
        #Message for if change detected
        client.message.create(
            body = "We have detected a change!",
            from_ = twilio_phone,
            to = user_phone
        )
        # if(user_end_after_success == True):
        #     break
        # else:
        #     time.sleep(user_interval)

def no_change():
    if(send_text == True):
        #Message for if change not detected
        client.message.create(
            body = "We did not detect a change.",
            from_ = twilio_phone,
            to = user_phone
        )
        
