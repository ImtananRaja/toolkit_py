#!/usr/bin/python

from termcolor import colored
import hashlib

def tryOpen(passwordFile):
    try:
        passFile = open(passwordFile, "r")
        return passFile
    except:
        print("No such file in path!")
        quit()

def getMd5Pass(passFile, passwordHash):
    for password in passFile:
        print(colored("Trying: " + password.strip("\n"), 'blue'))
        # Have to encode word because it is python3
        encodePass = password.encode('utf-8')
        # Now we are going to hash the password with md5
        # 1) Makes the object of md5
        # 2) then hexdigest() turns it into a md5 hash
        md5digest = hashlib.md5(encodePass.strip()).hexdigest()

        if md5digest == passwordHash:
            print(colored("Password found: " + password, 'green'))
            exit(0)

    print(colored("Password is not in list!", 'red'))

# TODO: Create sha1, sha512, sha256 password decrypter and as many others in the hashlib library

def main():
    passwordHash = input("[*] please enter the md5 hash: ")
    passwordFile = input("Please specify the password file: ")
    passFile = tryOpen(passwordFile)
    # run the function to get md5 hashed password
    getMd5Pass(passFile, passwordHash)


if __name__ == '__main__':
    main()


