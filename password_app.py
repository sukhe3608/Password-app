import tkinter as tk
import random as rn
import string
from tkinter import messagebox

class PasswordGenerator():
    def __init__(self, root):
        # Initialize the main window
        self.root = root

        # Set minimum and maximum size of the window
        self.root.minsize(400, 200)
        self.root.maxsize(300, 700)  
        self.root.title("Password Recommender")
        
        # Create and place the title label
        self.label = tk.Label(text="RANDOM PASSWORD RECOMMENDER", font=(None, 16), bg="black", fg="white")
        self.label.grid(row=0, column=1, columnspan=3)  

        # Create and place the password length label and entry
        self.length_label = tk.Label(text="Enter the length of the password you want:", font=(None, 12))
        self.length_label.grid(row=2, column=1, columnspan=3)  
        self.length = tk.Entry()
        self.length.grid(row=3, column=1, columnspan=3)  

        # Create and place the password strength label
        self.strength_label = tk.Label(text="Select the strength of the password:", font=(None, 12))
        self.strength_label.grid(row=4, column=1, columnspan=3) 

        # Create and place the buttons for password strength selection
        self.weak_button = tk.Button(text="WEAK", command=lambda: self.generate_password("weak"))
        self.weak_button.grid(row=5, column=1)
        
        self.medium_button = tk.Button(text="MEDIUM", command=lambda: self.generate_password("medium"))
        self.medium_button.grid(row=5, column=2)
        
        self.strong_button = tk.Button(text="STRONG", command=lambda: self.generate_password("strong"))
        self.strong_button.grid(row=5, column=3)

    def weak_password(self, length):
        # Generate a weak password
        characters = string.ascii_lowercase + string.digits
        return ''.join(rn.choice(characters) for _ in range(length))

    def medium_password(self, length):
        # Generate a medium strength password
        characters = string.ascii_letters + string.digits
        return ''.join(rn.choice(characters) for _ in range(length))

    def strong_password(self, length):
        # Generate a strong password
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(rn.choice(characters) for _ in range(length))
    
    def generate_password(self, strength=""):
        try:
            # Get the password length from the entry box
            length = int(self.length.get())
        except ValueError:
            # Show an error message if the length is not an integer
            messagebox.showerror("Error", "Please enter a valid password length.")
            return
        
        # Generate password based on the selected strength
        if strength == "weak":
            password = self.weak_password(length)
        elif strength == "medium":
            password = self.medium_password(length)
        elif strength == "strong":
            password = self.strong_password(length)
        else:
            messagebox.showerror("Error", "Invalid choice")
            return
        
        # Display the generated password
        messagebox.showinfo("Password Generated", f"Your {strength} password is: {password}")

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
