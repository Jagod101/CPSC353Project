import urllib
import requests
import json
from pprint import pprint
from selenium import webdriver
from cart import Cart
from user_preferences import User

url = "https://www.alphaleteathletics.com/products.json"
baseUrl = "https://www.alphaleteathletics.com/cart/"
# r = requests.get("https://www.gymshark.com/products.json".decode('utf-8'))
# print(r.json())

resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below

def get_user_details():
    # global product_name
    # product_name = raw_input("Please enter the name of the product you would like to purchase")
    global product_size
    product_size = raw_input("Please enter the size of the product you would like to purchase, for example: 'S' for small\n")

def get_value(searchFor):
    get_user_details()
    for key,value in data.items():
        for products in data['products']:
            print products['title']
            if products['title'] == searchFor:
                for variants in products['variants']:
                    print variants
                    if variants['title'] == product_size:
                        checkoutUrl = baseUrl + str(variants['id']) + ":1"
                        print(checkoutUrl)
                        exit()

# def checkout():




print(get_value("Men's Joggers - Blackberry"))
