alfabet ="abcdefghijklmnopqrstuvwxyz"
reversed_alfabet = alfabet[::-1]
string_to_cipher = input()
def atbash_cipher():
    new_string = ""
    for i in string_to_cipher:
        index = alfabet.find(i)
        new_letter = reversed_alfabet[index]
        new_string += new_letter
    print(new_string)