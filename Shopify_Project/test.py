import sqlite3

conn = sqlite3.connect('Shopify.db.sqlite')
cur = conn.cursor()

def createTable():

    # Statement for Creating the Users Table
    createTable = """CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Email VARCHAR(50),
        FirstName VARCHAR(30),
        LastName VARCHAR(50),
        ShipAddr1 VARCHAR(40),
        ShipAddr2 VARCHAR(40),
        ShipCity VARCHAR(25),
        State VARCHAR(25),
        Zip INTEGER,
        PhoneNumber VARCHAR(12),
        ShippingisBilling BOOLEAN,
        CreditCard INTEGER,
        CardName VARCHAR(30),
        CardExpire VARCHAR(5),
        CVV INTEGER
        );"""

    cur.execute(createTable)
    conn.commit()
    print("Table created")


def getUserInfo():
    email = raw_input("Enter your email: ")
    fName = raw_input("Enter your First Name: ")
    lName = raw_input("Enter your Last Name: ")
    shipAddr = raw_input("Enter your Shipping Address: ")
    shipCity = raw_input("Enter your Shipping City: ")
    state = raw_input("Enter your Shipping State: ")
    zip = raw_input("Enter your Zip Code: ")
    phone = raw_input("Enter your Phone Number: ")

    # Find whether or not billing and shipping addresses are the same (yes = 1 no = 0)
    shippingbilling = raw_input("Is your shipping address also your billing address? (y/n)")
    shipbillsame = 0
    if shippingbilling == 'y':
        shipbillsame = 1

    card = raw_input("Enter your Credit Card Number: ")
    cardFullName = raw_input("Enter the Name on the Card: ")
    cardExpire = raw_input("Enter the expiration date: ")
    cvv = raw_input("Enter the 3 digit code on the back: ")

    userInfo = (email, fName, lName, shipAddr, '', shipCity, state, zip, phone, shipbillsame, card, cardFullName, cardExpire, cvv)

    # Statement for Inserting a new user into the Users Table
    cur.execute("INSERT INTO Users('Email', 'FirstName', 'LastName', 'ShipAddr1', 'ShipAddr2', 'ShipCity', 'State', 'Zip', 'PhoneNumber', 'ShippingisBilling', 'CreditCard', 'CardName', 'CardExpire', 'CVV')"
              "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", userInfo)
    conn.commit()
    print("Record inserted")
    conn.close()


if __name__ == '__main__':
    createTable()
    getUserInfo()
