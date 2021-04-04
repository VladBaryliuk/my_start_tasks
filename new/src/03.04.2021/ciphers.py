alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for i in plaintext:
        index = alfabet.index(i)
        new_index = (index + key) % len(alfabet)
        new_letter = alfabet[new_index]
        ciphertext += new_letter
    return ciphertext
print(caesar_encrypt("фмд", 4))
def decaesar_encrypt(plaintext, key):
    deciphertext = ""
    for i in plaintext:
        if i == " ":
            deciphertext += " "
            continue
        index = alfabet.find(i)
        new_index = (index + key) % len(alfabet)
        new_letter = alfabet[new_index]
        deciphertext += new_letter
    return deciphertext
print(decaesar_encrypt("кгтлфюегмхзфя рг тусдрсз кгрвхлз", -3))
def breaking_caesar_encrypt(plaintext,):
    broken_ciphertext = ""
    for j in range(len(alfabet)):
        key = j
        print(decaesar_encrypt(plaintext, key))
breaking_caesar_encrypt("ч жбъщиуоюя ёхе цищъз нюйё хзцхн")