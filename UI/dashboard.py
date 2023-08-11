import tkinter as tk
from tkinter import ttk
import requests
import json


def student_dachboard_window(string):
    def go_to_url(value):
        def run_url():
            string[0]="http://127.0.0.1:8000/getCourse/?courseVal=5"
            window.destroy()
        return run_url
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

    button1 = ttk.Button(window,textvariable=button1_textvar,padding=1,style="my.TButton",command = go_to_url(0))
    button2 = ttk.Button(window,textvariable=button2_textvar,padding=1,style="my.TButton",command = go_to_url(1))
    button3 = ttk.Button(window,textvariable=button3_textvar,padding=1,style="my.TButton",command = go_to_url(2))
    button4 = ttk.Button(window,textvariable=button4_textvar,padding=1,style="my.TButton",command = go_to_url(3))
    button5 = ttk.Button(window,textvariable=button5_textvar,padding=1,style="my.TButton",command = go_to_url(4))
    button6 = ttk.Button(window,textvariable=button6_textvar,padding=1,style="my.TButton",command = go_to_url(5))


    if len(s)>0:
        button1_textvar.set(f"{s[0]['name']}\nProgress : {s[0]['progress']}\nTeacher : {s[0]['Teacher']}"+" "*(int(float(s[0]['progress']))))
        # button1.config['fg']=return_colour(s[0]['progress'])
        # button1.grid(row = 2,column=1,sticky="w")
        button1.place(x = 100,y = 100+70)
    if len(s)>1:
        button2_textvar.set(f"{s[1]['name']}\nProgress : {s[1]['progress']}\nTeacher : {s[1]['Teacher']}"+" "*(int(float(s[1]['progress']))))
        # button2.grid(row = 3,column=1,sticky='w')
        button2.place(x = 100,y = 100+140)
    if len(s)>2:
        button3_textvar.set(f"{s[2]['name']}\nProgress : {s[2]['progress']}\nTeacher : {s[2]['Teacher']}"+" "*(int(float(s[2]['progress']))))
        # button3.grid(row = 4,column=1,sticky="w")
        button3.place(x = 100,y = 100+210)
    if len(s)>3:
        button4_textvar.set(f"{s[3]['name']}\nProgress : {s[3]['progress']}\nTeacher : {s[3]['Teacher']}"+" "*(int(float(s[3]['progress']))))
        # button4.grid(row = 5,column=1,sticky="w")
        button4.place(x = 100,y = 100+280)
    if len(s)>4:
        button5_textvar.set(f"{s[4]['name']}\nProgress : {s[4]['progress']}\nTeacher : {s[4]['Teacher']}"+" "*(int(float(s[4]['progress']))))
        # button5.grid(row = 6,column=1,sticky="w")
        button5.place(x = 100,y = 100+350)
    if len(s)>5:
        button6_textvar.set(f"{s[5]['name']}\nProgress : {s[5]['progress']}\nTeacher : {s[5]['Teacher']}"+" "*(int(float(s[5]['progress']))))
        # button6.grid(row = 7,column=1,sticky="w")
        button6.place(x = 100,y = 100+420)

    # frame.pack()
    window.mainloop()
# string = ['']
# student_dachboard_window(string)
# print(string)