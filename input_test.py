import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import argparse
import html2text
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
     tree = html.fromstring(page.content)
    soup = BeautifulSoup()
    #references to go back to:
    #https://docs.python-guide.org/scenarios/scrape/
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
x = "jknv qwdklb alkwjef aljfln sdfnklsjnal aglwkgn asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdaflkjk awlkjfbklwabfkjln awfkljbwablk"
y = "jknv qwdulb alkwjef aljfln sdfnklsjnal aglwkgm asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdajlkjk awlkjfbklwabfkjln awfoojbwablk"
x_segment = x[50:100]
y_segment = y[50:100]
print(len(x_segment))
