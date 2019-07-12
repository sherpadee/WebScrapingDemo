# Import the Twython class
from twython import Twython  
import json

# Load credentials from json file
with open("twitter_credentials-df.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['consumer_key'], creds['consumer_secret'])

# Create our query
query = {'q': '#nuedigital',  
        'result_type': 'newest',
        'count': 30,
        'lang': 'de',
        }

import pandas as pd

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)  
df.sort_values(by='favorite_count', inplace=True, ascending=False)  
print(df.head()  )
