# RSS to WordPress Poster

This Python script fetches news articles from RSS feeds and automatically posts them to a WordPress website.

## Installation

1. Clone the repository:
git clone [https://github.com/your-username/your-repository.git](https://github.com/AdityaJain2162/wordpress-automate-rss.git)

2. Install the required Python packages:
pip install feedparser newspaper3k requests

3. Install the miniOrange WordPress REST API Authentication plugin on your WordPress website from [here](https://plugins.miniorange.com/wordpress-rest-api-authentication).

## Usage

1. Configure the miniOrange plugin:
- Follow the instructions provided by the plugin to set it up.
- Once configured, note the URL provided by the plugin for acquiring the JWT token.

2. Replace the placeholder values in the script with your WordPress details:
- `wordpress_url`: URL of your WordPress website's REST API endpoint for posts.
- `wordpress_token_url`: URL provided by the miniOrange plugin for acquiring the JWT token.
- `wordpress_username`: Your WordPress username.
- `wordpress_password`: Your WordPress password.

3. Add RSS feed URLs to the `rss_feed_urls` list variable.

4. Run the script:
python wordpress.py
