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



quote_page = https://github.com/webscrapergroup/webscraper
<li class="commits">
          <a data-pjax="" href="/webscrapergroup/webscraper/commits/master">
              <svg class="octicon octicon-history" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z"></path></svg>
              <span class="num text-emphasized">
                18
              </span>
              commits
          </a>
        </li>
       page = requests.get(url)
def tag_from_html(body):
    soup = BeautifulSoup(page.content, 'html.parser')
    inner_text = soup.find("div", id="commits").content
    page.status_code = 200
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    #references to go back to:
    #https://docs.python-guide.org/scenarios/scrape/
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    #https://blog.hartleybrody.com/web-scraping-cheat-sheet/
    #https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
    #https://blog.hartleybrody.com/web-scraping-cheat-sheet/#extracting-content-from-html

x = "jknv qwdklb alkwjef aljfln sdfnklsjnal aglwkgn asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdaflkjk awlkjfbklwabfkjln awfkljbwablk"
y = "jknv qwdulb alkwjef aljfln sdfnklsjnal aglwkgm asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdajlkjk awlkjfbklwabfkjln awfoojbwablk"
x_segment = x[50:100]
y_segment = y[50:100]
print(len(x_segment))
