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
        course = course.split('_')
        text = ['']
        i=0
        for word in course:
            if len(text[i]) + len(word) > 80:
                text.append(word)
                i+=1
            else:
                text[i]= text[i]+' '+word
        text = '\n'.join(text)
        print(text)

        ttk.Label(window,text =text,font=('Arial_Rounded_MT_Bold',15)).place(x = 250,y = 250)
        
    window = tk.Tk()
    # window.title(read())
    window.configure(bg='#353535')
    window.title('EDU HUB')
    window.geometry("1000x600")


    d = requests.get(string[0])
    s = json.loads(d.text)
    other = s[0]
    s = s[1:]
    # print(other)

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

    stud_name_var = tk.StringVar(value = f"Teacher : {other['Teacher']}"+f" | Subject : {other['name']}")
    student_name = ttk.Label(window,textvariable=stud_name_var,background="#94E16B",font = 'Arial_Rounded_MT_Bold 25',padding=10)
    student_name.place(x = 20,y = 20)

    # course_name_var = tk.StringVar(value = f"Subject : {other['name']}")
    # course_name_label = ttk.Label(window,textvariable=course_name_var,background="#94E16B",font = 'Arial_Rounded_MT_Bold 25',padding=10)
    # course_name_label.place(x = 500,y = 20)


    course_material_list=[]
    for i in s:
        course_material_list.append(i['textContent'])
    # print("course_material_list",course_material_list)
    course_material_table = ttk.Treeview(window,columns=("Videos"),show='headings',selectmode='browse')
    for i in range(len(course_material_list)):
        course_material_table.insert(parent='',index='end',values=(course_material_list[i].replace(' ','_')))
    course_material_table.grid(row=2,column=0,columnspan=1,sticky="w",ipady=50)
    material_urls = {} 
    for i in s:
        material_urls.update({i['textContent']:i['videoURL']})
    # print("material_urls",material_urls)

    course_material_table.bind('<<TreeviewSelect>>',url_loader)
    def do_quiz():
        window.destroy()
    ttk.Button(window,text = "Quiz",command=do_quiz).place(x = 800,y = 500)

    window.mainloop()

