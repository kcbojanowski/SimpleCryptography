"""
Task no.2
In function key_pair() write a code that will allow you to save pair of keys:
public and private it format of `public_key_[Year][Month][Hour][Minute][Second].pem`.
To do that use library Cryptodome.
"""

# IMPORTS
from Cryptodome.PublicKey import RSA
import binascii
import datetime


# FUNCTION TO WORK WITH
def key_pair():
    # here is a code used for getting current time
    now = datetime.datetime.now() # now - current time
    date = now.strftime("%y_%m_%d_%H%M%S") # date - string showing current time
