import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

# Adjust this if legendary.exe is not in PATH
LEGENDARY_CMD = "legendary"

def run_command(cmd):
    try:
        output = subprocess.check_output([LEGENDARY_CMD] + cmd, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

def login():
    result = run_command(["auth"])
    messagebox.showinfo("Login", result)

def list_games():
    result = run_command(["list-installed"])
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, result)

def install_game():
    game = simpledialog.askstring("Install Game", "Enter game AppName:")
    if game:
        result = run_command(["install", game])
        messagebox.showinfo("Install", result)

def launch_game():
    game = simpledialog.askstring("Launch Game", "Enter game AppName:")
    if game:
        result = run_command(["launch", game])
        messagebox.showinfo("Launch", result)

root = tk.Tk()
root.title("Legendary GUI")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Login", command=login).grid(row=0, column=0, padx=5)
tk.Button(frame, text="List Installed Games", command=list_games).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Install Game", command=install_game).grid(row=1, column=0, padx=5)
tk.Button(frame, text="Launch Game", command=launch_game).grid(row=1, column=1, padx=5)

text_box = tk.Text(root, width=80, height=20)
text_box.pack(pady=10)

root.mainloop()
