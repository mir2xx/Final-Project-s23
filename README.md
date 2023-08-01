# Password Manager
In this project you will create a password manager system that will store passwords, usernames and sites. Passwords will need to be [encrtpted](https://cloud.google.com/learn/what-is-encryption#:~:text=started%20for%20free-,Encryption%20defined,unscramble%20it%20can%20access%20it.) and decrypted (reversing the encryption). Here are the files you should have:
- main.py
- manager.py
- cryptography.py
- test.py
- passwords.txt
## main.py
Your main.py file will be the main runner of the project. It will prompt you for a password and after correctly inputting the password it will give you a list of options for you to do. It should look like this: 
1. Generate password
2. Get Login
3. Add password
4. Update password
5. Delete password
6. Quit

After running through the option selected the user will return to this menu
### Generate password
This will ask the user to input the site name, username, and password length. It will then print the password and save the information
### Get Login
This will ask the user for the site name and will then print the username and password
### Add password
This will ask the user for the site name, username and password. It will then save this information
### Update password
This will ask the user for the site name and user name. It will then ask if the user wants to enter their own password or generate a new password. Depending on what the user selects it will then replace the old password with the new one
### Delete Password
This will ask the user for the site name. It will then remove the password and login information
### Quit
This will save all changes made into [passwords.txt](#passwordstxt) and end the program
## manager.py
This file will contain the Manager Class and will be used to manage all the data. Some of the code has been written for you, you will need to complete these functions:
- __init__
- save
- load
- generate_password
- get_password
- update_password
- add_password
- delete_password

### __init__
Input: None
Output: None
The init function is how we initialize objects in python. Most of this function has been written for you but you will need to finish the code where it is commeted out
### save
Input: None
Output: None
The save function will take all the data saved in the safe variable and put it into the [password.txt](#passwordstxt) file.
### load
Input: None
Output: None
The load function does the opposite of the save function and it will read the data from the [password.txt](#passwordstxt) file and store it into your program.
### save_ password
Inputs: site, username, password
Output: None
Takes site, username & password and saves it into self.safe variable
### generate_password
Inputs: site, username, password length
Output: generated password
The generate password function will randomly generate a password with the specified length. It should contain at least:
- 1 lowercase
- 1 uppercase
- 1 number
- 1 special character

The function will then return the new password
### get_password
Inputs: site, username
Output: password
The get password function should retrieve the password that matches the site and username provided 
### update_password
Inputs: site, username, new password
Output: None
The update password function will replace the current password with the new password
### delete_password
Inputs: site, username
Output: site, username, password
Removes the data related to site and username provided

## cryptography.py
This file will contain the Cryptography Class and will be used to encrypt and decrypt your data. There is already some code written you will need to write the encrypt & decrypt methods. You will also need to come up with your own encryption & decryption algorithms. Here are some useful research links:
- [Substitution Encryption](https://www.csfieldguide.org.nz/en/chapters/coding-encryption/substitution-ciphers/#:~:text=A%20substitution%20cipher%20simply%20means,H's%2C%20E's%2C%20and%20L's.)
- [Ceasar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
- [Transposition Cipher](https://en.wikipedia.org/wiki/Transposition_cipher)
- [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

It is not expected you create a modern/advanced encryption algorithm but it should meet these requirements:
- Is more than a simple substitution or transposition cipher
- Uses a key
## test.py
This is a testing file that you should use to test both [cryptography.py](#cryptographypypy) & [manager.py](#managerpy)
Some tests have been provided but you should write some extra ones or modify the ones written.
## passwords.txt
This is where you will save your data to instead of a database
## Possible Enhancements
If you finish early and want an extra challenge here are some enhancements you can add
- Instead of only encrypting the password try encrypting the usernames and site names aswell
- Instead of only having one username and password per site site try making it so that you can have multiple usernames and passwords for a site
- What happens when your encryption key gets leaked? Add a way to change the encryption key. hint: you will need anothere .txt file
- What if multiple people want to use the password manager? Add a functionality that allows multiple users. But remember Each user should only be able to access their own passwords and nobodies elses. 
