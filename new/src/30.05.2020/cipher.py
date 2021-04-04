alfabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_encrypt(plaintext, key):
    chiphertext = ""
    for letter in (plaintext):
        new_letter = (alfabet.find(letter.lower()) + key % len(alfabet))
        chiphertext = chiphertext + alfabet[new_letter]
    return chiphertext


print(caesar_encrypt(str(input("input text to cipher")), 3))