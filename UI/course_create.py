import tkinter as tk
from tkinter import ttk
import requests
import json

#-------------------------------------------------------functions
def course_create_window(string):
    def go_to_url(url):
        def run_url():
            # course_text_ = requests.get(url).text
            # course_text_ = format_text(course_text_)
            # display_text_var.set(course_text_)
            # print(text_area.get(0))

            if(url=='new_page'):
                print('new_page')
            else:
                try:
                    f = open(display_text_var.get())
                    print(f.read())
                    
                except:
                    display_text_var.set('Invalid File!')
            # print(display_text_var.get())
        return run_url


    #--------------------------------------------------------window configs
    window = tk.Tk()
    window.geometry("1000x600")
    window.title('EDU HUB')
    window.configure(bg='#353535')

    #------------------------------------------------------dummy data



    #------------------------------------------------------creator variables
    creator_name_var = tk.StringVar(value="Sherica")
    creator_name_label = ttk.Label(window,textvariable=creator_name_var,font = 'Arial_Rounded_MT_Bold 54',padding=10,background="#94E16B")
    creator_name_label.grid(row = 0,column=0,sticky="w")

    #------------------------------------------------------display made courses
    material_urls = []
    material_buttons = []
    material_text_vars = []




    #------------------------------------------------------the directory input
    display_text_var = tk.StringVar(value=r"C:\Users\Parth\OneDrive\Desktop\hackathon\P-slayers\UI\data.txt")
    # text_area = tk.Entry(window,textvariable=display_text_var,font=('Tahoma', 12),width=50)
    # text_area.grid(row = 1,column=1,columnspan=2,sticky='e')


    #------------------------------------------------------the button to create a new course
    new_course_button = ttk.Button(window,text='New Course',style="my.TButton",command=go_to_url("new_page"))
    new_course_button.grid(row = 1,column=2,sticky='e')
    #pg buttons



    #------------------------------------------------------mail loop
    window.mainloop()