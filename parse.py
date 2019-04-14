# parse.py
# Author: Zach Jagoda
# Email: jagod101@mail.chapman.edu
# Course: CPSC 353
# Assignment: CPSC353 Final Project - Shop-ify
# Date: 4/14/19

import urllib
import json

url = "https://www.gymshark.com/products.json"

response = urllib.urlopen(url)
data = json.loads(response.read())

# print(data)

itemName = raw_input('Please Enter an Item: ')
itemColor = raw_input('Please Enter the Items Color: ')

