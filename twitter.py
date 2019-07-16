# Import the Twython class
from twython import Twython  
import json
from tabulate import tabulate

# Load credentials from json file
with open("twitter_credentials-df.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['consumer_key'], creds['consumer_secret'])

# Create our query
query = {'q': '#nuedigital',  
        'result_type': 'newest',
        'count': 20,
        'lang': 'de',
        }

import pandas as pd

# Search tweets
dict_ = {'user': [],  'text': [], 'fav_count': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    #dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['fav_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)  
df.sort_values(by='fav_count', inplace=True, ascending=False)  
print(tabulate(df, headers='keys', tablefmt='grid'))
