import tkinter as tk
from tkinter import ttk
import requests
import json

def login_signin_window(string):

    window = tk.Tk()
    window.title('w2')
    window.geometry('1000x600')
    #functions
    def check_email_password(email,password):
        def check():
            print(f"email = {email.get()}")
            print(f"password = {password.get()}")
            if(email.get() == 'parth' and password.get() == '123'):
                # string.set('correct')
                string[0] = 'correct'
            else:
                # string.set('incorrect')
                string[0]  = 'incorrect'
            window.destroy()
        return check

    #frame variable
    # frame = ttk.Frame(window)


    ttk.Label(window,text='Email : ',font = ('Calibri',20)).place(x = 200,y = 300)
    ttk.Label(window,text='Password : ',font = ('Calibri',20)).place(x = 200,y = 350)

    # email_label = ttk.Label(window,text='Email : ',font = ('Calibri',20)).pack()
    # password_label = ttk.Label(window,text='Password : ',font = ('Calibri',20)).pack()
    
    # email_label.place(x = 200,y = 300)
    # password_label.place(x = 200,y = 350)

    button_style = ttk.Style()
    button_style.configure('my.TButton', font=('Tahoma', 12))

    email_text_var = tk.StringVar(value='parth')
    password_text_var = tk.StringVar(value='123')
    
    email_entry = ttk.Entry(window,width=50,textvariable=email_text_var,font=('Tahoma', 12))
    password_entry = ttk.Entry(window,width=50,textvariable=password_text_var,font=('Tahoma', 12))


    email_entry.place(x=400,y=300)
    password_entry.place(x=400,y=350)
    
    ttk.Button(window,text = 'Login / Sign_in',command=check_email_password(email_text_var,password_text_var)).place(x = 300,y = 400)

    
    # frame.pack()
    window.mainloop()
