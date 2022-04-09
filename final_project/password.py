import sqlite3
import random
from prettytable import PrettyTable
import csv

#generate a random password passing in a length
def generate_password(length:int):
    password = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    higher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "!@#$%^&*()_+.?"
    for i in range(length):
        password += random.choice(lower + higher + number + symbol)
    password = list(password)
    #ensure the pwd consist of at least one lowercase letter, one uppercase letter, one number, and one special character
    while not any(c in password for c in lower):
        password[random.randrange(0,length)] = random.choice(lower)
    while not any(c in password for c in higher):
        password[random.randrange(0,length)] = random.choice(higher)
    while not any(c in password for c in number):
        password[random.randrange(0,length)] = random.choice(number)
    while not any(c in password for c in symbol):
        password[random.randrange(0,length)] = random.choice(symbol)
    password = "".join(password)
    return password

def check(email):
    #check if email is valid
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if len(email) < 5:
        return False
    return True


def print_menu():
    print("""
    +-----------------------------------------------+
    |1. Generate a new random password              |
    |2. Store a new password                        |
    |3. View password via name of website           |
    |4. View all accounts connected to a password   |
    |5. Update a password                           |
    |6. Delete a password via name of website       |
    |7. Delete all passwords records                |
    |8. save all info in pwd.csv                    |
    |9. Import data from pwd.csv                    |
    |10. View all                                   |
    |0. Exit                                        |
    +-----------------------------------------------+
    """)

#main
db = sqlite3.connect("password.db")
db.execute("CREATE TABLE IF NOT EXISTS passwords (ID INTEGER PRIMARY KEY UNIQUE, web_name TEXT, email TEXT, pwd TEXT);")

