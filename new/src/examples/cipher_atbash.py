
def chipher(plaintext):
    alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    chiphertext = ""
    for letter in plaintext:
        encrypted_letter = (len(alfabet) - 1 - alfabet.find(letter))
        chiphertext = chiphertext + alfabet[encrypted_letter]
    return chiphertext
print(chipher("айтигенио"))