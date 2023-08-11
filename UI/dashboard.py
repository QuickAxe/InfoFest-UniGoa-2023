import tkinter as tk
from tkinter import ttk
import requests
import json


def student_dachboard_window(string):

    def go_to_url(url):
        pass
    window = tk.Tk()
    window.geometry('1000x600')
    window.configure(bg='#353535')
    # frame = ttk.Frame(window)
    # window.title(read())
    # window.geometry("1000x600")


    d = requests.get("http://127.0.0.1:8000/getStudentCourse/?studentID=1").text
    s=json.loads(d)
    # s = [
    #     {
    #         'lat': 'Physics',
    #         'longitude':'37',
    #         'url':'URL'
    #     },
    #     {
    #         'lat': 'Physics',
    #         'longitude':'37',
    #         'url':'URL'
    #     },
    #     {
    #         'lat': 'Physics',
    #         'longitude':'37',
    #         'url':'URL'
    #     }
    # ]


    button1_textvar=tk.StringVar()
    button2_textvar=tk.StringVar()
    button3_textvar=tk.StringVar()
    button4_textvar=tk.StringVar()
    button5_textvar=tk.StringVar()
    button6_textvar=tk.StringVar()

    student_name_var = tk.StringVar(value="Hello")
    student_name_label = ttk.Label(window,textvariable=student_name_var,background="#94E16B",font = 'Arial_Rounded_MT_Bold 54')
    student_name_label.place(x = 10,y = 10)

    button_style = ttk.Style()
    button_style.configure('my.TButton', font=('Tahoma', 12))

    button1 = ttk.Button(window,textvariable=button1_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
    button2 = ttk.Button(window,textvariable=button2_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
    button3 = ttk.Button(window,textvariable=button3_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
    button4 = ttk.Button(window,textvariable=button4_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
    button5 = ttk.Button(window,textvariable=button5_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
    button6 = ttk.Button(window,textvariable=button6_textvar,padding=10,style="my.TButton",command = go_to_url("url"))



    if len(s)>0:
        button1_textvar.set(f"{s[0]['lat']}\nProgress : {s[0]['longitude']}"+" "*(int(float(s[0]['longitude']))))
        # button1.grid(row = 2,column=1,sticky="w")
        button1.place(x = 100,y = 100)
    if len(s)>1:
        button2_textvar.set(f"{s[1]['lat']}\nProgress : {s[1]['longitude']}"+" "*(int(float(s[1]['longitude']))))
        # button2.grid(row = 3,column=1,sticky='w')
        button2.place(x = 100,y = 150)
    if len(s)>2:
        button3_textvar.set(f"{s[2]['lat']}\nProgress : {s[2]['longitude']}"+" "*(int(float(s[2]['longitude']))))
        # button3.grid(row = 4,column=1,sticky="w")
        button3.place(x = 100,y = 200)
    if len(s)>3:
        button4_textvar.set(f"{s[3]['lat']}\nProgress : {s[3]['longitude']}"+" "*(int(float(s[3]['longitude']))))
        # button4.grid(row = 5,column=1,sticky="w")
        button4.place(x = 100,y = 250)
    if len(s)>4:
        button5_textvar.set(f"{s[4]['lat']}\nProgress : {s[4]['longitude']}"+" "*(int(float(s[4]['longitude']))))
        # button5.grid(row = 6,column=1,sticky="w")
        button5.place(x = 100,y = 300)
    if len(s)>5:
        button6_textvar.set(f"{s[5]['lat']}\nProgress : {s[5]['longitude']}"+" "*(int(float(s[5]['longitude']))))
        # button6.grid(row = 7,column=1,sticky="w")
        button6.place(x = 100,y = 350)

    # frame.pack()
    window.mainloop()
string = []
student_dachboard_window(string)
print(string)