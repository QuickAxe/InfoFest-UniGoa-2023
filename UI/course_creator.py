import tkinter as tk
from tkinter import ttk
import requests
import json
from tkinter import scrolledtext

#-------------------------------------------------------functions
def format_text(ct:str):
    i = 0
    text = ['']
    ct = ct.split(' ')
    for word in ct:
        if((len(text[i]) + len(word) )< 120):
            text[i]= text[i] + ' ' + word
        else:
            text.append(word)
            i+=1
    text = '\n'.join(text[:10])
    return text

def go_to_url(url):
    def run_url():
        course_text_ = requests.get(url).text
        course_text_ = format_text(course_text_)
        text_var.set(course_text_)
        
    return run_url


#--------------------------------------------------------window configs
window = tk.Tk()
window.geometry("1000x600")
window.title('EDU HUB')
window.configure(bg='#353535')
rows = 5
cols = 5
for i in range(rows):
    window.rowconfigure(i,weight=1)
for i in range(cols):
    window.columnconfigure(i,weight=1)

#------------------------------------------------------dummy data
data = [
    {
        "name":"Python",
        "url" :"https://filesamples.com/samples/document/txt/sample3.txt"
    },
    {
        "name":"DBMS",
        "url" :"http:/URL"
    },
    {
        "name":"FLAT",
        "url" :"http:/URL"
    },
    {
        "name":"MADF",
        "url" :"http:/URL"
    },
    
]


#------------------------------------------------------creator variables
creator_name_var = tk.StringVar(value="Sherica")
creator_name_label = ttk.Label(window,textvariable=creator_name_var,font = 'Arial_Rounded_MT_Bold 54',padding=10,background="#94E16B")
creator_name_label.grid(row = 0,column=0,sticky="w")

#------------------------------------------------------display made courses
course_urls = []
course_buttons = []
course_text_vars = []

button_style = ttk.Style()
button_style.configure('my.TButton', font=('Tahoma', 12))

for i in range(len(data)):
    course_urls.append(data[i]["url"])

    text_var = tk.StringVar(value=data[i]["name"])
    button = ttk.Button(window,textvariable=text_var,style="my.TButton",command=go_to_url(course_urls[i]))

    course_text_vars.append(text_var)
    course_buttons.append(button)


for i in range(len(data)):
    button = course_buttons[i]
    button.grid(row = 1+i,column=1,sticky="w")



#------------------------------------------------------the text display
# text_var = tk.StringVar()
# display_text = ttk.Entry(window,background="#616161",textvariable=text_var)
# display_text.grid(row = 1,column=2,rowspan=5,columnspan=2)
# text_area = scrolledtext.ScrolledText(window,width = 100,height = 200,font = ("Times New Roman",15))
# text_area.grid(row = 2,column=2)


#pg buttons



#------------------------------------------------------mail loop
window.mainloop()