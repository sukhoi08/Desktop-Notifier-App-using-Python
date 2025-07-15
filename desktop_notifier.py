import feedparser
import plyer
import time

def show_indian_news():
    RSS_URL = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"  # Example
    
    news_feed = feedparser.parse(RSS_URL)
    
    for entry in news_feed.entries[:10]:  # Show top 10 news items
        title = entry.get("title", "No title")
        summary = entry.get("description", entry.get("summary", "No summary"))
        
        print(f"{title}\n{summary}\n{'-'*50}\n")
        
        # Desktop notification
        try:
            plyer.notification.notify(
                title=title[:64],  # Trim long titles
                message=summary[:256],
                timeout=10
            )
        except Exception as e:
            print(f"Notification failed: {e}")
        
        time.sleep(5)  # Delay between news items

if __name__ == "__main__":
    show_indian_news()