import feedparser
from newspaper import Article
import requests
import time

# Function to fetch news from the RSS feed and post on WordPress
def fetch_post_and_post_to_wordpress(rss_feed_url, wordpress_url, wordpress_token_url, wordpress_username, wordpress_password):
    # Parse the RSS feed
    feed = feedparser.parse(rss_feed_url)

    if not feed.entries:
        print(f"No entries found in the RSS feed: {rss_feed_url}")
        return

    # Get JWT token for WordPress
    jwt_token = get_jwt_token(wordpress_token_url, wordpress_username, wordpress_password)

    # Create post for each news item
    for entry in feed.entries:
        post_link = entry.link
        post_title = entry.title

        # Fetch the article content using newspaper3k
        article = Article(post_link)
        article.download()
        article.parse()

        # Post the article to WordPress
        create_post(wordpress_url, jwt_token, post_title, article.text)

# Function to get JWT token for WordPress
def get_jwt_token(url, username, password):
    data = {'username': username, 'password': password}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        token = response.json().get('jwt_token')
        return token
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Function to create post on WordPress
def create_post(url, token, title, content):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {'title': title, 'content': content, 'status': 'publish'}
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Post published successfully")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Main function to check for updates and post on WordPress
def check_for_updates_and_post_to_wordpress(rss_feed_urls, wordpress_url, wordpress_token_url, wordpress_username, wordpress_password):
    while True:
        for rss_feed_url in rss_feed_urls:
            fetch_post_and_post_to_wordpress(rss_feed_url, wordpress_url, wordpress_token_url, wordpress_username, wordpress_password)
        time.sleep(60)  # Check for updates every 60 seconds

# Example usage with multiple RSS feed URLs
rss_feed_urls = [
    "https://timesofindia.indiatimes.com/rssfeedmostrecent.cms",
    # Add more RSS feed URLs as needed
]

# Replace with your WordPress details
wordpress_url = 'http://localhost/wp-json/wp/v2/posts'
wordpress_token_url = 'http://localhost/wp-json/api/v1/token'
wordpress_username = 'admin'
wordpress_password = 'admin'

# Check for updates and post on WordPress
check_for_updates_and_post_to_wordpress(rss_feed_urls, wordpress_url, wordpress_token_url, wordpress_username, wordpress_password)
