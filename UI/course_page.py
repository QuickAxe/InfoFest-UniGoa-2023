import tkinter as tk
from tkinter import ttk
import requests
import json


#reads the title from the file
def read():
    read = open(r"data.txt").read().split('\n')
    title = read[0]
    return title

def url_loader(url):
    # print(material_urls[course_material_table.item(course_material_table.selection()[0])['values']])
    # print(course_material_table.item(course_material_table.selection()[0])['values'])
    item = course_material_table.selection()[0]
    course = course_material_table.item(item)['values'][0]
    course=course.replace('_',' ')
    print(material_urls[course])
    
window = tk.Tk()
window.configure(bg='#353535')
window.title(read())
window.geometry("1000x600")


d = requests.get("http://127.0.0.1:8000/get")
s = json.loads(d.text)


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

stud_name_var = tk.StringVar(value = s[0]['id'])
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

# print(material_urls['Video 1'])







# button1_textvar=tk.StringVar()
# button2_textvar=tk.StringVar()
# button3_textvar=tk.StringVar()
# button4_textvar=tk.StringVar()
# button5_textvar=tk.StringVar()
# button6_textvar=tk.StringVar()


# button_style = ttk.Style()
# button_style.configure('my.TButton', font=('Tahoma', 12))

# button1 = ttk.Button(window,textvariable=button1_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
# button2 = ttk.Button(window,textvariable=button2_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
# button3 = ttk.Button(window,textvariable=button3_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
# button4 = ttk.Button(window,textvariable=button4_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
# button5 = ttk.Button(window,textvariable=button5_textvar,padding=10,style="my.TButton",command = go_to_url("url"))
# button6 = ttk.Button(window,textvariable=button6_textvar,padding=10,style="my.TButton",command = go_to_url("url"))



# if len(s)>0:
#     button1_textvar.set(f"{s[0]['lat']}\nProgress : {s[0]['longitude']}"+" "*(int(float(s[0]['longitude']))))
#     button1.grid(row = 2,column=1,sticky="w")
#     # ttk.Label(window,text = " "*100,background="green").grid(row = 2,column=2,sticky="e")
# if len(s)>1:
#     button2_textvar.set(f"{s[1]['lat']}\nProgress : {s[1]['longitude']}"+" "*(int(float(s[1]['longitude']))))
#     button2.grid(row = 3,column=1,sticky='w')
#     # ttk.Label(window,text = " "*100,background="green").grid(row = 3,column=2,sticky="e")
# if len(s)>2:
#     button3_textvar.set(f"{s[2]['lat']}\nProgress : {s[2]['longitude']}"+" "*(int(float(s[2]['longitude']))))
#     button3.grid(row = 4,column=1,sticky="w")
#     # ttk.Label(window,text = " "*100,background="green").grid(row = 4,column=2,sticky="e")
# if len(s)>3:
#     button4_textvar.set(f"{s[3]['lat']}\nProgress : {s[3]['longitude']}"+" "*(int(float(s[3]['longitude']))))
#     button4.grid(row = 5,column=1,sticky="w")
#     # ttk.Label(window,text = " "*100,background="green").grid(row = 5,column=2,sticky="e")
# if len(s)>4:
#     button5_textvar.set(f"{s[4]['lat']}\nProgress : {s[4]['longitude']}"+" "*(int(float(s[4]['longitude']))))
#     button5.grid(row = 6,column=1,sticky="w")
#     # ttk.Label(window,text = " "*100,background="green").grid(row = 6,column=2,sticky="e")
# if len(s)>5:
#     button6_textvar.set(f"{s[5]['lat']}\nProgress : {s[5]['longitude']}"+" "*(int(float(s[5]['longitude']))))
#     button6.grid(row = 7,column=1,sticky="w")
#     # ttk.Label(window,text = " "*100,background="green").grid(row = 7,column=2,sticky="e")

window.mainloop()
