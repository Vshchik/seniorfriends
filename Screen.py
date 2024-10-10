import tkinter as tk
from tkinter import messagebox
import pickle

import Users
from Groups import Group
from Messages import Messages

users = []
filtered_groups = []
group_messages = []

# List of cities in Israel
cities_in_israel = [
    "Tel Aviv", "Jerusalem", "Haifa", "Beersheba", "Ashdod", "Netanya", "Holon", "Bat Yam",
    "Petah Tikva", "Rishon LeZion", "Eilat", "Herzliya"
]

# List of hobbies/interests
hobbies = ["Reading", "Walking", "Chess", "Gardening", "Cooking", "Music", "Sports", "Traveling"]


for city in cities_in_israel:
    global groups
    group = Group('', '', [])
    groups = group.get_all_groups()
    groups.pop(0)



# Main Application
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Senior Connections")
        self.frame = None
        self.current_user = None
        self.selected_hobbies = []
        self.load_data()  # Load user data at startup
        self.show_login()

    def load_data(self):
        global users
        users = Users.get_all_users()

    def clear_frame(self):
        if self.frame:
            self.frame.destroy()

    def show_login(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Login", font=('Arial', 18)).grid(row=0, column=1, pady=10)
        tk.Label(self.frame, text="Username:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Password:").grid(row=2, column=0, sticky="e", pady=5)

        self.login_username = tk.Entry(self.frame)
        self.login_password = tk.Entry(self.frame, show="*")
        self.login_username.grid(row=1, column=1)
        self.login_password.grid(row=2, column=1)

        tk.Button(self.frame, text="Login", command=self.login_user).grid(row=3, column=1, pady=5)
        tk.Button(self.frame, text="Register", command=self.show_register).grid(row=4, column=1)

    def login_user(self):
        username = self.login_username.get()
        password = self.login_password.get()
        user = Users.User(username, '', password,"", [])
        if user.user_exist() and user.login():
            user.user_id = user.get_user_id()
            self.current_user = user.get_user_by_id()
            self.show_profile()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def show_register(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Register", font=('Arial', 18)).grid(row=0, column=1, pady=10)
        # tk.Label(self.frame, text="Full Name:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Username:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Password:").grid(row=2, column=0, sticky="e", pady=5)
        # tk.Label(self.frame, text="Confirm Password:").grid(row=4, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Age:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Town:").grid(row=4, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Interests:").grid(row=5, column=0, sticky="e", pady=5)

        # self.reg_full_name = tk.Entry(self.frame)
        self.reg_username = tk.Entry(self.frame)
        self.reg_password = tk.Entry(self.frame, show="*")
        # self.reg_confirm_password = tk.Entry(self.frame, show="*")
        self.reg_age = tk.StringVar(self.frame)
        age_options = [str(age) for age in range(60, 100)] + ["100+"]

        self.reg_age.set(age_options[0])  # Default age
        age_menu = tk.OptionMenu(self.frame, self.reg_age, *age_options)
        age_menu.grid(row=3, column=1)

        # self.reg_full_name.grid(row=1, column=1)
        self.reg_username.grid(row=1, column=1)
        self.reg_password.grid(row=2, column=1)
        # self.reg_confirm_password.grid(row=4, column=1)

        # Drop-down menu for selecting a town
        self.selected_town = tk.StringVar(self.frame)
        self.selected_town.set("Choose City")  # Default value
        tk.OptionMenu(self.frame, self.selected_town, *cities_in_israel).grid(row=4, column=1)

        # Checkboxes for selecting multiple interests
        self.selected_hobbies = []
        for hobby in hobbies:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.frame, text=hobby, variable=var)
            chk.grid(sticky="w")
            self.selected_hobbies.append((hobby, var))

        tk.Button(self.frame, text="Register", command=self.register_user).grid(column=1, pady=10)
        tk.Button(self.frame, text="Back", command=self.show_login).grid(column=1)

    def register_user(self):
        # full_name = self.reg_full_name.get()
        username = self.reg_username.get()
        password = self.reg_password.get()
        # confirm_password = self.reg_confirm_password.get()
        age = self.reg_age.get()
        town = self.selected_town.get()
        interests = []

        for hobby, var in self.selected_hobbies:
            if var.get():
                interests.append(hobby)

        if username in users:
            messagebox.showerror("Error", "Username already exists")
        # elif password != confirm_password:
        #     messagebox.showerror("Error", "Passwords do not match")
        else:
            user = Users.User(username, age, password, town, interests)
            # users[username] = {
            #     'full_name': full_name,
            #     'username': username,
            #     'password': password,
            #     'age': age,
            #     'town': town,
            #     'interests': interests,
            #     'groups': []  # Initialize user's groups
            # }
            # # Save users to file
            # with open('users_data.pkl', 'wb') as file:
            #     pickle.dump(users, file)
            user.add_new_user()
            user = user.user_dict_to_list()
            users.append(user)

            messagebox.showinfo("Success", "Registration successful")
            self.show_login()

    def show_profile(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Profile", font=('Arial', 18)).grid(row=0, column=0, pady=5)
        # tk.Label(self.frame, text=f"Full Name: {self.current_user['full_name']}").grid(row=1, column=0, pady=5)
        tk.Label(self.frame, text=f"Username: {self.current_user.name}").grid(row=1, column=0, pady=5)
        tk.Label(self.frame, text=f"Age: {self.current_user.age}").grid(row=2, column=0, pady=5)
        # tk.Label(self.frame, text=f"Town: {self.current_user['town']}").grid(row=4, column=0, pady=5)
        tk.Label(self.frame, text=f"Interests: {', '.join(self.current_user.interests)}").grid(row=3, column=0, pady=5)

        # tk.Button(self.frame, text="Edit Profile", command=self.show_edit_profile).grid(row=6, column=0, pady=5)
        tk.Button(self.frame, text="Add Groups", command=self.show_add_groups).grid(row=4, column=0, pady=5)
        tk.Button(self.frame, text="View Groups", command=self.show_groups).grid(row=5, column=0, pady=5)
        # tk.Button(self.frame, text="Delete Account", command=self.delete_account).grid(row=9, column=0, pady=5)
        tk.Button(self.frame, text="Exit Account", command=self.show_login).grid(row=6, column=0, pady=5)

    def show_edit_profile(self):
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Edit Profile", font=('Arial', 18)).grid(row=0, column=1, pady=10)
        # tk.Label(self.frame, text="Full Name:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Password:").grid(row=1, column=0, sticky="e", pady=5)
        # tk.Label(self.frame, text="Confirm Password:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Age:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(self.frame, text="Town:").grid(row=4, column=0, sticky="e", pady=5)

        # self.edit_full_name = tk.Entry(self.frame)
        # self.edit_full_name.insert(0, self.current_user['full_name'])

        self.edit_password = tk.Entry(self.frame, show="*")
        # self.edit_confirm_password = tk.Entry(self.frame, show="*")

        self.edit_age = tk.StringVar(self.frame)
        self.edit_age.set(self.current_user['age'])
        age_options = [str(age) for age in range(60, 100)] + ["100+"]
        tk.OptionMenu(self.frame, self.edit_age, *age_options).grid(row=4, column=1)

        # Town dropdown
        self.edit_town = tk.StringVar(self.frame)
        self.edit_town.set(self.current_user['town'])
        tk.OptionMenu(self.frame, self.edit_town, *cities_in_israel).grid(row=5, column=1)

        # Checkboxes for interests
        self.edit_selected_hobbies = []
        for hobby in hobbies:
            var = tk.BooleanVar(value=hobby in self.current_user['interests'])
            chk = tk.Checkbutton(self.frame, text=hobby, variable=var)
            chk.grid(sticky="w")
            self.edit_selected_hobbies.append((hobby, var))

        # self.edit_full_name.grid(row=1, column=1)
        self.edit_password.grid(row=1, column=1)
        # self.edit_confirm_password.grid(row=3, column=1)
        tk.Button(self.frame, text="Save Changes", command=self.save_profile_changes).grid(row=7, column=1, pady=5)
        tk.Button(self.frame, text="Back", command=self.show_profile).grid(row=8, column=1, pady=5)

    def save_profile_changes(self):
        # new_full_name = self.edit_full_name.get()
        new_password = self.edit_password.get()
        # confirm_password = self.edit_confirm_password.get()
        new_age = self.edit_age.get()
        new_town = self.edit_town.get()
        new_interests = []

        for hobby, var in self.edit_selected_hobbies:
            if var.get():
                new_interests.append(hobby)

        # if new_password and new_password != confirm_password:
        #     messagebox.showerror("Error", "Passwords do not match")
        #     return

        # self.current_user['full_name'] = new_full_name
        if new_password:
            self.current_user['password'] = new_password
        self.current_user['age'] = new_age
        self.current_user['town'] = new_town
        self.current_user['interests'] = new_interests

        # Save updated user data
        users[self.current_user['username']] = self.current_user
        with open('users_data.pkl', 'wb') as file:
            pickle.dump(users, file)

        messagebox.showinfo("Success", "Profile updated successfully")
        self.show_profile()

    def delete_account(self):
        del users[self.current_user['username']]
        with open('users_data.pkl', 'wb') as file:
            pickle.dump(users, file)
        messagebox.showinfo("Success", "Account deleted successfully")
        self.show_login()

    def show_add_groups(self):
        global filtered_groups
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Add Groups", font=('Arial', 18)).grid(row=0, column=1, pady=10)
        tk.Label(self.frame, text="Choose Group:").grid(row=1, column=0, pady=5)

        for group in groups:
            if self.current_user.town == group[1] and any(hobby in eval(group[3]) for hobby in self.current_user.interests):
                filtered_groups.append([group[1], eval(group[3])[0]])

        self.selected_group = tk.StringVar(self.frame)
        self.selected_group.set("__Choose Group__")  # Default value
        tk.OptionMenu(self.frame, self.selected_group, *filtered_groups).grid(row=1, column=1)

        tk.Button(self.frame, text="Join Group", command=self.join_group).grid(row=2, column=1, pady=5)
        tk.Button(self.frame, text="Back", command=self.show_profile).grid(row=3, column=1, pady=5)

    def join_group(self):
        group_name = self.selected_group.get()
        group_name = list(eval(group_name))
        if group_name in filtered_groups:
            group = Group(group_name[0], "0", group_name[1])
            group.group_id = group.get_group_id()
            members = group.get_all_members()
            is_in = False
            if members:
                for member in members:
                    if self.current_user.user_id == member:
                        is_in = True

            if not is_in:
                group.add_member(self.current_user.user_id)
                groups.append(group.group_to_list()) # Add group to user's list

                # # Save users to file
                # with open('users_data.pkl', 'wb') as file:
                #     pickle.dump(users, file)
                #
                # # Save groups data
                # with open('groups_data.pkl', 'wb') as file:
                #     pickle.dump(groups, file)

                messagebox.showinfo("Success", f"You have joined {group_name[0]} {group_name[1]}")
            else:
                messagebox.showerror("Error", "You are already a member of this group")
        else:
            messagebox.showerror("Error", "Please select a valid group")

    def show_groups(self):
        global groups
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Your Groups", font=('Arial', 18)).grid(row=0, column=0, pady=5)

        row = 1
        for group_name in groups:
            group = Group(group_name[1], group_name[2], group_name[3], group_id=group_name[0])
            group.users_id = group.get_all_members()

            if group.check_member_in_group(self.current_user.user_id):
                if not type(group_name[3]) is list:
                    group_name[3] = eval(group_name[3])
                group_temp = [group_name[1], group_name[3]]
                tk.Button(self.frame, text=group_temp, command=lambda name=group: self.show_group(name)).grid(row=row, column=0, pady=5)
                row += 1

        tk.Button(self.frame, text="Back", command=self.show_profile).grid(row=row, column=1, pady=5)

    def show_group(self, group_name: Group):
        self.clear_frame()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text=f"{group_name.town} {group_name.interests[0]}", font=('Arial', 18)).grid(row=0, column=0, pady=5)

        tk.Button(self.frame, text="Members", command=lambda: self.show_members(group_name)).grid(row=1, column=0, pady=5)

        tk.Label(self.frame, text="Messages:").grid(row=2, column=0, pady=5)
        row = 3

        global group_messages
        group_messages = group_name.get_messages_in_group()

        for msg in group_messages:
            user = Users.User('',"", '', "", [], user_id=msg[1])
            user = user.get_user_by_id()
            tk.Label(self.frame, text=f"{user.name}: {msg[3]}").grid(row=row, column=0, pady=5)
            row += 1

        self.message_text = tk.Entry(self.frame)
        self.message_text.grid(row=row, column=0, pady=5)
        tk.Button(self.frame, text="Send", command=lambda: self.send_message(group_name)).grid(row=row, column=1, pady=5)
        tk.Button(self.frame, text="Back", command=self.show_groups).grid(row=row + 1, column=1, pady=5)

    def show_members(self, group_name):
        members_info = ""
        for member in group_name.users_id:
            user = Users.User("", "", "", "", [], member)
            user = user.get_user_by_id()
            members_info += f"{user.name} (Age: {user.age})\n"
        messagebox.showinfo("Group Members", members_info)

    def send_message(self, group_name):
        global group_messages
        msg_text = self.message_text.get()
        if msg_text:
            message = Messages(self.current_user.user_id, group_name.group_id, msg_text)
            message.create_message()
            message = message.message_to_list()
            group_messages.append(message)
            # groups[group_name]['messages'].append({'name': self.current_user['full_name'], 'text': msg_text})
            self.message_text.delete(0, tk.END)
            self.show_group(group_name)

            # Save groups data
            with open('groups_data.pkl', 'wb') as file:
                pickle.dump(groups, file)
        else:
            messagebox.showerror("Error", "Please enter a message")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
