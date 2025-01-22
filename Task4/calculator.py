import tkinter as tk
from tkinter import messagebox
def append_to_display(value):
    """Adds the clicked button's value to the input field."""
    current_text = display_var.get()
    display_var.set(current_text + str(value))
def clear_display():
    """Clears the calculator display."""
    display_var.set("")
def evaluate_expression():
    """Calculates the result of the mathematical expression."""
    try:
        result = eval(display_var.get())  
        display_var.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Oops! Division by zero is not allowed.")
        display_var.set("")
    except Exception:
        messagebox.showerror("Input Error", "Invalid expression. Please try again.")
        display_var.set("")
root = tk.Tk()
root.title("Friendly Calculator")
root.geometry("300x400")
root.resizable(False, False)
display_var = tk.StringVar()  
display_field = tk.Entry(root, textvariable=display_var, font=("Arial", 20), 
                         justify="right", bd=10, relief="ridge")
display_field.pack(fill="both", padx=5, pady=5)
button_layout = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]
for row in button_layout:
    button_frame = tk.Frame(root)
    button_frame.pack(fill="both", expand=True)
    for button_text in row:
        if button_text == "C":
            action = clear_display
        elif button_text == "=":
            action = evaluate_expression
        else:
            action = lambda x=button_text: append_to_display(x)
        tk.Button(button_frame, text=button_text, font=("Arial", 18), 
                  command=action, width=5, height=2).pack(side="left", expand=True, fill="both")
root.mainloop() 