import tkinter as tk

buttons =  [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]
right_buttons = ["÷", "×", "-", "+", "="]
top_buttons = ["AC", "+/-", "%"]

row_count = len(buttons)
col_count = len(buttons[0])

light_grey_color = "#D4D4D2"
black_color= "#1C1C1C"
dark_liver_color= "#505050"
orange_color = "#FF9500"
white_color = "#FFFFFF"

def clear_all():
    global A, operator, B
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
     # Handle floating point precision issues
    if isinstance(num, str):
        num = float(num)
    
    # Round to 10 decimal places to avoid floating point errors
    rounded = round(num, 10)
    
    if rounded % 1 == 0:
        return str(int(rounded))
    else:
        # Convert to string and remove any trailing zeros
        result = str(rounded)
        if '.' in result:
            result = result.rstrip('0').rstrip('.')  # Remove trailing zeros and decimal point if needed
        return result

def button_click(value):
    global right_buttons, top_buttons, A, operator, B, label
    
    if value in right_buttons:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    result = numA + numB
                elif operator == "-":
                    result = numA - numB
                elif operator == "×":
                    result = numA * numB
                elif operator == "÷":
                    if numB != 0:
                        result = numA / numB
                    else:
                        label["text"] = "Error"
                        return

                label["text"] = remove_zero_decimal(result)
                A = label["text"]   
                operator = None
                B = None

        elif value in "+-×÷":   
            A = label["text"]   
            operator = value   
            label["text"] = "0" 

    elif value == "AC":
        clear_all()
        label["text"] = "0"

    elif value == "+/-":
        try:
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        except ValueError:
            label["text"] = "Error"

    elif value == "%":
        try:
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        except ValueError:
            label["text"] = "Error"
    elif value == "√":
        try:
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)
        except ValueError:
            label["text"] = "Error"

    else:  # digit or dot
        if value == ".":
            if "." not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value



#window setup 
window = tk.Tk()
window.title("Calculator")
window.resizable(False,False)

frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame , text="0", anchor=tk.E, bg=black_color, fg=white_color, padx=10, font=("Arial", 30), height=2, width=col_count)
label.grid(row=0, column=0, columnspan=col_count, sticky="we")

for row in range(row_count):
    for column in range(col_count):
        value = buttons[row][column]
        button = tk.Button(frame, text=value , font=("Arial",30), width = col_count-1 , height=1 , command=lambda value=value: button_click(value))

        if value in right_buttons:
            button.config(bg=orange_color, fg=white_color)
        if value in top_buttons:
            button.config(bg=light_grey_color, fg=black_color)
        if value not in right_buttons and value not in top_buttons:
            button.config(bg=dark_liver_color, fg=white_color)
        button.grid(row=row+1, column=column)

#centre the window on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


#operations 
A = 0 
operator = None 
B = None 


window.mainloop()