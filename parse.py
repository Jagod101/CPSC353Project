# parse.py
# Author: Zach Jagoda, Ashley Wood, Ryan Klapper, Cole Gotelli
# Email: jagod101@mail.chapman.edu
# Course: CPSC 353
# Assignment: CPSC353 Final Project - Shop-ify
# Date: 4/14/19

import urllib
import json

itemName = raw_input("Please Enter an Item: ")
itemColor = raw_input("Please Enter the Items Color: ")

print(itemName.lower())
print(itemColor.lower())

url = "https://www.gymshark.com/products.json"

response = urllib.urlopen(url)
data = json.load(response)

# print(data)

# shopifyDataFile = open("shopifyData.json", "w")
# shopifyDataFile.write(json.dumps(json.loads(data), indent=4, sort_keys=True))
# shopifyDataFile.close()

def search(data, searchFor):
    for key, value in data.items():
        for v in value:
            if searchFor in v:
                return key
    # return None

print(search(data, itemName))