import tkinter as tk
import random
file_path = r"C:\Users\B-ONE\Desktop\c++\Dr Frank\.vscode\words.txt"
with open(file_path , "r") as f :
    words = [w.strip().lower() for w in f if len(w.strip()) ==5]
secret = random.choice(words)    
print ("just trying " , secret)
#preparing the main window
root = tk.Tk()
root.title("Wordle Game")
root.geometry("450x700")
root.resizable(False,False);
#preparing the game grid
rows , cols =  6,5
labels = [[None for _ in range (cols)] for _ in range (rows)]
current_row=0 #following the line the player plays it 
#grid colors
colors = {
    "green" : "#6aaa64" ,
    "yellow" : "#c9b458" ,
    "gray" : "#787c7e" }
#building the interface
for r in range(rows) :
    for c in range (cols) :
        label_box = tk.Label (root , text ="" , width = 4 , height =2 , font = ("Helvetica" , 18 , "bold") , relief = "solid" , borderwidth =1 , bg = "white")
        label_box.grid(row = r , column = c , padx=5 , pady=6)
        labels [r] [c] = label_box
#function for detecting
def check_word () :
    global current_row
    guess = entry.get().lower()
    if len(guess) != 5 :
        status.config(text ="Word must be 5 letters" , fg="red")
        return
    if guess not in words :
        status.config(text = "word is not in list" , fg="red")
        return 
    for i in range(cols) :
        labels [current_row] [i].config(text=guess[i].upper())
        if guess[i] == secret[i] :
            labels[current_row][i].config(bg = colors["green"] , fg="white")    
        elif guess[i] in secret :
            labels[current_row][i].config(bg = colors["yellow"] , fg = "white")
        else :
            labels[current_row][i].config(bg=colors["gray"] , fg="white")
    if guess == secret :
        status.config(text= "YOU HAD WON!!", fg="green")
        entry.config(state = "disabled")
    else :
        current_row += 1 
        if current_row == rows :
            status.config(text = f"game over , the secret word was :  {secret.upper()} ", fg="red" )
            entry.config(state= "disabled")
            return
    entry.delete(0 , tk.END)   
entry=tk.Entry(root , font= ("helvetica" , 18), justify="center") 
entry.grid(row=rows , column=0 , columnspan=3 , pady=10)

letter_buttons = {}

# ===== دالة تلوين الكيبورد =====
def update_keyboard(guess):
    for i, ch in enumerate(guess.upper()):
        if ch not in letter_buttons:
            continue
        btn = letter_buttons[ch]
        current_bg = btn.cget("bg")
        if guess[i] == secret[i]:
            btn.config(bg=colors["green"], fg="white")
        elif guess[i] in secret:
            # لو لسه مش أخضر
            if current_bg != colors["green"]:
                btn.config(bg=colors["yellow"], fg="white")
        else:
            if current_bg not in (colors["green"], colors["yellow"]):
                btn.config(bg=colors["gray"], fg="white")

# fuction for detecting
def check_word():
    global current_row
    guess = entry.get().lower()
    if len(guess) != 5:
        status.config(text="Word must be 5 letters", fg="red")
        return
    if guess not in words:
        status.config(text="Word is not in list", fg="red")
        return

    for i in range(cols):
        labels[current_row][i].config(text=guess[i].upper())
        if guess[i] == secret[i]:
            labels[current_row][i].config(bg=colors["green"], fg="white")
        elif guess[i] in secret:
            labels[current_row][i].config(bg=colors["yellow"], fg="white")
        else:
            labels[current_row][i].config(bg=colors["gray"], fg="white")

    update_keyboard(guess)

    if guess == secret:
        status.config(text="YOU HAD WON!!", fg="green")
        entry.config(state="disabled")
    else:
        current_row += 1
        if current_row == rows:
            status.config(text=f"Game over, the secret word was: {secret.upper()}", fg="red")
            entry.config(state="disabled")
            return
    entry.delete(0, tk.END)

# GUESS button
btn = tk.Button(root, text="GUESS?", font=("helvetica", 14), command=check_word)
btn.grid(row=rows, column=3, columnspan=2)

status = tk.Label(root, text="", font=("Helvetica", 12))
status.grid(row=rows+1, column=0, columnspan=5)

# keyboard
keyboard_rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

def press_letter(ch):
    current = entry.get()
    if len(current) < 5:
        entry.insert(tk.END, ch)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

start_row = rows + 2
for r, row_keys in enumerate(keyboard_rows):
    frame = tk.Frame(root)
    frame.grid(row=start_row + r, column=0, columnspan=5, pady=2)
    for ch in row_keys:
        btn = tk.Button(frame, text=ch, width=4, height=2,
                        command=lambda c=ch: press_letter(c))
        btn.pack(side="left", padx=2)
        letter_buttons[ch] = btn
    if r == len(keyboard_rows) - 1:
        back_btn = tk.Button(frame, text="⌫", width=4, height=2, command=backspace)
        back_btn.pack(side="left", padx=2)
root.mainloop()         




