📌 Project Overview: The Desktop Notifier fetches news data from BBC News RSS feeds to display timely updates on a user’s desktop. Leveraging Python libraries like feedparser for parsing RSS feeds and plyer for handling notifications, the app collects, formats, and displays the latest news headlines with summaries, giving users an efficient way to stay updated on current events.

🛠️ How It Works:

RSS Feed Parsing: The app begins by pulling news data from an RSS feed URL, specifically BBC News’ RSS, using the feedparser library. Each news item in the feed includes details like the title and summary, which are extracted and stored.
Display Notifications: Using plyer, the app creates a system notification for each news item, displaying the title and a short summary directly on the desktop. This method provides non-intrusive alerts that keep users informed without interrupting their workflow.
Icon and Timing: A unique icon gives the notifications a personalized feel. Additionally, the app is configured to show each notification for a set duration, allowing users to see multiple headlines at spaced intervals.
