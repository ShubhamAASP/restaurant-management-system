import customtkinter as ctk
from tkinter import messagebox
from db.admin_auth import validate_admin
import gui.dashboard as dashboard

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant Admin Login")
        self.geometry("400x300")
        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self, text="Admin Login", font=("Arial", 20)).pack(pady=20)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)

        login_btn = ctk.CTkButton(self, text="Login", command=self.try_login)
        login_btn.pack(pady=20)

    def try_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validate_admin(username, password):
            messagebox.showinfo("Login Success", "Welcome!")
            self.destroy()
            dashboard.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
