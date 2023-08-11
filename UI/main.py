import tkinter as tk
from tkinter import ttk 
import requests
import json

# garbage = tk.Tk()

def show_login_signin():
    import login_sign_in
    login_sign_in.login_signin_window(string)

def show_student_dashboard():
    import dashboard
    dashboard.student_dachboard_window(string)

def show_course_page():
    import course_page
    course_page.course_page_window(string)

def show_quiz_window():
    import quiz
    quiz.quiz_window(string)

#window
# window = tk.Tk()
# window.title('w1')
# window.geometry('1000x600')
global string
string = ["corret"]

login_sign_in_farme = 0

show_login_signin()
print('string = ',string)
if(string[0] == 'correct'):
    show_student_dashboard()
    print('after studnet dash',string)
    show_course_page()
    print('after course page',string)
    show_quiz_window()
    print('after quiz window',string)
# window.mainloop()