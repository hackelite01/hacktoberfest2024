import tkinter as tk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def floor_division(x, y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Negative input."

def cube_root(x):
    return x ** (1/3)

def absolute_value(x):
    return abs(x)

def evaluate_expression(expression):
    try:
        expression = expression.replace('√', 'sqrt').replace('∛', 'cbrt').replace('abs', 'abs')
        
        allowed_names = {
            'sqrt': math.sqrt,
            'cbrt': lambda x: x ** (1/3),
            'abs': abs,
            '__builtins__': {}
        }
        
        result = eval(expression, allowed_names)
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception:
        return "Error!"

root = tk.Tk()
root.title("Minimalist Calculator")
root.geometry("400x600")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 24, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.pack(ipady=20)  

btns_frame = tk.Frame(root, width=400, height=500, bg="grey")
btns_frame.pack()

def click_button(item):
    global expression
    if item in ('√', '∛', 'abs'):
        if item == '√':
            expression += 'sqrt('
        elif item == '∛':
            expression += 'cbrt('
        elif item == 'abs':
            expression += 'abs('
    else:
        expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    result = evaluate_expression(expression)
    input_text.set(result)
    expression = str(result)

buttons = [
    ('C', 0, 0, 'clear'), ('√', 0, 1, 'operation'), ('∛', 0, 2, 'operation'), ('%', 0, 3, 'operator'),
    ('7', 1, 0, 'number'), ('8', 1, 1, 'number'), ('9', 1, 2, 'number'), ('/', 1, 3, 'operator'),
    ('4', 2, 0, 'number'), ('5', 2, 1, 'number'), ('6', 2, 2, 'number'), ('*', 2, 3, 'operator'),
    ('1', 3, 0, 'number'), ('2', 3, 1, 'number'), ('3', 3, 2, 'number'), ('-', 3, 3, 'operator'),
    ('0', 4, 0, 'number'), ('.', 4, 1, 'number'), ('abs', 4, 2, 'operation'), ('+', 4, 3, 'operator'),
    ('//', 5, 0, 'operator'), ('**', 5, 1, 'operator'), ('=', 5, 2, 'equal', 2)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    btn_type = btn[3]
    colspan = btn[4] if len(btn) > 4 else 1
    
    if btn_type == 'number' or btn_type == 'operator' or btn_type == 'operation':
        action = lambda x=text: click_button(x)
    elif btn_type == 'clear':
        action = clear
    elif btn_type == 'equal':
        action = equal
    
    button = tk.Button(btns_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=action)
    
    if colspan == 2:
        button.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1, sticky="nsew")
    else:
        button.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

for i in range(6):
    btns_frame.rowconfigure(i, weight=1)
for j in range(4):
    btns_frame.columnconfigure(j, weight=1)

root.mainloop()