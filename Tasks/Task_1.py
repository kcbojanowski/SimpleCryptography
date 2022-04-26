"""
Zadanie nr 1
Napisz funkcje służącą do odszyfrowywania szyfrogramu szyfru Vigenere. Spróbuj nie używać
Internetu.
"""


def generateKey(mess, keyword):
    key = list(keyword)
    mess = mess.replace(" ", "")
    if len(mess) == len(key):
        return key
    else:
        for i in range(len(mess) - len(key)):
            key.append(key[i % len(key)])
    generated_key = "".join(key).upper()
    return generated_key


"""
[PARAMETRY]
 message - szyfrogram Vigenere
 keyword - klucz 
 key - klucz wygenerowany przez funkcje generateKey()
 (powielony aby otrzymać tą samą długość co szyfrogram)
 [PODPOWIEDŹ] chr(65) = "A", chr(66) = "B" itp.
 """


def Decrypt_Vigenere(message, keyword):
    key = generateKey(message, keyword)
    # ENTER YOUR CODE HERE
    pass
