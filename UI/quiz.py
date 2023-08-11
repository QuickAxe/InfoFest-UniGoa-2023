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
    # data =[
    #     {
    #         "question":"Question to be displayed ?",
    #         "op1":"Option 1",
    #         "op2":"Option 2",
    #         "op3":"Option 3",
    #         "op4":"Option 4",
    #         "cor_opt":1
    #     },
    #     {
    #         "question":"Question to be  ?",
    #         "op1":"Option 1",
    #         "op2":"Option 2",
    #         "op3":"Option 3",
    #         "op4":"Option 4",
    #         "cor_opt":1
    #     },
    #     {
    #         "question":"Question to be displayed ?",
    #         "op1":"Option 1",
    #         "op2":"Option 2",
    #         "op3":"Option 3",
    #         "op4":"Option 4",
    #         "cor_opt":1
    #     },
    #     {
    #         "question":"Question to be  ?",
    #         "op1":"Option 1",
    #         "op2":"Option 2",
    #         "op3":"Option 3",
    #         "op4":"Option 4",
    #         "cor_opt":1
    #     },
    #     {
    #         "question":"Question to be displayed ?",
    #         "op1":"Option 1",
    #         "op2":"Option 2",
    #         "op3":"Option 3",
    #         "op4":"Option 4",
    #         "cor_opt":1
    #     },
        
    # ]


    q_number = tk.IntVar(value=0)

    question_text = tk.StringVar()
    option1text = tk.StringVar()
    option2text = tk.StringVar()
    option3text = tk.StringVar()
    option4text = tk.StringVar()
    
    option_selected = tk.IntVar()

    question_var = ttk.Label(window,textvariable=question_text,font = ('Arial_Rounded_MT_Bold',12))#,background='#353535',foreground='#FFFFFF')
    option1_var = ttk.Radiobutton(window,textvariable=option1text,value=1,command=lambda:option_selected.set(1))
    option2_var = ttk.Radiobutton(window,textvariable=option2text,value=2,command=lambda:option_selected.set(2))
    option3_var = ttk.Radiobutton(window,textvariable=option3text,value=3,command=lambda:option_selected.set(3))
    option4_var = ttk.Radiobutton(window,textvariable=option4text,value=4,command=lambda:option_selected.set(4))

    question_text.set(f'Question {1} : '+data[0]['q1'])
    option1text.set(data[0]["q1A"])
    option2text.set(data[0]["q1B"])
    option3text.set(data[0]["q1C"])
    option4text.set(data[0]["q1D"])



    def change_qustion(change:int):
        def load_question():
            print(change)
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
    
    question_var.place(x= 200,y = 100)
    option1_var.place(x = 300,y = 300)
    option2_var.place(x = 300,y = 350)
    option3_var.place(x = 300,y = 400)
    option4_var.place(x = 300,y = 450)

    buttonL = ttk.Button(window,text = "Previous Question",command=change_qustion(-1)).place(x = 100,y = 150)
    buttonR = ttk.Button(window,text = "Next Question",command=change_qustion(1)).place(x = 900,y = 150)
    

    window.mainloop()