import customtkinter as ctk

def open_dashboard():
    win = ctk.CTk()
    win.title("Dashboard")
    win.geometry("600x400")
    ctk.CTkLabel(win, text="Welcome to Dashboard", font=("Arial", 24)).pack(pady=40)
    win.mainloop()
