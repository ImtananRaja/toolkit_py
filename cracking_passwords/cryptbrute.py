#!/usr/bin/python

#admin & RocketMan - DL
#RocketMan - GH

# to syntax check run
# python -m py_compile <filename>

import crypt
from termcolor import colored
import hashlib

count = 0

def crackpass(cryptWord, dictFile):
    global count
    #get the salt which is the first 2 letters
    salt = cryptWord[0:2]
    with open(dictFile, 'r') as dictionaryWord:
        for word in dictionaryWord.readlines():
            # set the crypt for the dictionary word for comparison later
            cryptDictWord = crypt.crypt(word.strip('\n'), salt=salt)
            # check if they cryptedWord and crypted dictionary word are the same
            if cryptDictWord == cryptWord:
                print(colored("Found the crypted word: " + word, 'green'))
                count = 1


def main():
    # cryptpass.txt
    passwordFile = input("Please type the path to the file: ")
    dictFile = input("Please type the path to the dictionary file: ")
    with open(passwordFile, 'r') as lines:
        # read each line
        for line in lines.readlines():
            # split on colon
            if ":" in line:
                # general convention user then password
                user = line.split(':')[0]
                cryptword = line.split(':')[1].strip(' ').strip('\n')
                print(colored("Cracking password for: " + user, 'blue'))
                crackpass(cryptword, dictFile)
        if count != 1:
            print(colored('No crypted password found in dictionary!', 'red'))

if __name__ == '__main__':
    main()

