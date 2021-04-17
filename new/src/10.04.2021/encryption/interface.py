from tkinter import *
root = Tk()
root.geometry("300x400")

alfabet = "abcdefghijklmnopqrstuvwxyz"
reversed_alfabet = alfabet[::-1]

choice = StringVar()
choice.set("ceasar's cipher")

cipher_name = Label(text="cipher", width=25)
cipher_name.place(x=90, y=285)
cipher_message = Label(text="", width=15)
cipher_message.place(x=80, y=305)
keybox = Entry(root, width=7)
keybox.place(x=215, y=230)

def atbash_cipher(plaintext):
    new_string = ""
    for i in plaintext:
        index = alfabet.find(i)
        new_letter = reversed_alfabet[index]
        new_string += new_letter
    return new_string

def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for i in plaintext:
        index = alfabet.find(i)
        new_index = (index + key) % len(alfabet)
        new_letter = alfabet[new_index]
        ciphertext += new_letter
    return ciphertext

def change_cipher():
    current_cipher = choice.get()
    if current_cipher == "ceasar's cipher":
        cipher_name.config(text="encecryped by ceasar's cipher")
        keybox.config(state="normal")
    if current_cipher == "atbash cipher":
        cipher_name.config(text="encecryped by atbash cipher")
        keybox.config(state="disabled")

def encrypt():
    current_cipher = choice.get()
    if current_cipher == "ceasar's cipher":
        plaintext = plaintextbox.get()
        key = keybox.get()
        key = int(key)
        cipher_text = caesar_encrypt(plaintext, key)
        cipher_message.config(text=cipher_text)
    elif current_cipher == "atbash cipher":
        plaintext = plaintextbox.get()
        cipher_text = atbash_cipher(plaintext)
        cipher_message.config(text=cipher_text)

change_cipher()
l1 = Label(text="choice of cipher", width=16)
l1.place(x=1, y=15)
radio_ceasar = Radiobutton(text="ceasar's cipher", variable=choice, value="ceasar's cipher", command=change_cipher)
radio_ceasar.place(x=100, y=30)
radio_atbash = Radiobutton(text="atbash cipher", variable=choice, value="atbash cipher", command=change_cipher)
radio_atbash.place(x=100, y=50)

l2 = Label(text="data", width=6)
l2.place(x=1, y=180)
plaintextbox_Label = Label(text="enter the text", width=10)
plaintextbox_Label.place(x=45, y=210)
keybox_Label = Label(text="enter the key", width=10)
keybox_Label.place(x=200, y=210)
plaintextbox = Entry(root, width=25)
plaintextbox.place(x=45, y=230)

l4 = Label(text="encrypted message", width=15)
l4.place(x=1, y=270)
cipher_button = Button(text="encrypt", width=10, command=encrypt)
cipher_button.place(x=100, y=350)

root.mainloop()
