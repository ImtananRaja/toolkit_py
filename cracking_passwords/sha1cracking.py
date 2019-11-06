#!/usr/bin/python

# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt

# this library allows us to request pages from internet and
# also lets us open the page
from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input("[*] please Enter a sha1 hash: ")

# open and read the file in utf-8 mode
passwordList = str(urlopen(
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(),
                   'utf-8')

# loop over the rows, ignore the new lines
for password in passwordList.split("\n"):
    # This is turning the password in to a hash using sha1
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    # comparing the hash passed in vs the hash from the file
    if hashguess == sha1hash:
        print(colored("[+] The password is: " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] Password guess: " + str(password) + " does not match, trying next..", 'red'))
print("Password not in password list")