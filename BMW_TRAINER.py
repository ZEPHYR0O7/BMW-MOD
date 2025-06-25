import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# === CONFIGURATION ===
CE_PATH = r"C:\Program Files\Cheat Engine\cheatengine-x86_64.exe"  # Change if your CE is in a different location
CT_FILE = "b1-Win64-Shipping-v5.CT"  # CT file name
PROCESS_NAME = "b1-Win64-Shipping.exe"

# === Functions ===
def attach_cheat_table():
    if not os.path.exists(CT_FILE):
        messagebox.showerror("CT File Missing", f"Cannot find: {CT_FILE}")
        return

    try:
        subprocess.Popen([CE_PATH, CT_FILE])
        messagebox.showinfo("Attached", "Cheat Engine table loaded.\nNow attach it manually if not auto.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Cheat Engine.\n{e}")

def exit_app():
    root.destroy()

# === Cyberpunk Style Setup ===
root = tk.Tk()
root.title("BMW Trainer")
root.geometry("500x650")
root.configure(bg="#0f0f0f")

# Fonts and Styles
title_font = ("Consolas", 20, "bold")
button_font = ("Consolas", 12, "bold")
label_font = ("Consolas", 11)
neon_color = "#00fff7"
frame_color = "#1c1c1c"

# === UI ===
tk.Label(root, text="🐒 BMW TRAINER", font=title_font, fg=neon_color, bg="#0f0f0f").pack(pady=20)

# Frame
frame = tk.Frame(root, bg=frame_color, padx=20, pady=20)
frame.pack(pady=10)

# Cheats List
cheats = [
    "Compact Mode",
    "Will Points",
    "No Will Lost in Shop",
    "EXP + Sparks",
    "Walk Speed Multiplier",
    "Jump Height Multiplier",
    "Inventory Editor",
    "Item ID + Quantity",
    "EXP / Sparks / Total XP"
]

# Checkboxes
vars = []
for cheat in cheats:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame, text=cheat, variable=var, font=label_font,
                         fg=neon_color, bg=frame_color, activebackground=frame_color,
                         activeforeground=neon_color, selectcolor="#101010")
    chk.pack(anchor="w", pady=5)
    vars.append(var)

# Buttons
btn_frame = tk.Frame(root, bg="#0f0f0f")
btn_frame.pack(pady=20)

attach_btn = tk.Button(btn_frame, text="🧠 Attach to Game", command=attach_cheat_table,
                       font=button_font, bg=neon_color, fg="#0f0f0f", padx=10, pady=5)
attach_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="❌ Exit", command=exit_app,
                     font=button_font, bg="#ff3b3b", fg="white", padx=10, pady=5)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()
