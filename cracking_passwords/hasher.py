#!/usr/bin/python

# we will be hashing different types of strings

# This library helps us hash with a few lines of code
import hashlib

hashValue = input("Enter a string to hash: ")

# create a md5 hash object
hashobj1 = hashlib.md5()
# This will add the string to the md5 and then
# it will hash it with the md5 method
hashobj1.update(hashValue.encode())
# get the hashed string
print(hashobj1.hexdigest())

hashobj2 = hashlib.sha1()
hashobj2.update(hashValue.encode())
print(hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
hashobj3.update(hashValue.encode())
print(hashobj3.hexdigest())

hashobj4 = hashlib.sha256()
hashobj4.update(hashValue.encode())
print(hashobj4.hexdigest())

hashobj5 = hashlib.sha512()
hashobj5.update(hashValue.encode())
print(hashobj5.hexdigest())
