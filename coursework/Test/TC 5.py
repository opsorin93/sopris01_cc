#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:26:10 2020

@author: sorinraducuoprisa
"""

import requests
import json

# Nick adds an item for auction with an expiration time using his token
url = "http://193.61.36.135:8000/authentication/token/"
user= {
            'username': 'Nick',
            'password':'nick'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print(user_token) 

auction_url = "http://193.61.36.135:8000/newAuction/auction/add/"# Our API!
headers = {'Authorization': 'Bearer '+str(user_token)} 

auctionItem2 = {
    "title": "Jack Daniels",
    "endDate": "2020-04-19T22:01:00Z",
    "price": 20,
   	"description": "Strong whiskey"
}
response = requests.post(auction_url, headers=headers, data=auctionItem2)