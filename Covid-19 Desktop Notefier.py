from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as bs
from plyer import notification
import time 

header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/syria/", headers = header)
html = urlopen(req)

obj = bs(html)
new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]



while True:
   notification.notify(title="COVID-19 Update"
                      ,message="new cases - " + new_cases +"\nDeath -"+ death
                      ,timeout=5)
   time.sleep(5)

