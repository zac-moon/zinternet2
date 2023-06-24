import tkinter as tk

root = tk.Tk()
root.title("ZBank Login")
root.geometry("800x600")

homeLabel = tk.Label(root,text="ZBANK",font=('Arial',120))
usercodeLabel = tk.Label(root, text="UserCode:",font=('Arial',20))
usercodeEntry = tk.Entry(root)
accountNumberLabel = tk.Label(root, text="Account Number:",font=('Arial',20))
accountNumberEntry = tk.Entry(root)

def bankMenu(fullName):
    print("Bank Menu")
    client = tk.Toplevel()
    client.title("ZBANK- "+fullName)

def login():
    usercodeTry =  usercodeEntry.get()
    accountNumberTry = accountNumberEntry.get()
    print(f"Login- {usercodeTry} - {accountNumberTry}")
    if usercodeTry == "zacmoon" and accountNumberTry =="436118":
        bankMenu("Zac Moon")


loginBtn = tk.Button(root, text="Login",command=login)

homeLabel.pack()
usercodeLabel.pack()
usercodeEntry.pack()
accountNumberLabel.pack()
accountNumberEntry.pack()
loginBtn.pack()

root.mainloop()