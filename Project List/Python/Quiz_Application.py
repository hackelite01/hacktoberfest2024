# This is a simple Quiz Appliication created using tkinter module in Python.


import tkinter as tk
from tkinter import messagebox


Ques = [
    " Who developed Python Programming Language?",
    " Is Python code compiled or interpreted?",
    "Which of the following is used to define a block of code in Python language?",
    "Which keyword is used for function in Python language?",
    "Which of the following functions is a built-in function in python?"
]

Options = [['Wick van Rossum','Rasmus Lerdorf','Guido van Rossum','Niene Stom'],
            ["Both compiled and interpreted", "neither compiled nor interpreted", "only compiled", "only interpreted"],
    ["Indentation", "Key", "Brackets", "All of the mentioned"],
    ["Function ","def","Fun" ,"Define"],
    ["factorial()","print()","seed()","sqrt()"]
]

Ans = [
    "Guido van Rossum",
    "Both compiled and interpreted",
    "Indentation",
    "def",
    "print()"
]

def show_question():
    
    question = Ques[count]
    quest_label.config(text=question)
    option_var.set(None)
    for i, option in enumerate(Options[count]):
        option_buttons[i].config(text=option, value=option)
    #show_result.config(text="")  

def checkanswer():
    global count, score

    selected_option = option_var.get()
    if selected_option:
        correctans = Ans[count]
        if selected_option == correctans:
            score += 1
            show_result.config(text="Correct!", fg="green")
        else:
            show_result.config(text=f"Incorrect! The correct answer was {correctans}.", fg="red")

        count += 1
        if count < len(Ques):
            show_question()
        else:
            p = int(score*100/len(Ques))
            messagebox.showinfo("SCORE", f"{username.get()}, your score is {score}/{len(Ques)},\n Percentage : {p}%")
            root.quit()
    else:
        messagebox.showwarning("No Selection", "Please select an option before submitting.")

def start_quiz():
    if not username.get():
        messagebox.showwarning("No Username", "Please enter username to start the quiz.")
        return
    userlabel.pack_forget()
    user_enter.pack_forget()
    start.pack_forget()
    quiz_interface()

def quiz_interface():
    global quest_label, option_var, option_buttons, show_result
    global count, score

    count = 0
    score = 0

    
    quest_label = tk.Label(root, text="", wraplength=400, font=('Helvetica', 16,'italic'))
    quest_label.pack(pady=20)

    
    option_var = tk.StringVar()
    option_buttons = []
    for i in range(4):
        rb = tk.Radiobutton(root, text="", variable=option_var, value="", wraplength=400, font=('Helvetica', 14),padx=20, pady=10)
        rb.pack(anchor=tk.W)
        option_buttons.append(rb)

    
    submit = tk.Button(root, text="Submit", command=checkanswer, font=('Helvetica', 14))
    submit.pack(pady=20)

    
    show_result = tk.Label(root, text="", font=('Helvetica', 14))
    show_result.pack(pady=20)

    show_question()


def quiz_app():
    global root, username, userlabel, user_enter, start

    root = tk.Tk()
    root.title("Quiz App")
    root.geometry('700x900')

    
    userlabel = tk.Label(root, text="Username:", font=('Helvetica', 20)) 
    userlabel.pack(pady=20)

    username = tk.StringVar()  
    user_enter = tk.Entry(root, textvariable=username, font=('Helvetica', 14))  
    user_enter.pack(pady=10)

    
    start = tk.Button(root, text="Start Quiz", command=start_quiz, font=('Helvetica', 14))
    start.pack(pady=20)

    root.mainloop()

def main():
    quiz_app()

main()
