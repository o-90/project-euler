# -*- coding: utf-8 -*-

import string


# 59)
# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.  A
# modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key. The
# advantage with the XOR function is that using the same encryption key on
# the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
# then 107 XOR 42 = 65.  For unbreakable encryption, the key is the same
# length as the plain text message, and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in
# different locations, and without both "halves", it is impossible to decrypt
# the message.  Unfortunately, this method is impractical for most users, so
# the modified method is to use a password as a key. If the password is
# shorter than the message, which is likely, the key is repeated cyclically
# throughout the message. The balance for this method is using a sufficiently
# long password key for security, but short enough to be memorable.  Your task
# has been made easy, as the encryption key consists of three lower case
# characters. Using cipher.txt (right click and 'Save Link/Target As...'), a
# file containing the encrypted ASCII codes, and the knowledge that the plain
# text must contain common English words, decrypt the message and find the
# sum of the ASCII values in the original text.

# ----------------------------------------------------------------------------
# NOTE:  We can assume that since this a paragraph of english words and
# sentences, that the last character is a period (.).  There are 1201
# ASCII characters in the text, so the last encryption character will
# correspond to the 1st character (because 1201 is congruent to 1 mod 3).
# Therefore, the text begins with a '(' and every 3rd element can be
# decrypted with the key 103.
# ----------------------------------------------------------------------------



def logical_xor(a, b):
    """
    implement XOR for two integers
    """
    a = bin(a)[2:]
    b = bin(b)[2:]
    diff = abs(len(a) - len(b))

    if len(a) < len(b):
        a = diff * '0' + a
    if len(b) < len(a):
        b = diff * '0' + b

    return int(''.join(str(int(x)^int(y)) for x, y in zip(a, b)), 2)


lcase = string.ascii_lowercase
ascii_map = {ord(x): x for x in list(lcase)}


f = open("../../data/p059_cipher.txt", 'r')
codes = f.read().strip().split(',')

keys = ascii_map.keys()
phrase = []

for k, x in enumerate(codes):
    if k%3 == 0:
        phrase.append(logical_xor(int(x), 103))
    elif k%3 == 1:
        phrase.append(logical_xor(int(x), 111))
    else:
        phrase.append(logical_xor(int(x), 100))

ans = sum(phrase)
print ans
