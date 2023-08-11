import tkinter as tk
from tkinter import ttk
import requests
import json

def course_page_window(string):
    def url_loader(url):
        # print(material_urls[course_material_table.item(course_material_table.selection()[0])['values']])
        # print(course_material_table.item(course_material_table.selection()[0])['values'])
        item = course_material_table.selection()[0]
        course = course_material_table.item(item)['values'][0]
        course=course.replace('_',' ')
        print(material_urls[course])
        
    window = tk.Tk()
    # window.title(read())
    window.configure(bg='#353535')
    window.title('EDU HUB')
    window.geometry("1000x600")


    # d = requests.get("http://127.0.0.1:8000/get")
    # s = json.loads(d.text)


    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=1)
    window.columnconfigure(3,weight=1)
    window.columnconfigure(4,weight=1)

    window.rowconfigure(0,weight=2)
    window.rowconfigure(1,weight=2)
    window.rowconfigure(2,weight=1)
    window.rowconfigure(3,weight=1)
    window.rowconfigure(4,weight=1)
    window.rowconfigure(5,weight=1)
    window.rowconfigure(6,weight=1)
    window.rowconfigure(7,weight=1)

    stud_name_var = tk.StringVar(value = 'parth')
    student_name = ttk.Label(window,textvariable=stud_name_var,background="#94E16B",font = 'Arial_Rounded_MT_Bold 54',padding=10)
    student_name.grid(row = 0,column=1,columnspan=1,sticky="w")

    course_name_var = tk.StringVar(value = 'Physics')
    course_name_label = ttk.Label(window,textvariable=course_name_var,background="#94E16B",font = 'Arial_Rounded_MT_Bold 42',padding=10)
    course_name_label.grid(row = 0,column=4,columnspan=1,sticky="w")

    course_material_list=["Video 1","Video 2","Video 3","Video 4","Video 5","Video 6","Video 7","Video 8","Video 9","Video 10","Video 11","Video 12","Video 13","Video 14","Video 15","Video 16","Video 17","Video 18","Video 19","Video 20"]
    course_material_table = ttk.Treeview(window,columns=("Videos "),show='headings',selectmode='browse')
    for i in range(len(course_material_list)):
        # course_material_table.insert(parent='',index='end',values=(course_material_list[i].replace(' ','⠀')))
        course_material_table.insert(parent='',index='end',values=(course_material_list[i].replace(' ','_')))
    course_material_table.grid(row=2,column=0,columnspan=1,sticky="w",ipady=50)
    material_urls = {'Video 1': 'URL 1', 'Video 2': 'URL 2', 'Video 3': 'URL 3', 'Video 4': 'URL 4', 'Video 5': 'URL 5', 'Video 6': 'URL 6', 'Video 7': 'URL 7', 'Video 8': 'URL 8', 'Video 9': 'URL 9', 'Video 10': 'URL 10', 'Video 11': 'URL 11', 'Video 12': 'URL 12', 'Video 13': 'URL 13', 'Video 14': 'URL 14', 'Video 15': 'URL 15', 'Video 16': 'URL 16', 'Video 17': 'URL 17', 'Video 18': 'URL 18', 'Video 19': 'URL 19', 'Video 20': 'URL 20'}  

    course_material_table.bind('<<TreeviewSelect>>',url_loader)

    window.mainloop()
