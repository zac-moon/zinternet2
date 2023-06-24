import tkinter as tk

root = tk.Tk()
root.title("ZBank Login")
root.geometry("800x600")

homeLabel = tk.Label(root,text="ZBANK",font=('Arial',120))
usercodeLabel = tk.Label(root, text="UserCode:",font=('Arial',20))
usercodeEntry = tk.Entry(root)
accountNumberLabel = tk.Label(root, text="Account Number:",font=('Arial',20))
accountNumberEntry = tk.Entry(root)


def login():
    usercode
    print(f"Login- {}")


loginBtn = tk.Button(root, text="Login",command=login)

homeLabel.pack()
usercodeLabel.pack()
usercodeEntry.pack()
accountNumberLabel.pack()
accountNumberEntry.pack()
loginBtn.pack()

root.mainloop()