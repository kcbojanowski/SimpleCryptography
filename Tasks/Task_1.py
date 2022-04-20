"""
Task no. 1
Write a code that will encrypt plaintext in Vigenere Cipher. Try to avoid using
the Internet. You can use given function to generate key.
"""
def generateKey(string, key):
    key = list(key)
    string = string.replace(" ", "")

    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])

    key = "".join(key).upper()
    return key

def Encrypt_Vigenere(message, keyword):
    pass
