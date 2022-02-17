# -*- coding: utf-8 -*-
"""
reddit_collector.py
reddit collector script

Usage: reddit_collector.py

Example: python3 reddit_collector.py
"""

"""
Description: Data from the following list of search terms will be collected from reddit:
{Bitcoin, Ethereum, Dogecoin, Cryptocurrency}

For each term, a request will be sent to the pushshift API to collect a random sample of 
comments for every day, starting from two years ago
The API returns a JSON formatted string, which can be converted to a dictionary by using 
the requests.json() method. 
This new dictionary has the 'data' key and sometimes the 'metadata' key.

The Pandas library is used to convert the dictionary into a DataFrame, 
which is then written to a .csv file. 

"""

import sys
import requests
import pandas as pd
import numpy as np
import pickle
import ipdb

def query_reddit(subreddit = None, from_date=None, until_date=None, search_query = None, size = 100):
    # TODO
    # Using PushShift API, scrape reddit comments related to {Bitcoin, Ethereum, Dogecoin, Cryptocurrency}
    # return a DataFrame of comments, columns should be 'body', 'created_utc', 'total_awards_received', 'subreddit'

    search_query_url = "https://api.pushshift.io/reddit/search/comment/?q=" + search_query + "&before=" + str(until_date) + "d&after=" + str(from_date) + "d&size=" + str(size)
    return requests.get(search_query_url)

def utc_to_datetime(date: int)-> str:
    # convert UTC in unix time to datetime object
    years = #
    months = #
    days = #
    
    return reformatted_date

def clean_data(reddit_data: list, columns: list = None)-> list:
  """
  """
  # TODO
  # append comment lists to a new list, keeping elements that correspond to the passed in parameters 
  pre_df = [columns]
  for comment in reddit_data:
      appending = []
      for column in columns:
          appending.append(comment[column])
      pre_df.append(appending)
  df = pd.DataFrame(data=pre_df[1:], columns=pre_df[0])
  return df

def main(filepath: str, queries: list, column_names: list)-> None:
    """

    :param filepath:
    :param queries:
    :param column_names:
    :return:
    """

    # Import all data from reddit first
    # Store it in a list of dictionaries    
    df = pd.DataFrame()
    
    # for every query in the list, we search reddit comments
    for query in queries:

        dataf = pd.DataFrame(columns=column_names)
        for date in range(730, -1, -1):
            cont = True
            while cont:
                try:
                    comments = query_reddit(from_date=date, until_date=date - 1, search_query=query)
                    comments = comments.json()
                    cont = False
                except JSONDecodeError:
                    pass
            data_to_append = clean_data(comments["data"], columns=column_names)
            dataf = pd.concat([dataf, data_to_append])
            print(data_to_append.head())
        dataf.to_csv(filepath + query + ".csv", index=False)

def convert_date(date: int):

if __name__ == "__main__":

    # for every day since two years ago, collect 1000 comments returned
    # from the query and add it to the csv file for that particular query
    # df = pd.read_csv("~/PycharmProjects/pythonProject/reddit_data_sets/dogecoin.csv")
    
    filepath = "/home/alden/PycharmProjects/pythonProject/reddit_data_sets/"
    queries = ["bitcoin", "dogecoin", "ethereum", "cryptocurrency", "economics", "finance", "politics", "election"]
    # column_names = ['body', 'created_utc', 'total_awards_received', 'subreddit']

    main(filepath, queries, column_names)
