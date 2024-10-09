import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Fake data storage (for demo purposes)
users = {}
groups = {}
messages = {}

# List of cities in Israel
cities_in_israel = [
    "Tel Aviv", "Jerusalem", "Haifa", "Beersheba", "Ashdod", "Netanya", "Holon", "Bat Yam",
    "Petah Tikva", "Rishon LeZion", "Eilat", "Herzliya"
]

# List of hobbies/interests
hobbies = ["Reading", "Walking", "Chess", "Gardening", "Cooking", "Music", "Sports", "Traveling"]

# Main Application
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Senior Connections")
        self.frame = None
        self.current_user = None
        self.selected_hobbies = []
        self.show_login()

    def clear_frame(self):
        if self.frame:
            self.frame.destroy()

    def center_frame(self, frame):
        frame.pack(expand=True)

    def show_login(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.center_frame(self.frame)

        tk.Label(self.frame, text="Login").grid(row=0, column=1)
        tk.Label(self.frame, text="Name:").grid(row=1, column=0)
        tk.Label(self.frame, text="Password:").grid(row=2, column=0)

        self.login_name = tk.Entry(self.frame)
        self.login_password = tk.Entry(self.frame, show="*")
        self.login_name.grid(row=1, column=1)
        self.login_password.grid(row=2, column=1)

        tk.Button(self.frame, text="Login", command=self.login_user).grid(row=3, column=1)
        tk.Button(self.frame, text="Register", command=self.show_register).grid(row=4, column=1)

    def login_user(self):
        name = self.login_name.get()
        password = self.login_password.get()
        if name in users and users[name]['password'] == password:
            self.current_user = users[name]
            self.show_profile()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def show_register(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.center_frame(self.frame)

        tk.Label(self.frame, text="Register").grid(row=0, column=1)
        tk.Label(self.frame, text="Name:").grid(row=1, column=0)
        tk.Label(self.frame, text="Password:").grid(row=2, column=0)
        tk.Label(self.frame, text="Age:").grid(row=3, column=0)
        tk.Label(self.frame, text="Town:").grid(row=4, column=0)
        tk.Label(self.frame, text="Interests:").grid(row=5, column=0)

        self.reg_name = tk.Entry(self.frame)
        self.reg_password = tk.Entry(self.frame, show="*")

        self.reg_name.grid(row=1, column=1)
        self.reg_password.grid(row=2, column=1)

        # Drop-down menu for selecting a town
        self.selected_town = tk.StringVar(self.frame)
        self.selected_town.set("CHOOSE CITY")  # Default value
        town_menu = tk.OptionMenu(self.frame, self.selected_town, *cities_in_israel)
        town_menu.grid(row=4, column=1)

        # Use Combobox for selecting age
        self.selected_age = tk.StringVar(self.frame)
        age_options = [str(age) for age in range(60, 100)] + ["100+"]
        self.age_combobox = ttk.Combobox(self.frame, textvariable=self.selected_age, values=age_options, width=10)  # Set width in characters
        self.age_combobox.set("60")  # Default value
        self.age_combobox.grid(row=3, column=1)

        # Create a frame for the interests with a scrollbar
        interests_frame = tk.Frame(self.frame)
        interests_frame.grid(row=5, column=1, sticky="nsew")

        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(interests_frame, height=150)
        self.scrollbar = tk.Scrollbar(interests_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create another frame inside the canvas to hold the checkboxes
        self.checkbox_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.checkbox_frame, anchor="nw")

        # Add checkboxes for selecting multiple interests
        self.selected_hobbies = []
        for i, hobby in enumerate(hobbies):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.checkbox_frame, text=hobby, variable=var)
            chk.grid(row=i, column=0, sticky="w")
            self.selected_hobbies.append(var)

        # Update the scroll region to encompass the entire checkbox frame
        self.checkbox_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        tk.Button(self.frame, text="Register", command=self.register_user).grid(row=6 + len(hobbies), column=1)
        tk.Button(self.frame, text="Back", command=self.show_login).grid(row=7 + len(hobbies), column=1)

    def register_user(self):
        name = self.reg_name.get()
        password = self.reg_password.get()
        age = self.selected_age.get()
        town = self.selected_town.get()
        interests = [hobby.get() for hobby, var in zip(hobbies, self.selected_hobbies) if var.get()]

        if not name or not password or not age or town == "CHOOSE CITY" or not interests:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if name in users:
            messagebox.showerror("Error", "User already exists")
        else:
            users[name] = {
                'name': name,
                'password': password,
                'age': age,
                'town': town,
                'interests': interests,
            }
            messagebox.showinfo("Success", "Registration successful")
            self.show_login()

    def show_profile(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.center_frame(self.frame)

        tk.Label(self.frame, text="Profile").grid(row=0, column=1)
        tk.Label(self.frame, text=f"Name: {self.current_user['name']}").grid(row=1, column=0)
        tk.Label(self.frame, text=f"Age: {self.current_user['age']}").grid(row=2, column=0)
        tk.Label(self.frame, text=f"Town: {self.current_user['town']}").grid(row=3, column=0)
        tk.Label(self.frame, text=f"Interests: {', '.join(self.current_user['interests'])}").grid(row=4, column=0)

        tk.Button(self.frame, text="Add Groups", command=self.show_add_groups).grid(row=5, column=0)
        tk.Button(self.frame, text="View Groups", command=self.show_groups).grid(row=6, column=0)

    def show_add_groups(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.center_frame(self.frame)

        tk.Label(self.frame, text="Add Group").grid(row=0, column=1)
        tk.Label(self.frame, text="Group Name:").grid(row=1, column=0)

        self.group_name = tk.Entry(self.frame)
        self.group_name.grid(row=1, column=1)

        tk.Button(self.frame, text="Add", command=self.add_group).grid(row=2, column=1)
        tk.Button(self.frame, text="Back", command=self.show_profile).grid(row=3, column=1)

    def add_group(self):
        group_name = self.group_name.get()
        if group_name not in groups:
            groups[group_name] = {
                'members': [self.current_user],
                'messages': [],
            }
            messagebox.showinfo("Success", f"Group '{group_name}' created")
        else:
            messagebox.showerror("Error", "Group already exists")

    def show_groups(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.center_frame(self.frame)

        tk.Label(self.frame, text="Groups").grid(row=0, column=1)

        row = 1
        for group_name in groups:
            tk.Button(self.frame, text=group_name, command=lambda g=group_name: self.show_group(g)).grid(row=row, column=0)
            row += 1

        tk.Button(self.frame, text="Back", command=self.show_profile).grid(row=row, column=1)

    def show_group(self, group_name):
        self.clear_frame()
        self.frame = tk.Frame(self.root)
        self.center_frame(self.frame)

        tk.Label(self.frame, text=f"Group: {group_name}").grid(row=0, column=1)

        row = 1
        for message in groups[group_name]['messages']:
            tk.Label(self.frame, text=message).grid(row=row, column=0)
            row += 1

        tk.Button(self.frame, text="Back", command=self.show_groups).grid(row=row, column=1)

# Create and run the application
root = tk.Tk()
app = App(root)
root.geometry("400x600")  # Set the initial window size
root.mainloop()
