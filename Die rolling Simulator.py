import tkinter as tk
import random

window=tk.Tk()
window.title("Rolling The Dices")
window.geometry("800x400")
window.resizable(False,False)
window.configure(bg="lightblue")


label=tk.Label(window,bg="lightblue",font=("times",200),fg="orange")


def roll_dices():
    die_dots=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    
    label.configure(text=f'{random.choice(die_dots)}')
    label.pack()



roll_button=tk.Button(window,text="ROLL",bg="blue",fg="white",command=roll_dices)
roll_button.pack(padx=50,pady=50)
    
window.mainloop()
