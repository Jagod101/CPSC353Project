# CPSC353 Project - Shopify-ing the Consumer World

### Abstract
Online shopping has become an absolute nightmare for the average consumer who wishes to purchase an item that is highly sought after. Our project combats the already intense bot-marketplace. We are creating a cloud-based shopify bot that has the capability to purchase an item at a blazing fast speed. We chose shopify as the main base of this project is due to the growing community of shopify websites that are now taking over the e-commerce space. We want this bot to be universal across many different websites, not just one in particular. The user enters the url of the website, chooses specific keywords (this is how the bot finds the item), and makes a profile. This profile contains the users information that is required for purchasing an item. The bot also has connections to discord and slack, meaning anytime there is a purchase or decline on your credit card, you will receive a discord or slack notification. This is done via discord or slack webhooks. By having the bot cloud-based, it optimizes speed tremendously.

### Installing

To start things off, you will need to make a couple of installations:

```
pip install urllib
pip install requests
pip install json
pip install time
pip install selenium
```
After these are installed, you will be good to go!

### Running Instructions
```
If you are running in windows:
```
  - You must have your chromedriver in C:/Python27/Scripts (On windows, you need to add .exe to the path of the chromedriver)
  - You must have selenium,requests, urllib, json, and time installed in python 2.7
  - In the checkout function, simply edit line 36 to the location of where the chromedriver is
```
If you are running on mac:
```
  - You must have your chromedriver in the correct path as the folder
  - You must have selenium (webdriver,Keys,NoSuchElement,Options) ,requests, urllib, json, and time installed in python 2.7
  - In the checkout function, simply edit line 35 to the location of where the chromedriver is

### Break down into end to end tests

On line 189, there is a function named:
```
get_titles()
```
--> Run that function first and comment out the print statement and function call on line 188 

--> This will return the top products on the gymshark website.

--> To run the program, simply copy a title that was returned from the function get_titles()

--> Paste this title in quotation marks as the first parameter of the get_value(searchFor,product_size)

--> To select a size, please enter a size of an article of clothing

## Built With

* [Python](https://docs.python.org/2.7/) - Language used to develop
* [Selenium](https://selenium-python.readthedocs.io/) - Used to interact with browser
* [Requests](https://realpython.com/python-requests/) - Used to extract data from browser
* [Urllib](https://docs.python.org/2/library/urllib.html) - Ability to visit specifc URLs
* [Json](https://docs.python.org/3/library/json.html) - Ability to encode and decode json
* [Time](https://docs.python.org/2/library/time.html) - Used for browser to wait a specific amount of time

## Authors

* **Ryan Klapper** - *klapp101@mail.chapman.edu* - Data Analytics
* **Ashley Wood** - *wood198@mail.chapman.edu* - Computer Science
* **Cole Gotelli** - *gotel100@mail.chapman.edu* - Computer Science
* **Zach Jagoda** - *jagod101@mail.chapman.edu* - Computer Science

### Faculty Advisor
Michael Fahy, fahy@chapman.edu
