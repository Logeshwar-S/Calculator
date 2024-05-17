
import math

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Projects\Calculator\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("338x553")
window.title("Calculator")
window.configure(bg = "#1A1A1A")
window.iconbitmap(r"F:\Projects\Calculator\assets\icon.ico")





# Function to handle button clicks for numbers

def on_number_click(number):
    entry.insert("end", str(number))

canvas = Canvas(
    window,
    bg = "#1A1A1A",
    height = 553,
    width = 338,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

result = 0

# Function to calculate the percentage

def calc_percentage():
    entry.insert("end", "%")

# Function to calculate the square of a number

def calc_sqaure():
    try:
        num = int(entry.get())  
        result = num ** 2  
        entry.delete(0, "end")  
        entry.insert("end", str(result)) 
    except ValueError:
        entry.delete(0, "end")
        entry.insert("end", "0")

# Function to clear current entry

def clear_entry():
    entry.delete(0, "end")

# Function to clear all entries

def clearall():
    entry.delete(0, "end")
    calculation_history.clear()
    update_history_display()

# Function to change sign

def plus_minus():
    num = float(entry.get())
    entry.delete(0, "end")  
    result = num
    if num > 0:
        entry.insert("end", "-" + str(result))
    else:
        result = (-1*num)
        entry.insert("end", str(result))
  
# Function to input dot operator

def dot():
    current_text = entry.get()
    if "." not in current_text:  # Check if a dot already exists
        entry.insert("end", ".")

# Function to calculate the square root of a number

def calc_sroot():
    result = math.sqrt(int(entry.get()))
    entry.delete(0, "end") 
    entry.insert("end", str(result))

# Function to clear single digit entry

def backspace():
    current_text = entry.get()
    if current_text == "Error":
        entry.delete(0, "end") 
    else:
        new_text = current_text[:-1]  # Remove the last character
        entry.delete(0, "end") 
        entry.insert("end", new_text)
    
# Function for division

def calc_div():
    entry.insert("end", "/")

# Function for multiplication

def calc_mul():
    entry.insert("end", "*")

# Function for addition

def calc_add():
    entry.insert("end", "+")

# Function for subtraction

def calc_sub():
    entry.insert("end", "-")

# Function to inverse a number

def inverse():
    try:
        result = 1/(int(entry.get()))
        entry.delete(0, "end")
        entry.insert("end", str(result))
    except:
        entry.insert("end","Error")

calculation_history = []  # For recent calculations

#Function to formulate expressions

def calc_equal():
  
    try:
        expression = entry.get()
        if any(char.isalpha() for char in expression):  # Check if expression contains alphabets
            entry.delete(0, "end")
            entry.insert("end", "Error")
        else:
            result = eval(entry.get())
            entry.delete(0, "end")  
            entry.insert("end", str(result)) 
            calculation = f"{expression} = {result}"
            calculation_history.append(calculation)
            update_history_display()
    except Exception as e:
        if entry.get()=="":
            pass
        else:
            entry.delete(0, "end")
            entry.insert("end", "Error")
            print("Error:", e)

# Function to update calculation history 

def update_history_display():
    recent_text.config(state="normal")  # Enable editing
    recent_text.delete(1.0, "end")  # Clear previous history
    if calculation_history:
        recent_text.insert("end", "\n".join(calculation_history[-2:]))  # Display last 2 calculations
    recent_text.config(state="disabled")  # Disable editing

canvas.place(x = 0, y = 0)
button_image_percentage = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_percentage = Button(
    image=button_image_percentage,
    borderwidth=0,
    highlightthickness=0,
    command=calc_percentage,
    relief="flat"
)
button_percentage.place(
    x=4.0,
    y=157.0,
    width=81.0,
    height=61.0
)

button_image_square = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_square = Button(
    image=button_image_square,
    borderwidth=0,
    highlightthickness=0,
    command=calc_sqaure,
    relief="flat"
)
button_square.place(
    x=87.0,
    y=223.0,
    width=81.0,
    height=61.0
)


entry_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg = canvas.create_image(
    169.0,
    82.0,
    image=entry_image
)

entry = Entry(
    bd=0,
    bg="#424141",
    fg="#FFFFFF",
    highlightthickness=0,
    font=('Arial', 40),
    justify="right",
    width=40,
    
    
)


entry.place(
    x=4.0,
    y=12.0,
    
    width=330.0,
    height=138.0
)

# Create the Text widget for displaying recent calculations

recent_text = Text(
    window,
    bd=0, 
    bg="#333333", 
    fg="#FFFFFF", 
    highlightthickness=0, 
    font=('Arial', 12), 
    wrap="word")
recent_text.place(
    x=4,
    y=6,
    width=330,
    height=40)


button_image_CE = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_CE = Button(
    image=button_image_CE,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry,
    relief="flat"
)
button_CE.place(
    x=87.0,
    y=157.0,
    width=81.0,
    height=61.0
)

button_image_C = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_C = Button(
    image=button_image_C,
    borderwidth=0,
    highlightthickness=0,
    command=clearall,
    relief="flat"
)
button_C.place(
    x=170.0,
    y=157.0,
    width=81.0,
    height=61.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    text="7",
    command=lambda: on_number_click(7),
    relief="flat"
)
button_7.place(
    x=4.0,
    y=289.0,
    width=81.0,
    height=61.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    text="8",
    command=lambda: on_number_click(8),
    relief="flat"
)
button_8.place(
    x=87.0,
    y=289.0,
    width=81.0,
    height=61.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    text="9",
    command=lambda: on_number_click(9),
    relief="flat"
)
button_9.place(
    x=170.0,
    y=289.0,
    width=81.0,
    height=61.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    text="6",
    command=lambda: on_number_click(6),
    relief="flat"
)
button_6.place(
    x=170.0,
    y=355.0,
    width=81.0,
    height=61.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    text="5",
    command=lambda: on_number_click(5),
    relief="flat"
)
button_5.place(
    x=87.0,
    y=355.0,
    width=81.0,
    height=61.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    text="4",
    command=lambda: on_number_click(4),
    relief="flat"
)
button_4.place(
    x=4.0,
    y=355.0,
    width=81.0,
    height=61.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    text="1",
    command=lambda: on_number_click(1),
    relief="flat"
)
button_3.place(
    x=4.0,
    y=421.0,
    width=81.0,
    height=61.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    text="2",
    command=lambda: on_number_click(2),
    relief="flat"
)
button_2.place(
    x=87.0,
    y=421.0,
    width=81.0,
    height=61.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    text="3",
    command=lambda: on_number_click(3),
    relief="flat"
)
button_1.place(
    x=170.0,
    y=421.0,
    width=81.0,
    height=61.0
)

button_image_plus_minus = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_plus_minus = Button(
    image=button_image_plus_minus,
    borderwidth=0,
    highlightthickness=0,
    command=plus_minus,
    relief="flat"
)
button_plus_minus.place(
    x=4.0,
    y=487.0,
    width=81.0,
    height=61.0
)

button_image_0 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_0 = Button(
    image=button_image_0,
    borderwidth=0,
    highlightthickness=0,
    text="0",
    command=lambda: on_number_click(0),
    relief="flat"
)

button_0.place(
    x=87.0,
    y=487.0,
    width=81.0,
    height=61.0
)

button_image_dot = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_dot = Button(
    image=button_image_dot,
    borderwidth=0,
    highlightthickness=0,
    command=dot,
    relief="flat"
)
button_dot.place(
    x=170.0,
    y=487.0,
    width=81.0,
    height=61.0
)


button_image_equal = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_equal = Button(
    image=button_image_equal,
    borderwidth=0,
    highlightthickness=0,
    command=calc_equal,
    relief="flat"
)
button_equal.place(
    x=253.0,
    y=487.0,
    width=81.0,
    height=61.0
)


button_image_add = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_add = Button(
    image=button_image_add,
    borderwidth=0,
    highlightthickness=0,
    command=calc_add,
    relief="flat"
)
button_add.place(
    x=253.0,
    y=421.0,
    width=81.0,
    height=61.0
)

button_image_sub = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_sub = Button(
    image=button_image_sub,
    borderwidth=0,
    highlightthickness=0,
    command=calc_sub,
    relief="flat"
)
button_sub.place(
    x=253.0,
    y=355.0,
    width=81.0,
    height=61.0
)

button_image_mul = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_mul = Button(
    image=button_image_mul,
    borderwidth=0,
    highlightthickness=0,
    command=calc_mul,
    relief="flat"
)
button_mul.place(
    x=253.0,
    y=289.0,
    width=81.0,
    height=61.0
)

button_image_inverse = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_inverse = Button(
    image=button_image_inverse,
    borderwidth=0,
    highlightthickness=0,
    command=inverse,
    relief="flat"
)
button_inverse.place(
    x=4.0,
    y=223.0,
    width=81.0,
    height=61.0
)

button_image_div = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_div = Button(
    image=button_image_div,
    borderwidth=0,
    highlightthickness=0,
    command=calc_div,
    relief="flat"
)
button_div.place(
    x=253.0,
    y=223.0,
    width=81.0,
    height=61.0
)

button_image_backspace = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_backspace = Button(
    image=button_image_backspace,
    borderwidth=0,
    highlightthickness=0,
    command=backspace,
    relief="flat"
)
button_backspace.place(
    x=253.0,
    y=157.0,
    width=81.0,
    height=61.0
)

button_image_sroot = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_sroot = Button(
    image=button_image_sroot,
    borderwidth=0,
    highlightthickness=0,
    command=calc_sroot,
    relief="flat"
)
button_sroot.place(
    x=170.0,
    y=223.0,
    width=81.0,
    height=61.0
)
window.resizable(False, False)
window.mainloop()
