#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:51:28 2020

@author: sorinraducuoprisa
"""

import requests
import json

# Olga adds an item for auction with an expiration time using her token
url = "http://193.61.36.135:8000/authentication/token/"
user= {
            'username': 'Olga',
            'password':'olga'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print(user_token) 

auction_url = "http://193.61.36.135:8000/newAuction/auction/add/"# Our API!
headers = {'Authorization': 'Bearer '+str(user_token)} 

auctionItem1 = {
    "title": "Teddy beat",
    "endDate": "2020-04-19T22:00:00Z",
    "price": 10,
   	"description": "Fluffy toy, perfect for kids"
}
response = requests.post(auction_url, headers=headers, data=auctionItem1)

