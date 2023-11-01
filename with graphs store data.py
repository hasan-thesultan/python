import tkinter as tk
from tkinter import messagebox

def view_passwords():
    try:
        with open("password2.txt", 'r') as f:
            data = f.read()
        text.delete('1.0', tk.END)  # Clear the text widget
        text.insert(tk.END, data)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No passwords found.")

def add_password():
    name = name_entry.get()
    age = age_entry.get()
    if not name or not age:
        messagebox.showerror("Error", "Name and Age are required.")
        return
    try:
        age = int(age)
        if age <= 18:
            messagebox.showerror("Error", "Age must be greater than 18.")
        else:
            with open("password2.txt", 'a') as f:
                f.write(name + "-" + str(age) + "\n")
                name_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number.")

def delete_passwords():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete all passwords?")
    if confirmation:
        with open("password2.txt", 'w') as f:
            f.truncate(0)
        text.delete('1.0', tk.END)  # Clear the text widget

# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Create and configure widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

add_button = tk.Button(root, text="Add Password", command=add_password)
add_button.pack()

view_button = tk.Button(root, text="View Passwords", command=view_passwords)
view_button.pack()

delete_button = tk.Button(root, text="Delete All Passwords", command=delete_passwords)
delete_button.pack()

text = tk.Text(root, height=10, width=30)
text.pack()

# Start the GUI event loop
root.mainloop()
