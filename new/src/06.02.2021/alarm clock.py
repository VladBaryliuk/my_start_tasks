from tkinter import *
import random
root = Tk()
root.geometry("185x300")
listbox = Listbox(root, width=30, height=10, justify=CENTER, selectmode = EXTENDED)
status = Label (root, text = "you have " + str(listbox.size()) + " alarms")
status.grid(column = 0, row = 1)
def generate_alarms():
    alarms = []
    start_ring = 1
    end_ring = 5
    for i in range(10):
        time_rining = random.randint(start_ring, end_ring)
        if time_rining < 10: 
            alarms.append('07: 0' + str(time_rining))
        else: 
            alarms.append('07:' + str(time_rining)) 
        start_ring += 5
        end_ring += 5
    listbox.insert(END, *alarms)
    status.config(text = "you have " + str(listbox.size()) + " alarms")
def alarm_delete():
    indexes = listbox.curselection()
    for i in indexes[::-1]:
        print (indexes)
        print (indexes[len(indexes)-1])
        listbox.delete(i)
        status.config(text = "you have " + str(listbox.size()) + " alarms")
lable = Label(root, text="alarm clock")
btn1 = Button(root, width=25, height=2, text="random alarm clocks", command = generate_alarms)
btn2 = Button(root, width=17, height=2, text="delete alarm clock", command = alarm_delete)
lable.grid(column=0, row=0)
listbox.grid(column=0, row=2)
btn1.grid(column=0, row=3)
btn2.grid(column=0, row=4)
