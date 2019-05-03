import urllib
import requests
import json
import os
import pprint
import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from splinter import Browser
import webbrowser
from cart import Cart

url = "https://www.gymshark.com/products.json"
baseUrl = "https://www.gymshark.com/cart/"
# r = requests.get("https://www.gymshark.com/products.json".decode('utf-8'))
# print(r.json())

resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below
start_time = time.time()

def get_user_details():
    # global product_name
    # product_name = raw_input("Please enter the name of the product you would like to purchase")
    global product_size
    # product_size = raw_input("Please enter the size of the product you would like to purchase, for example: Medium\n")

def get_value(searchFor,product_size):
    global checkoutUrl
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
                        checkout()
                        information()
                        payment()

def checkout():
    chrome_options = Options()
    global driver
    chromedriver = '/Users/ryanklapper/Desktop/Shopify_Project/chromedriver'
    #driver = webdriver.Chrome(executable_path=r"C:\Users\Ashley-Laptop\Downloads\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    driver.get(checkoutUrl)

def information():
    # global N
    print('Entering shipping info...')
    email = driver.find_element_by_id('checkout_email')
    email.send_keys('ryan.klapper.MA@gmail.com')

    first_name = driver.find_element_by_id('checkout_shipping_address_first_name')
    first_name.send_keys('Ryan')

    last_name = driver.find_element_by_id('checkout_shipping_address_last_name')
    last_name.send_keys('Klapper')

    address_1 = driver.find_element_by_id('checkout_shipping_address_address1')
    address_1.send_keys('123 Test Road')

    address_2 = driver.find_element_by_id('checkout_shipping_address_address2')
    address_2.send_keys('')

    address_city = driver.find_element_by_id('checkout_shipping_address_city')
    address_city.send_keys('Orange')
    # Not needed on Gymshark
    # country = driver.find_element_by_id('checkout_shipping_address_country')
    # country.send_keys('United States')
    # country.send_keys(Keys.TAB)
    address_state = driver.find_element_by_id('checkout_shipping_address_province')
    address_state.send_keys('California')

    address_zip = driver.find_element_by_id('checkout_shipping_address_zip')
    address_zip.send_keys('92866')

    address_phone = driver.find_element_by_id('checkout_shipping_address_phone')
    address_phone.send_keys('6503886500')
    address_phone.send_keys(Keys.TAB)

    time.sleep(0.5)
    button = driver.find_element_by_name('button').click()
    # time.sleep(2)
    print('Selecting shipping rate...')
    payment_button = driver.find_element_by_name('button').click()
    time.sleep(1)


def payment():
    #https://stackoverflow.com/questions/16702066/how-do-i-get-around-this-error-webelement-does-not-support-indexingwebdriver
    # time.sleep(1)
    try:
        #First frame block
        print('Entering billing info...')
        iframe = driver.switch_to.frame(driver.find_elements_by_class_name('card-fields-iframe')[0]) #Frame number 1
        credit_card_number = driver.find_element_by_id('number')
        credit_card_number.send_keys('4342923222931029')
        credit_card_number.send_keys(Keys.TAB)

        #Second frame block
        driver.switch_to.default_content()
        cc = driver.switch_to.frame(driver.find_elements_by_class_name('card-fields-iframe')[1]) #Frame number 2
        credit_card_name = driver.find_element_by_id('name')
        credit_card_name.send_keys("Ryan Klapper")
        credit_card_name.send_keys(Keys.TAB)

        #Third frame block
        driver.switch_to.default_content()
        cced = driver.switch_to.frame(driver.find_elements_by_class_name('card-fields-iframe')[2]) #Frame number 3
        credit_card_expiration_date = driver.find_element_by_id('expiry')
        credit_card_expiration_date.send_keys('06/21')
        credit_card_expiration_date.send_keys(Keys.TAB)

        #Fourth frame block
        driver.switch_to.default_content()
        csv = driver.switch_to.frame(driver.find_elements_by_class_name('card-fields-iframe')[3]) #Frame number 4
        credit_card_security_value = driver.find_element_by_id('verification_value')
        credit_card_security_value.send_keys('221')
        credit_card_security_value.send_keys(Keys.TAB)

        #Complete order button pressed
        driver.switch_to.default_content()
        scroll = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        div = driver.find_element_by_class_name('step__footer')

        print('SUCCESS')
        print("It took", time.time() - start_time, "to find your product and checkout")

    except NoSuchElementException:
        assert 0, "can't find input with number id"
        time.sleep(2)
        # driver.close()

def get_titles():
    for products in data['products']:
        print products['title']

print(get_value("Gymshark Legacy Luxe Tank - Chalk White", 'Medium'))
# get_titles()
