#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:44:34 2020

@author: sorinraducuoprisa
"""

import requests

# Olga trying to create an auction without using a token
url = "http://193.61.36.135:8000/newAuction/auction/add/"
user= {
            'username': 'Olga',
            'password':'olga'
        }
response = requests.get(url)
json_response = response.json()
print(json_response)
