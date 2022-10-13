#*************************Reference****************
#The following are required packages and software I used to run this code:
#tweepy             4.10.1
#networkx           2.8.6
from asyncio.streams import FlowControlMixin
from re import M
from operator import itemgetter
import tweepy
import networkx as nx
import matplotlib.pyplot as plt
import json 
import pandas as pd

#This is what I would run if I wanted to scrape data by interacting with the Tweepy API.
#When run, it will ask for tweets made under the two specfied hashtags. It will then take 
# the ID's of the users who created those tweets and then find their followers and put them
# in a list. This is what I have visualized in a network.

# initialize tweepy client with bearer_token
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAACBxgQEAAAAAyz%2FFEMlTwxWv3pFf7eqpNn%2FAfMM%3DVVRYG7FYeBCIXcQc0rozUEr8lkWfAJWLQZ7XNDVvN7FJ4G2mOV')
#retrieve the people a user follows, return a list of their ids
def get_following(user):
    anti_user_following = client.get_users_following(id = user[0])
    following = []
    for info in anti_user_following.data:
        following.append((user[0], info.id))
    return following
#gets the username given ids
def get_username(id):
    name = client.get_user(id = id)
    return name

# ****************************Fetching Anti Vaccine Users**************************
# Collect the user id's of ten people who tweeted against covid-19
hashtag = '#DoNotComply'
anti_vax_users = client.search_recent_tweets(query=hashtag, user_fields=['username'], expansions='author_id',  max_results=10)
anti_users = {u["id"]: u for u in anti_vax_users.includes['users']}
anti_user_objects = [] #list of users who are against COVID-19
for tweet in anti_vax_users.data:
    if anti_users[tweet.author_id]:
        user = anti_users[tweet.author_id]        
        anti_user_objects.append((str(user.id), user.username))
#a list of the people user_objects follow (A list of lists)
anti_users_followers = []
#writes to a json file  
for i in anti_user_objects:
    anti_users_followers.append(get_following(i))

#make the list of lists to one long list
flat_anti_users_followers = [item for sublist in anti_users_followers for item in sublist]
#Dump data into Json file
with open('anti.json', 'w') as out:       
        json.dump(flat_anti_users_followers, out, indent=2)

#********************Fetching Pro Vaccine Users****************************
hashtag = '#GetYourBooster'
pro_vax_users = client.search_recent_tweets(query=hashtag, user_fields=['username'], expansions='author_id',  max_results=10)
pro_users = {u["id"]: u for u in pro_vax_users.includes['users']}
pro_user_objects = [] #list of users who are against COVID-19
for tweet in pro_vax_users.data:
    if pro_users[tweet.author_id]:
        user = pro_users[tweet.author_id]        
        pro_user_objects.append((str(user.id), user.username))

#a list of the people user_objects follow (A list of lists)
pro_users_followers = []
#writes to a json file  
for i in pro_user_objects:
    pro_users_followers.append(get_following(i))

#make the list of lists to one long list
flat_pro_users_followers = [item for sublist in pro_users_followers for item in sublist]

with open('pro.json', 'w') as out:       
        json.dump(flat_pro_users_followers, out, indent=2)