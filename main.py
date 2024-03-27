import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    guess = int(guess_entry.get())
    if guess == secret:
        messagebox.showinfo("Result", "You guessed!")
        reset_game()
    else:
        messagebox.showinfo("Result", "Try again!")
        guess_entry.delete(0, 'end')

def reset_game():
    global secret
    secret = random.randint(1, num)
    guess_entry.delete(0, 'end')

def start_game():
    global num, secret
    num = int(num_entry.get())
    secret = random.randint(1, num)
    messagebox.showinfo("Start", "Let's play")

root = tk.Tk()
root.geometry("900x260")

num_label = tk.Label(root, text="Type a number:")
num_label.pack()

num_entry = tk.Entry(root)
num_entry.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

guess_label = tk.Label(root, text="Guess a number:")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack()

root.mainloop()
