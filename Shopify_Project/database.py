import sqlite3



def createTable():

    conn = sqlite3.connect('Shopify.db.sqlite')
    cur = conn.cursor()

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
        CreditCard INTEGER,
        CardFirstName VARCHAR(30),
        CardLastName VARCHAR(50),
        CardExpire VARCHAR(5),
        CVV INTEGER
        );"""

    cur.execute(createTable)
    conn.commit()
    print("record created")
    conn.close()


if __name__ == '__main__':
    createTable()
