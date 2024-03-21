import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not (username and password and confirm_password):
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        # Here you can add code to save the registration details
        messagebox.showinfo("Success", "Registration Successful!")

# Create the main window
root = tk.Tk()
root.title("User Registration")

# Create labels
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

# Create entry fields
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.grid(row=2, column=1, padx=10, pady=5)

# Create register button
btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
