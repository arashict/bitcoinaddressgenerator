from tkinter import *
from bitcoin import *
import random
root=Tk()
root.geometry("700x200")
root.title('Bitcoin address Generator')

first_label = Label(root, text='Private key: ')
first_label.grid(row=0, column=0)
second_label = Label(root, text='Address: ')
second_label.grid(row=1, column=0)


privateKey = Entry(root, width=80, borderwidth=5)
privateKey.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
address_1 = Entry(root, width=80, borderwidth=5)
address_1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

def my_click(): 
    pv_key = random.randrange(2**255, 2**256)
    address = privtoaddr(pv_key)
    privateKey.delete(0, END) 
    privateKey.insert(0, pv_key)
    address_1.delete(0, END)
    address_1.insert(0, address)


my_button = Button(root, command= my_click, text='Generate', bg='#9bf2aa', fg='#000000')
my_button.grid(row=0, column=5, columnspan=1, padx=10, pady=10)


root.mainloop()

