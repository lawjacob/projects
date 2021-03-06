# Password generator and manager
#### Video Demo:  https://youtu.be/D0qk7EUvyt8
#### Description:
This is a password manager that allows you to create, view, store, and delete passwords.

## Language:
All code is written in Python. 

## Main program:
The main program(password.py) is a command-line interface that allows you to create, view, store, and delete passwords.

## Special features:
* The program can handle multiple passwords linked with same website and email.
* The program allow backup and restore of passwords.
* Information is displayed prettily with help of prettytable module.

## Modules:
* prettytable: used to display information prettily.
* sqlite3
* random
* csv

## Database:
Sqlite3 is used as the database.
databse is named "passwords.db"
    Structure:
    |id|name of website|email address|password|

## Funtions explained:
There are 10 main function in the program:
1. Generate a new password and memorise it in the database.
2. Store user's inputted password in the database.
3. Search password with the name of website.
4. view all accounts connected to the same password.
5. Update a password.
6. Delete a password.
7. Delete all passwords in the table.
8. save all passwords in the table to a csv file.
9. load all passwords in the table from a csv file.
10. View all passwords in the table.


## Function 1: Generateing passwords:
    - The user can generate a new, strong password by entering the website name and the password length.

    - It is designed to generate password with most complex and most variety of charater types(including symbols/number/capital letter/lower case letters). As the password manager would memorise the password for user, the password can be as complex as possible without concerning of forgetting it.

    - The password is generated with the following rules:
        1. The password should be at least 8 characters long.
        2. The password should contain at least one number.
        3. The password should contain at least one uppercase letter.
        4. The password should contain at least one lowercase letter.
        5. The password should contain at least one symbol.
        6. The password should not contain any space.

    - As the password generated by random maybe not meet the rules(e.g AAaa00118), which means the password is not strong enough, the program will modify password by changing random digit of password to the lacking character type(e.g. symbol) until it meets the rules.

## Function 2: Storing passwords:
    - The program will store the password and related information(website's name, email address) user inputted in the database.

    - Strength of password stored under this program is not guaranteed. The strength of password determined by the user.

## Function 3: Searching passwords:
    - The user can search the password with the website name.

    - The program will return the password and related information(website's name, email address) stored in the database.

    - The program will display all passwords with same website name if there is multiple passwords(for different accounts).

## Function 4: View accounts connected to same password:
    - The user can view all accounts connected to the same password.

    - User may reuse same passwords for many websites which can be a security risk. Through this program, the user can view all accounts connected to the same password and change the password for the accounts with function 5.

## Function 5: Updating passwords:
    - The user can update the password for the accounts.

    - This program will first display all information(id, name of webistes, email address, passwords) stored in databse.
    - The user can choose the id of the account he/she wants to update.
    - The user can input the new password for the account.
    - The program will update the password for the account.

## Function 6: Deleting a password:
    - The user can delete a password of a webiste.

    - The program will ask user for the website name.

    - if the website name is correct and there is only one password connected to the website, the program will delete the password and related information in the database.

    - if the website name is correct and there are multiple passwords connected to the website, the program will ask user for the id of the account he/she wants to delete.

    - if the website name is correct and the account id is correct, the program will delete the password and related information in the database.

## Function 7: Deleting all passwords:
    - If the user wants to delete all passwords in the database, the program will ask user for confirmation.

    - If the user confirms, the program will delete all passwords in the database.

    - If the user cancels, the program will do nothing.

## Function 8: Backuping passwords:
    - The user can backup all passwords in the database to a csv file named pwd.csv.

## Function 9: loading bakcuped passwords:
    - The user can load backuped passwords from a csv file named pwd.csv.

## Function 10: View all passwords:
    - The user can view all passwords in the database.