**#📌 Project Overview**
This Python-powered Indian News Notifier fetches breaking news from leading Indian publications (like Times of India, The Hindu, or NDTV) via RSS feeds. Using lightweight libraries, it transforms raw news data into sleek desktop notifications, keeping users informed without disrupting their workflow. Perfect for professionals, students, or anyone who wants to track Indian current affairs efficiently.

**#🛠️ How It Works**
RSS Feed Integration

Pulls live news from customizable Indian RSS feeds (e.g., Times of India’s top stories).

Extracts headlines, summaries, and metadata using feedparser.

Smart Notifications

Displays concise notifications via plyer, with:

Trimmed titles/summaries (to avoid overflow).

Error handling for robust delivery.

Optional console printing for debugging.

User-Centric Design

Configurable delay (time.sleep(5)) between updates.

Shows only the top 10 headlines to avoid overload.

**🌟 Key Features**
✅ No API Keys Needed – Uses free, public RSS feeds.
✅ Cross-Platform – Works on Windows, macOS, and Linux (with libnotify).
✅ Customizable Sources – Swap the RSS_URL for any Indian news feed.
✅ Lightweight – Minimal dependencies, runs in the background.

📈 Project Value
For Users: Saves time by aggregating news from multiple sources into one stream.

For Developers: Demonstrates:

Real-time data parsing with feedparser.

System integration via plyer.

Error handling and graceful degradation.

🔗 Scalability & Extensions
Add More Feeds: Support sports (https://www.thehindu.com/sport/feeder/default.rss) or business news.

Advanced Filtering: Exclude irrelevant topics (e.g., cricket) using keyword checks.

Logging: Save news history to a file for later review.

💡 Key Takeaways
Building this notifier sharpened my skills in:

RSS feed manipulation and XML parsing.

User experience design (notification timing, content trimming).

Cross-platform compatibility testing.
