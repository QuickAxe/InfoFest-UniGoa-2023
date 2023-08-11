import tkinter as tk
from tkinter import ttk
import requests
import json

def quiz_window(string):

    window = tk.Tk()
    window.geometry("1000x600")
    window.title('EDU HUB')
    window.configure(bg='#353535')

    data = requests.get('http://127.0.0.1:8000/getQuiz/?courseVal=1').text
    data = json.loads(data)
    teacher = data[0]
    data = data[1:]


    q_number = tk.IntVar(value=0)

    question_text = tk.StringVar()
    option1text = tk.StringVar()
    option2text = tk.StringVar()
    option3text = tk.StringVar()
    option4text = tk.StringVar()
    
    option_selected = tk.StringVar()

    ans = [0,0,0,0,0]
    def update_ans():
        ans[q_number.get()] = int(option_selected.get())
        print(ans)

    question_var = ttk.Label(window,textvariable=question_text,font = ('Arial_Rounded_MT_Bold',24))#,background='#353535',foreground='#FFFFFF')
    option1_var = ttk.Radiobutton(window,variable=option_selected,textvariable=option1text,value=1,command=update_ans)
    option2_var = ttk.Radiobutton(window,variable=option_selected,textvariable=option2text,value=2,command=update_ans)
    option3_var = ttk.Radiobutton(window,variable=option_selected,textvariable=option3text,value=3,command=update_ans)
    option4_var = ttk.Radiobutton(window,variable=option_selected,textvariable=option4text,value=4,command=update_ans)

    question_text.set(f'Question {1} : '+data[0]['q1'])
    option1text.set(data[0]["q1A"])
    option2text.set(data[0]["q1B"])
    option3text.set(data[0]["q1C"])
    option4text.set(data[0]["q1D"])

    

    def change_qustion(change:int):
        def load_question():
            if(q_number.get()==0 and change==-1):
                return
            elif(q_number.get()==4 and change == 1):
                return
            q_number.set(q_number.get()+change)
            question_text.set(f'Question {q_number.get()+1} : '+data[q_number.get()]['q1'])
            option1text.set(data[q_number.get()]["q1A"])
            option2text.set(data[q_number.get()]["q1B"])
            option3text.set(data[q_number.get()]["q1C"])
            option4text.set(data[q_number.get()]["q1D"])
        return load_question
    
    question_var.place(x= 150,y = 100)
    option1_var.place(x = 150,y = 20+200)
    option2_var.place(x = 150,y = 50+200)
    option3_var.place(x = 150,y = 80+200)
    option4_var.place(x = 150,y = 110+200)


    def submit():
        total=0
        for ind,val in enumerate(ans):
            if (val == data[ind]['correctAns']):
                total+=1
        window.destroy()
        popup = tk.Tk()
        ttk.Label(popup,text=f"Total Score = {total}").pack()
        popup.mainloop()
        
    ttk.Button(window,text = "Previous Question",command=change_qustion(-1)).place(x = 20,y = 20)
    ttk.Button(window,text = "Next Question",command=change_qustion(1)).place(x = 900,y = 20)
    
    ttk.Button(window,text = 'Submit',command=submit).place(x = 800,y=500)

    window.mainloop()

quiz_window([""])