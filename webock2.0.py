from tkinter import *
from tkinter import messagebox as msg
import sys


# pres
root = Tk()
root.title("Website Blocker")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "insert domain name")

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
writer_path = "C:\\Users\\resul\\Desktop\\x\\websiteblocker\\mitschreiber.txt"
# checkboxes
global comvar
global orgvar
global devar
comvar = IntVar()  # 1 checked, 0 not checked
orgvar = IntVar()
devar = IntVar()
checkerCOM = Checkbutton(root, text=".com", variable=comvar)
checkerORG = Checkbutton(root, text=".org", variable=orgvar)
checkerDE = Checkbutton(root, text=".de", variable=devar)
checkerCOM.grid()
checkerORG.grid()
checkerDE.grid()
# globals
global mem
mem = []

# methods


def button_block():
    global label
    values = comvar.get() + orgvar.get() + devar.get()
    domain = e.get()
    with open(hosts_path, 'r+') as file:
        content = file.read()
        if domain in content:
            label = Label(root, text="already blocked")
            pass
        else:
            if values > 0:
                if comvar.get() == 1:
                    file.write(redirect + " www." + domain + ".com" + "\n")
                    file.write(redirect + " " + domain + ".com" + "\n")
                    mem.append(domain + ".com")
                if orgvar.get() == 1:
                    file.write(redirect + " www." + domain + ".org" + "\n")
                    file.write(redirect + " " + domain + ".org" + "\n")
                    mem.append(domain + ".org")
                if devar.get() == 1:
                    file.write(redirect + " www." + domain + ".de" + "\n")
                    file.write(redirect + " " + domain + ".de" + "\n")
                    mem.append(domain + ".de")
                label = Label(root, text=f"you have blocked {domain}")
            elif values == 0:
                label = Label(root, text="check a box")
        label.grid()
        button_block1['state'] = DISABLED
        button_unblock1['state'] = DISABLED
        button_clear1['state'] = NORMAL


def button_unblock():
    global label
    domain = e.get()
    # mem

    for i in mem:
        if domain + ".com" == i:
            mem.remove(i)
        if domain == ".":
            mem.clear()
        if domain + ".de" == i:
            mem.remove(i)
        if domain + ".org" == i:
            mem.remove(i)
        else:
            pass
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in domain):
                file.write(line)
        file.truncate()

        label = Label(root, text=f"you have unblocked {domain}")
        label.grid()
        button_block1['state'] = DISABLED
        button_unblock1['state'] = DISABLED
        button_clear1['state'] = NORMAL


def button_clear():
    label.destroy()
    button_block1['state'] = NORMAL
    button_unblock1['state'] = NORMAL
    button_clear1['state'] = DISABLED


def show_blocked():
    msg.showinfo("info of blocked", mem)


# buttons
button_block1 = Button(root, text="press to block",
                       command=button_block, width=35)

button_unblock1 = Button(root, text="press to unblock",
                         command=button_unblock, width=35)

button_clear1 = Button(root, text="clear",
                       command=button_clear, width=35, state=DISABLED)

button_showinfo = Button(root, text="show blocked domains",
                         command=show_blocked, width=35)


# grids
button_block1.grid()
button_unblock1.grid()
button_clear1.grid()
button_showinfo.grid()

# mainloop
root.mainloop()
