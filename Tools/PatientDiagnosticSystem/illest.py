import tkinter as tk
from tkinter import messagebox
import random

def get_diagnosis(event=None):
    name = name_entry.get().strip()
    
    if not name:
        messagebox.showwarning("Input Error", "Please enter a patient name.")
        return

    try:
        with open('illnesses.txt', 'r', encoding='utf-8') as file:
            illnesses = [line.strip() for line in file.readlines() if line.strip()]
        
        if not illnesses:
            messagebox.showerror("Error", "The database is empty.")
            return

        raw_illness = random.choice(illnesses)
        severity = random.randint(1, 5)
        
        # 1. Logic for "x" (Positive Results)
        is_positive = raw_illness.lower().startswith('x')
        # Clean the name (remove the x for display)
        display_illness = raw_illness[1:] if is_positive else raw_illness

        # 2. Censorship Logic
        # If censored is checked AND it's not a positive 'x' word
        if censor_var.get() and not is_positive:
            display_illness = "BAD CONSEQUENCE"

        # 3. Color Logic
        # Positive 'x' words are green, otherwise use severity colors
        if is_positive:
            sev_color = "#4ade80" # Neon Green
            text_color = "#4ade80"
        else:
            colors = ["#4ade80", "#facc15", "#fb923c", "#f87171", "#ef4444"]
            sev_color = colors[severity-1]
            text_color = "#f1f5f9" # Default off-white

        # Update Main Display
        patient_display.config(text=name.upper())
        illness_display.config(text=display_illness, fg=text_color)
        severity_display.config(text=f"SEVERITY: {'★' * severity}{'☆' * (5-severity)}", fg=sev_color)

        # Add to History List
        history_entry = f" {name.upper()} | {display_illness} | LVL {severity}"
        history_list.insert(0, history_entry)
        
        # Color the history item specifically if it was an 'x' word
        if is_positive:
            history_list.itemconfig(0, fg="#4ade80")
        else:
            history_list.itemconfig(0, fg="#38bdf8") # Default history blue
        
        name_entry.delete(0, tk.END)
        
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'illnesses.txt' not found.")

# --- UI Setup ---
root = tk.Tk()
root.title("ADVANCED DIAGNOSTIC TERMINAL")
root.geometry("700x800")
root.configure(bg="#0f172a")

# Fonts & Variables
title_font = ("Courier New", 18, "bold")
label_font = ("Helvetica", 10, "bold")
result_font = ("Verdana", 24, "bold")
history_font = ("Consolas", 10)
censor_var = tk.BooleanVar()

# Title
tk.Label(root, text="PATIENT DIAGNOSTIC SYSTEM", font=title_font, 
         bg="#0f172a", fg="#38bdf8").pack(pady=15)

# Input Section
input_frame = tk.Frame(root, bg="#1e293b", padx=20, pady=15)
input_frame.pack(pady=10, fill="x", padx=50)

name_entry = tk.Entry(input_frame, font=("Consolas", 14), bg="#0f172a", 
                      fg="white", insertbackground="white", justify="center")
name_entry.pack(pady=5)
name_entry.focus_set()
root.bind('<Return>', get_diagnosis)

# Control Section (Button + Checkbox)
control_frame = tk.Frame(root, bg="#0f172a")
control_frame.pack(pady=10)

diagnose_button = tk.Button(
    control_frame, text="RUN ANALYSIS", command=get_diagnosis,
    bg="#3b82f6", fg="white", font=("Helvetica", 12, "bold"),
    relief="flat", padx=20, pady=10, cursor="hand2"
)
diagnose_button.pack(side="left", padx=10)

censor_check = tk.Checkbutton(
    control_frame, text="CENSOR RESULTS", variable=censor_var,
    bg="#0f172a", fg="#94a3b8", selectcolor="#0f172a",
    activebackground="#0f172a", activeforeground="white",
    font=label_font
)
censor_check.pack(side="left", padx=10)

# Result Card
result_frame = tk.Frame(root, bg="#0f172a", highlightbackground="#334155", highlightthickness=1)
result_frame.pack(pady=10, fill="x", padx=50)

patient_display = tk.Label(result_frame, text="", font=("Courier New", 14), bg="#0f172a", fg="#94a3b8")
patient_display.pack(pady=(10, 0))

illness_display = tk.Label(result_frame, text="READY", font=result_font, 
                           bg="#0f172a", fg="#f1f5f9", wraplength=550)
illness_display.pack(pady=5)

severity_display = tk.Label(result_frame, text="", font=("Courier New", 16, "bold"), bg="#0f172a")
severity_display.pack(pady=(0, 15))

# History Section
tk.Label(root, text="RECENT DIAGNOSTIC LOGS", font=label_font, bg="#0f172a", fg="#64748b").pack(pady=(20, 0))
history_frame = tk.Frame(root, bg="#1e293b")
history_frame.pack(pady=(10, 20), fill="both", expand=True, padx=50)

scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side="right", fill="y")

history_list = tk.Listbox(
    history_frame, font=history_font, bg="#1e293b", fg="#38bdf8", 
    borderwidth=0, highlightthickness=0, yscrollcommand=scrollbar.set
)
history_list.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar.config(command=history_list.yview)

root.mainloop()