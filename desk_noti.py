import feedparser
import plyer
import time
import os

def Parsefeed():
   f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
   ICON_PATH = os.getcwd() + "/news_icon.ico"



   for newsitem in f['items']:
       print(newsitem['title'])
       print(newsitem['summary'])
       print('\n')

       plyer.notification.notify(
           title=newsitem['title'],
           message=newsitem['summary'],
           app_icon=ICON_PATH,
           timeout=15
       )
       time.sleep(10)

if __name__ == '__main__':
   try:
       Parsefeed()
   except Exception as e:
       print(f"Error: {e}")