while True:
    print_menu()

    # Invalid input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number")
        exit()

    if choice < 0 or choice > 10:
        print("Please enter a number between 0 and 10")
        exit()

    # Case 0: Exit
    if choice == 0:
        print("Exiting...")
        break

    # Case 1: Create a new password
    if choice == 1:
        web_name = input("Input the name of the website or app: ")
        # if null input, exit
        if not web_name:
            print("Please enter a name")
            exit()

        email = input("Input the email address: ")
        if not email:
            print("Please enter an email")
            exit()

        # if email is not valid, exit
        if check(email) == False:
            print("Please enter a valid email address")
            exit()

        # if valid length of password
        try:
            length = int(input("Input the length of the password more than 8: "))
        except ValueError:
            print("Please enter a number")
            exit()
        
        if length < 8:
            print("Please enter a number greater than 8")
            exit()

        #generate a strong password

        pwd = generate_password(length)
        print("Creating a new password...")
        db.execute("INSERT INTO passwords (web_name, email, pwd) VALUES (?, ?, ?);", (web_name, email, pwd))
        db.commit()
        print("New password created for {} is {}! ".format(web_name, pwd))
    
    # Case 2: Store a new password
    if choice == 2:
        web_name = input("Input the name of the website or app: ")
       
        # if null input, exit
        if not web_name:
            print("Please enter a name")
            exit()
        email = input("Input the email address: ")
        if not email:
            print("Please enter an email")
            exit()
        
        # if email is not valid, exit
        if check(email) == False:
            print("Please enter a valid email address")
            exit()
        pwd = input("Input the password: ")
        if not pwd:
            print("Please enter a password")
            exit()
        
        print("Storing a new password...")
        
        db.execute("INSERT INTO passwords (web_name, email, pwd) VALUES (?, ?, ?);", (web_name, email, pwd))
        db.commit()
        print("New password stored for {} is {}! ".format(web_name, pwd))

    # Case 3: View password via name of website
    if choice == 3:
        web_name = input("Input the name of the website or app: ")
        # if null input, exit
        if not web_name:
            print("Please enter a name")
            exit()

        print("Viewing password...")

        cursor = db.execute("SELECT * FROM passwords WHERE web_name = ?;", (web_name, ))
        table3 = PrettyTable(["Web Name", "Email address","Password"])
        for row in cursor:
            table3.add_row([row[1],row[2], row[3]])
        print(table3)

    # Case 4: View all accounts connected to the same password
    if choice == 4:
        pwd = input("Input the password: ")
        # if null input, exit
        if not pwd:
            print("Please enter a password")
            exit()
        print("Viewing all accounts connected to {}...".format(pwd))
        cursor = db.execute("SELECT * FROM passwords WHERE pwd = ?;", (pwd, ))
        table4 = PrettyTable(["ID", "Web Name", "Email"])
        for row in cursor:
            table4.add_row([row[0], row[1], row[2]])
        print(table4)

    # Case 5: Update a password
    if choice == 5:
        print("Viewing all passwords...")
        all = db.execute("SELECT * FROM passwords;").fetchall()

        if not all:
            print("No passwords found")
            db.execute("DELETE FROM passwords;")
            db.commit()
            print("All passwords deleted")
            continue
        
        id = db.execute("SELECT ID FROM passwords;").fetchall()
        if all == id: # if all is the same as only id
            db.close
            db = sqlite3.connect("password.db")
            all = db.execute("SELECT * FROM passwords;")
        table = PrettyTable(["ID", "Web Name", "Email", "Password"])
        for row in all:
            table.add_row([row[0], row[1], row[2], row[3]])
        print(table)

        id = input("Input the ID of the password you want to update: ")
        pwd = input("Input the new password: ")
        if not pwd:
            print("Please enter a password")
            exit()
        print("Updating password...")
        db.execute("UPDATE passwords SET pwd = ? WHERE ID = ?;", (pwd, id,))
        db.commit()
        print("Password updated for password id: {} is {}! ".format(id, pwd))

    # Case 6: Delete a password
    if choice == 6:
        web_name = input("Input the name of the website or app: ")
        # if null input, exit
        if not web_name:
            print("Please enter a name")
            exit()

        all = db.execute("SELECT * FROM passwords WHERE web_name = ?;", (web_name,))
        if not all:
            print("No password found for {}".format(web_name))
            exit()

        #getting len of "all"
        db.row_factory = lambda cursor, row: row[0]
        fetch_len = len(db.execute("SELECT * FROM passwords WHERE web_name = ?;", (web_name, )).fetchall())
        if fetch_len > 1:
            print("Multiple passwords found for {}".format(web_name))
            print("Which one do you want to delete?")
            t = PrettyTable(["ID","Web Name","Email","Password"])
            ids = []
            for i in all:
                t.add_row([i[0], i[1], i[2], i[3]])
                ids.append(i[0])
            print(t)

            try:
                id = int(input("Enter the ID: "))
            except ValueError:
                print("Please enter a number")
                exit()

            if id not in (ids):
                print("Please enter a number within id displayed")
                exit()

            print("Deleting password...")
            db.execute("DELETE FROM passwords WHERE ID = ?;", (id,))
            db.commit()
            print("Password deleted for {}".format(web_name))
            db.close
            db = sqlite3.connect("password.db")
        else:
            print("Deleting password...")
            db.execute("DELETE FROM passwords WHERE web_name = ?;", (web_name,))
            db.commit()
            print("Password deleted for {}".format(web_name))
            db.close
            db = sqlite3.connect("password.db")
    
    # Case 7: Delete all passwords and save in pwd.csv
    if choice == 7:
        print("Deleting all passwords...")
        confirmation = input("You really wante to delete all passwords? (y/n): ")
        if confirmation in ("y", "Y"):
            db.execute("DELETE FROM passwords;")
            print("All passwords deleted")
            db.commit()
            db.close
            db = sqlite3.connect("password.db")
        else:
            print("Cancelled")

    # Case 8: Save records in pwd.csv
    if choice == 8:
        print("Saving...")
        with open("pwd.csv", "w") as f:
            f.write("web_name,email,pwd\n")
            all = db.execute("SELECT * FROM passwords;")
            for row in all:
                f.write("{},{},{}\n".format(row[1], row[2], row[3]))
        print("Saved!")

    # Case 9: Input data from pwd.csv file
    if choice == 9:
        print("Inputing data from pwd.csv...")
        try:
            with open("pwd.csv", "r") as f:
                db.execute("DELETE FROM passwords;")
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    db.execute("INSERT INTO passwords (web_name, email, pwd) VALUES (?, ?, ?);", (row[0], row[1], row[2]))
                    db.commit()
            print("Data inputed!")
            
        except FileNotFoundError:
            print("File not found")
            exit()

    # Case 10: View all
    if choice == 10:
        print("Viewing all passwords...")
        all = db.execute("SELECT * FROM passwords;").fetchall()

        if not all:
            print("No passwords found")
            db.execute("DELETE FROM passwords;")
            db.commit()
            print("All passwords deleted")
            continue
        
        id = db.execute("SELECT ID FROM passwords;").fetchall()
        if all == id: # if all is the same as only id
            db.close
            db = sqlite3.connect("password.db")
            all = db.execute("SELECT * FROM passwords;")
        table = PrettyTable(["Web Name", "Email", "Password"])
        for row in all:
            table.add_row([row[1], row[2], row[3]])
        print(table)
    
db.close