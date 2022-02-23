from tkinter import *
import sys
from pyparsing import col

# pres
root = Tk()
root.title("Website Blocker")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "enter your domain")

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# methods


def button_block():
    domain = e.get()
    with open(hosts_path, 'r+') as file:
        content = file.read()
        if domain in content:
            pass
        else:
            file.write(redirect + " " + domain + "\n")


def button_unblock():
    domain = e.get()
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in domain):
                file.write(line)
        file.truncate()


# buttons
button_block1 = Button(root, text="press to block",
                       padx=35, pady=15, command=button_block, width=35)

button_unblock1 = Button(root, text="press to unblock",
                         padx=35, pady=15, command=button_unblock, width=35)

# grids
button_block1.grid(row=10, column=0)
button_unblock1.grid(row=20, column=0)

# mainloop
root.mainloop()
