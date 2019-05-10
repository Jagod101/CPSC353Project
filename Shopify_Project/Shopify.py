import urllib
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

url = "https://www.gymshark.com/products.json"
baseUrl = "https://www.gymshark.com/cart/"

resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below
start_time = time.time()

def get_value(searchFor,product_size):
    global checkoutUrl
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
    chromedriver = '/Users/ryanklapper/Desktop/Shopify_Project/chromedriver' #Use for mac
    #chromedriver = webdriver.Chrome(executable_path=r"C:\Users\Ashley-Laptop\Downloads\chromedriver_win32\chromedriver.exe") #Use for windows
    # driver = webdriver.Chrome() #Use for windows
    # chrome_options.add_argument("--headless") #Use for mac - headless browser
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    driver.get(checkoutUrl)

def information():
    print('Entering shipping info...')
    email = driver.find_element_by_id('checkout_email')
    email.send_keys('test@gmail.com')

    first_name = driver.find_element_by_id('checkout_shipping_address_first_name')
    first_name.send_keys('Jane')

    last_name = driver.find_element_by_id('checkout_shipping_address_last_name')
    last_name.send_keys('Doe')

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
    print('Selecting shipping rate...')
    payment_button = driver.find_element_by_name('button').click()
    time.sleep(1)


def payment():
    #https://stackoverflow.com/questions/16702066/how-do-i-get-around-this-error-webelement-does-not-support-indexingwebdriver
    # time.sleep(1)
    try:
        #First frame block
        print('Submitting payment...')
        iframe = driver.switch_to.frame(driver.find_elements_by_class_name('card-fields-iframe')[0]) #Frame number 1
        credit_card_number = driver.find_element_by_id('number')
        credit_card_number.send_keys('4342923222931029')
        credit_card_number.send_keys(Keys.TAB)

        #Second frame block
        driver.switch_to.default_content()
        cc = driver.switch_to.frame(driver.find_elements_by_class_name('card-fields-iframe')[1]) #Frame number 2
        credit_card_name = driver.find_element_by_id('name')
        credit_card_name.send_keys("Jane Doe")
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

        div_section_content = driver.find_element_by_class_name('section__content')
        content_box = driver.find_element_by_class_name('content-box')
        checkout_different_billing_address_false = driver.find_element_by_id('checkout_different_billing_address_false')
        if checkout_different_billing_address_false:
            div = driver.find_element_by_class_name('step__footer')
            div_button = driver.find_element_by_class_name('shown-if-js')
            button = driver.find_elements_by_tag_name('button')[2].click()
            time.sleep(1)
            error_message = driver.find_element_by_id('error-for-number')
            if error_message:
                print('Payment declined')
                print("It took", time.time() - start_time, "to find your product and for you to be broke")
                driver.close()
            else:
                print('SUCCESS')
                print("It took", time.time() - start_time, "to find your product and checkout")
                driver.close()
        else:
            checkout_billing_address_first_name = driver.find_element_by_id('checkout_billing_address_first_name')
            checkout_billing_address_first_name.send_keys('Jane')

            checkout_billing_address_last_name = driver.find_element_by_id('checkout_billing_address_last_name')
            checkout_billing_address_last_name.send_keys('Doe')

            checkout_billing_address_address1 = driver.find_element_by_id('checkout_billing_address_address1')
            checkout_billing_address_address1.send_keys('123 Test Road')

            checkout_billing_address_address2 = driver.find_element_by_id('checkout_billing_address_address2')
            checkout_billing_address_address2.send_keys('')

            checkout_billing_address_city = driver.find_element_by_id('checkout_billing_address_city')
            checkout_billing_address_city.send_keys('Orange')
            scroll = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            checkout_billing_address_country = driver.find_element_by_id('checkout_billing_address_country')
            checkout_billing_address_country.send_keys('United States')

            checkout_billing_address_province = driver.find_element_by_id('checkout_billing_address_province')
            checkout_billing_address_province.send_keys('CA')

            checkout_billing_address_zip = driver.find_element_by_id('checkout_billing_address_zip')
            checkout_billing_address_zip.send_keys('92866')

            checkout_billing_address_phone = driver.find_element_by_id('checkout_billing_address_phone')
            checkout_billing_address_phone.send_keys('6503886500')



            div = driver.find_element_by_class_name('step__footer')
            div_button = driver.find_element_by_class_name('shown-if-js')
            button = driver.find_elements_by_tag_name('button')[2].click()
            time.sleep(1)
            error_message = driver.find_element_by_id('error-for-number')
            if error_message:
                print('Payment declined')
                print("It took", time.time() - start_time, "to find your product and for you to be broke")
                driver.close()
            else:
                print('SUCCESS')
                print("It took", time.time() - start_time, "to find your product and checkout")
                driver.close()

    except NoSuchElementException:
        assert 0, "can't find input with number id"
        time.sleep(2)

def get_titles():
    for products in data['products']:
        print products['title']

print(get_value("Gymshark Isla Knit Sweater - Dusky Pink", 'Medium'))
# get_titles()
