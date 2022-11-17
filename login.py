import hashlib
import os
import sys
import tkinter
import tkinter.messagebox
from tkinter import *


# reset login screen
def Clear1():
    text1.delete(0, tkinter.END)
    text2.delete(0, tkinter.END)


# reset register screen
def Clear3(*args):
    text11.delete(0, tkinter.END)
    text12.delete(0, tkinter.END)


# exit
def Exit(*args):
    login_window.quit()
    login_window.destroy()
    main_window.quit()
    main_window.destroy()
    sign_up_window.quit()
    sign_up_window.destroy()
    sys.exit(0)


# center window
def Center(window_form):
    window_form.config(background="#00C0C0")
    width = window_form.winfo_screenwidth()  # get the width of the screen
    height = window_form.winfo_screenheight()  # get the height of the screen
    window_form.resizable(False, False)  # Fixed size
    window_form.geometry("%dx%d+%d+%d" % (width / 2.5, height / 2.0, width / 4.0, height / 4.0))


# switch to different window
def Form(st):
    if st == 1:
        main_window.withdraw()
        sign_up_window.withdraw()
        Center(login_window)
        login_window.deiconify()
    elif st == 2:
        login_window.withdraw()
        sign_up_window.withdraw()
        Center(main_window)
        main_window.deiconify()
    elif st == 3:
        login_window.withdraw()
        main_window.withdraw()
        Center(sign_up_window)
        sign_up_window.deiconify()


def returnLogin():  # return login window
    sign_out_text = tkinter.messagebox.askyesno("Warning!", "Are you sure you want to sign out?")
    if sign_out_text == YES:
        Form(1)


# Login function
def Login():
    username_input = text1.get().strip()
    password_input = text2.get().strip()
    list_of_account = os.listdir()

    if username_input in list_of_account:
        file1 = open(username_input, "r")
        check_password = file1.read().splitlines()

        if username_input in list_of_account and password_input in check_password:
            tkinter.messagebox.showinfo("Welcome!", "Login Successful!")
            label22["text"] = username_input
            Clear1()
            Form(2)

        else:
            tkinter.messagebox.showinfo("Warning!", "Invalid Password!")
            text2.delete(0, tkinter.END)
            text2.focus()
    else:
        tkinter.messagebox.showinfo("Warning!", "Invalid Username!")
        text2.delete(0, tkinter.END)
        text2.focus()


# sign up function
def Register():
    newUsername = text11.get().strip()
    newPassword = text12.get().strip()
    list_of_account = os.listdir()

    if newUsername == "":
        tkinter.messagebox.showinfo("Warning", "Invalid Username!")
        text11.focus()
    elif newUsername in list_of_account:
        tkinter.messagebox.showinfo("Warning", "Username Already Exists!")
        Clear3()
    elif newPassword == "":
        tkinter.messagebox.showinfo("Warning", "Invalid Password!")
        text12.focus()
    else:
        file = open(newUsername, "w")
        file.write(newUsername + "\n")
        file.write(newPassword)
        file.close()
        tkinter.messagebox.showinfo("Successful!", "Successfully Signed Up!")
        Clear3()
        Form(1)


# main
# create windows
login_window = tkinter.Tk()
main_window = tkinter.Tk()
sign_up_window = tkinter.Tk()

# window titles
login_window.title("Login Page")
main_window.title("RealWork")
sign_up_window.title("Register")

# center the window
Center(login_window)
Center(main_window)
Center(sign_up_window)

# hide windows
main_window.withdraw()
sign_up_window.withdraw()

# exit all windows
login_window.protocol("WM_DELETE_WINDOW", Exit)
main_window.protocol("WM_DELETE_WINDOW", Exit)
sign_up_window.protocol("WM_DELETE_WINDOW", Exit)

# log in window
software_title = Label(login_window, text="RealWork", bg="#C0C0C0", font=('Calibri', 60), bd=5, relief='flat',
                       justify="center", )
software_title.place(x=350, y=100)
team_name = Label(login_window, text="BRAND.INC", bg="#C0C0C0", font=('Calibri', 12), bd=5, relief='flat',
                  justify="center", )
team_name.place(x=600, y=200)
label1 = Label(login_window, text="Username", font=('Calibri', 18), bd=5, relief='flat', justify="center", )
label1.place(x=200, y=300)
label2 = Label(login_window, text="Password", font=('Calibri', 18), bd=5, relief='flat', justify="center")
label2.place(x=200, y=400)
text1 = tkinter.Entry(login_window, font=("Calibri", 17), relief="flat", width=28, borderwidth=5, justify="center")
text1.place(x=350, y=300)
text2 = tkinter.Entry(login_window, font=("Calibri", 17), show="*", relief="flat", width=28, borderwidth=5,
                      justify="center")
text2.place(x=350, y=400)
button1 = Button(login_window, text="Login", activebackground="#ffffff", relief='solid', font=('Calibri', 17),
                 padx=15, pady=5, command=Login, )
button1.place(x=250, y=500)
button3 = Button(login_window, text="Sign UP", activebackground="#ffffff", relief='solid', font=('Calibri', 17),
                 padx=15, pady=5, command=lambda: Form(3), )
button3.place(x=500, y=500)
button4 = Button(login_window, text="Exit", activebackground="#ffffff", relief='solid', font=('Calibri', 17),
                 padx=15, pady=5, command=Exit)
button4.place(x=750, y=500)

# register window
label11 = Label(sign_up_window, text="Username", font=('Calibri', 18), bd=5, relief='flat', justify="center")
label11.place(x=240, y=200)
label12 = Label(sign_up_window, text="Password", font=('Calibri', 18), bd=5, relief='flat', justify="center")
label12.place(x=240, y=300)
text11 = tkinter.Entry(sign_up_window, font=("Calibri", 17), relief="flat", borderwidth=5, width=28, justify="center")
text11.place(x=380, y=200)
text12 = tkinter.Entry(sign_up_window, font=("Calibri", 17), relief="flat", show="*", borderwidth=5, width=28,
                       justify="center")
text12.place(x=380, y=300)
button11 = Button(sign_up_window, text="Sign Up", activebackground="#ffffff", relief='solid', font=('Calibri', 17),
                  padx=15, pady=5, command=Register)
button11.place(x=250, y=450)

button13 = Button(sign_up_window, text="Cancel", activebackground="#ffffff", relief='solid', font=('Calibri', 17),
                  padx=15, pady=5, command=lambda: Form(1))
button13.place(x=650, y=450)

# main software
button21 = Button(main_window, text="Exit", activebackground="#ffffff", relief='solid', font=('Calibri', 17),
                  padx=15, pady=5, command=Exit)
button21.place(x=750, y=600)

button24 = Button(main_window, text="Sign Out", activebackground="#ffffff", relief='solid', font=("Calibri", 17),
                  padx=15, pady=5, command=returnLogin, )
button24.place(x=320, y=600)

label21 = tkinter.Label(main_window, text="Username:", font=("Calibri", 18), padx=10, pady=10, relief="flat",
                        justify="center", )
label21.place(x=130, y=60)
label22 = tkinter.Label(main_window, text=text1.get(), font=("Calibri", 18), padx=10, pady=10, relief="flat",
                        justify="left", )
label22.place(x=250, y=60)

sign_up_window.mainloop()
main_window.mainloop()
login_window.mainloop()

# reference to
# https://blog.csdn.net/qq_60423778/article/details/126931153
# https://www.simplifiedpython.net/python-gui-login/
