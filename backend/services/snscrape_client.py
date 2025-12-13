import os
import snscrape.modules.twitter as sntwitter

# FORCE ALL REQUESTS THROUGH Tor SOCKS5 PROXY (INSIDE PYTHON)
os.environ.setdefault("HTTP_PROXY", "socks5h://127.0.0.1:9050")
os.environ.setdefault("HTTPS_PROXY", "socks5h://127.0.0.1:9050")
os.environ.setdefault("http_proxy", "socks5h://127.0.0.1:9050")
os.environ.setdefault("https_proxy", "socks5h://127.0.0.1:9050")

def fetch_twitter_profile(username: str):
    try:
        scraper = sntwitter.TwitterUserScraper(username)
        user = scraper.entity  # This forces an API lookup
        return {
            "username": user.username,
            "displayname": user.displayname,
            "bio": user.description,
            "join_date": str(user.created),
            "profile_image": user.profileImageUrl,
            "followers_count": user.followersCount,
        }
    except Exception as e:
        return {"error": repr(e)}

def fetch_tweets(username: str, limit=20):
    tweets = []
    try:
        for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
            if i >= limit:
                break
            tweets.append({
                "id": tweet.id,
                "text": tweet.rawContent,
                "timestamp": str(tweet.date),
                "url": tweet.url,
            })
    except Exception as e:
        return {"error": repr(e)}
    return tweets
