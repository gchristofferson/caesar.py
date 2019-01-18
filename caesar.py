# This program encrypts a message using Caesar's cipher
from cs50 import get_string
from cs50 import get_int
import sys

# only accept a single command-line argument (k)
if len(sys.argv) != 2:
    print('ERROR!! You must enter a key (number). Only one key is accepted')
    sys.exit(1)

# first, get the key from the user
k = int(sys.argv[1])

# prompt user for plaintext
p = get_string("plaintext: ")

# for each character in the plaintext string, if alphabetic, preserve case
# and shift plaintext character by key (k)
chars = list()
length = len(p)
for i in range(length):

    # if the character is not alphabetic, output the character unchanged
    if p[i].isalpha() == False:
        c = p[i]
        chars.insert(i, c)

    # if the character is uppercase, preserve case and add character to chars list
    elif p[i].isupper() == True:

        # convert to alphabetical index
        c = ord(p[i])
        ai = c - 65
        while True:
            if ai + k < 0:
                ai += 26
            if ai + k > 25:
                ai -= 26
            if ai + k >= 0 and ai + k <= 25:
                break

        # convert back to ascii index
        cai = (ai + k) % 26
        cai += 65

        # convert ascii to letter
        c = chr(cai)

        # append each letter into the chars list at the corresponding index
        chars.insert(i, c)

    # if the character is lowercase, preserve case and add character to chars list
    else:

        # convert to alphabetical index
        c = ord(p[i])
        ai = c - 97
        while True:
            if ai + k < 0:
                ai += 26
            if ai + k > 25:
                ai -= 26
            if ai + k >= 0 and ai + k <= 25:
                break

        # convert back to ascii index
        cai = (ai + k) % 26
        cai += 97

        # convert ascii to letter
        c = chr(cai)

        # append each letter to the chars list at the corresponding index
        chars.insert(i, c)

# print ciphertext
print("ciphertext: ", end='')
for i in range(length):
    print(chars[i], end='')
print()
sys.exit(0)