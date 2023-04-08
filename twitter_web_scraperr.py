import pandas as pd
from tqdm.notebook import tqdm 
import snscrape.modules.twitter as sntwitter

# Define the search keyword and date range
keyword = "climate change"
since_date = "2022-07-21"
until_date = "2023-03-21"
tweet_limit = 3000

# Create the query with the date range
query = f'{keyword} since:{since_date} until:{until_date} geocode:0,0,2000km' 
scraper = sntwitter.TwitterSearchScraper(query)

tweets = []

# Collect the specified number of tweets
for i, tweet in enumerate(scraper.get_items()):
    if tweet.coordinates:  # Check if geolocation data is available
        data = [
            tweet.date,
            tweet.id,
            tweet.content,
            tweet.user.username,
            tweet.coordinates,
            tweet.likeCount,
            tweet.retweetCount,
        ]
        tweets.append(data)
        
        if i >= tweet_limit - 1:
            break

tweet_df = pd.DataFrame(
    tweets, columns=['date', 'id', 'content', 'username', 'coordinates', 'like_count', 'retweet_count']
)

keyword = keyword.replace(' ','_')
tweet_df.to_csv(f'{keyword}-tweets.csv', index=False)