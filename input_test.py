import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import argparse
import html2text


x = "jknv qwdklb alkwjef aljfln sdfnklsjnal aglwkgn asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdaflkjk awlkjfbklwabfkjln awfkljbwablk"
y = "jknv qwdulb alkwjef aljfln sdfnklsjnal aglwkgm asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdajlkjk awlkjfbklwabfkjln awfoojbwablk"
x_segment = x[50:100]
y_segment = y[50:100]
print(len(x_segment))
