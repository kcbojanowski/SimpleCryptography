"""
Task no. 1
Write a code that will encrypt plaintext in Vigenere Cipher. Try to avoid using
the Internet. You can use given function to generate key.
"""


def generateKey(mess, keyword):
    key = list(keyword)
    mess = mess.replace(" ", "")
    if len(mess) == len(key):
        return key
    else:
        for i in range(len(mess) - len(key)):
            key.append(key[i % len(key)])
    key = "".join(key).upper()
    return key


# message is a plain text to encrypt
# keyword is a key multiplied to match a length of a message
def Encrypt_Vigenere(message, key):
    # ENTER YOUR CODE HERE
    pass
