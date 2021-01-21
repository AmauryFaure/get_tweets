#!/usr/bin/env python

"""
This file allows to get tweet content from the Twitter API.
"""

import os

import tweepy
import csv
from dotenv import load_dotenv

__author__="Amaury Faure"

#Load credentials to acess twitter API, credentials are personal therefore not included.
load_dotenv("credentials.env")
#Access twitter API
auth = tweepy.AppAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
api = tweepy.API(auth)


def get_tweet_text(tweet):
    """This function returns the full tweet content for a tweet object of tweepy.com

    This function receives a tweet objects and returns the full text content of the tweet.

    :param tweet: A tweet received from twitter
    :return: The text of this tweet as a string
    """
    if hasattr(tweet, "retweeted_status"):  # Check if Retweet
        try:
            content = tweet.retweeted_status.extended_tweet["full_text"]
        except AttributeError:
            content = tweet.retweeted_status.full_text
    else:
        try:
            content = tweet.extended_tweet["full_text"]
        except AttributeError:
            content = tweet.full_text
    return content

#Define export file
file = open('test.csv', 'w', newline='')
writer = csv.writer(file)
#To look for all stop words use this portion

with open("stopwords.csv", newline='') as words_file:
    reader = csv.reader(words_file)
    for row in reader:
        search_term = row
        for tweet in tweepy.Cursor(api.search, q=search_term, lang="fr", count="20", tweet_mode="extended").items(15):
            writer.writerow([get_tweet_text(tweet), search_term])

#To search for a special term :
# search_term="bonjour"
# for tweet in tweepy.Cursor(api.search, q=search_term, lang="fr", count="20", tweet_mode="extended").items(10):
#     writer.writerow([get_tweet_text(tweet), search_term])
