import tkinter as tk
from tkinter import messagebox
import re
import os

info_array = []
# Create Window
arra = 1


class RegistrationForm(tk.Tk):

    global image_path
    image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets"
        )
    
    def __init__(self):
        super().__init__()
        # win = tk.Tk()
        self.title("GUI Python")
        height = 650
        width = 1240
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))

        self.configure(bg="#525561")

        self.home_frame = tk.Frame(self, bg="#272A37")
        self.home_frame.place(x=0, y=0, relwidth=1, relheight=1)

        # ==============bG Image================

        self.create_widgets()

    def create_widgets(self):
        # Add Frame
        self.backgroundImage = tk.PhotoImage(file= os.path.join(image_path, "image_1.png"))
        self.bg_image = tk.Label(
            self.home_frame, image=self.backgroundImage, bg="#525561"
        )
        self.bg_image.place(x=120, y=28)

        self.label = tk.Label(
            self,
            text="PYTHON GUI",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37",
        )
        self.label.pack(padx=15, pady=15)

        self.name = tk.Label(
            self.bg_image,
            text="Name:",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        self.name.place(x=200, y=50)
        self.nameEntry = tk.Entry(
            self.bg_image,
            width=40,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
            bd=3,
        )
        self.nameEntry.place(x=300, y=50)

        # Email
        email = tk.Label(
            self.bg_image,
            text="Email:",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        email.place(x=200, y=100)
        self.emailVar = tk.StringVar()
        emailEntry = tk.Entry(
            self.bg_image,
            width=40,
            textvariable=self.emailVar,
            bd=3,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        emailEntry.place(x=300, y=100)

        # password
        password = tk.Label(
            self.bg_image,
            text="Password:",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        password.place(x=200, y=150)
        self.passwordVar = tk.StringVar()
        self.passwordEntry = tk.Entry(
            self.bg_image,
            width=40,
            textvariable=self.passwordVar,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
            bd=3,
            show="*",
        )
        self.passwordEntry.place(x=300, y=150)
        self.show_hide = tk.Button(
            self.bg_image, text="Show", width=5, bg="#272A37", fg="#FFFFFF", bd=0
        )
        self.show_hide.place(x=670, y=150)
        self.show_hide.bind(
            "<Button-1>",
            lambda e: self.show_hide.config(
                text="Hide" if self.show_hide.cget("text") == "Show" else "Show"
            ),
        )

        # Radio Button For gender
        gender = tk.Label(
            self.bg_image,
            text="Gender: ",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        gender.place(x=200, y=200)
        self.gender = tk.StringVar()
        self.gender.set("Male")
        male_radio = tk.Radiobutton(
            self.bg_image,
            text="Male",
            variable=self.gender,
            value="Male",
            bg="#272A37",
            fg="grey",
        )
        male_radio.place(x=300, y=200)
        female_radio = tk.Radiobutton(
            self.bg_image,
            text="Female",
            variable=self.gender,
            value="Female",
            bg="#272A37",
            fg="grey",
        )
        female_radio.place(x=400, y=200)

        # Spinbox
        status = tk.Label(
            self.bg_image,
            text="Status: ",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        status.place(x=200, y=250)
        choices = ["Private", "Public"]
        self.selected_choice = tk.StringVar()
        self.selected_choice.set("Private")
        spinbox = tk.Spinbox(
            self.bg_image,
            values=choices,
            textvariable=self.selected_choice,
            width=10,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12, "bold"),
        )
        spinbox.place(x=300, y=250)

        # List to select country
        country_label = tk.Label(
            self.bg_image,
            text="Country:",
            font=("yu gothic ui", 12),
            bg="#272A37",
            fg="#FFFFFF",
        )
        country_label.place(x=200, y=300)
        countries = [
            "USA",
            "Canada",
            "UK",
            "Australia",
        ]  # Replace with your desired list of countries
        self.selected_country = tk.StringVar()
        self.selected_country.set(countries[0])
        country_menu = tk.OptionMenu(self.bg_image, self.selected_country, *countries)
        country_menu.place(x=300, y=300)

        # Multiline Text Entry for Bio
        bio_label = tk.Label(
            self.bg_image,
            text="Bio:",
            font=("yu gothic ui", 12),
            bg="#272A37",
            fg="#FFFFFF",
            anchor="w",
        )

        bio_label.place(x=200, y=350)
        self.bio_text = tk.Text(
            self.bg_image, width=40, height=5, bg="#272A37", fg="#FFFFFF", bd=3
        )
        self.bio_text.place(x=300, y=350)

        # Check Box
        self.check = tk.IntVar()
        check_box = tk.Checkbutton(
            self.bg_image,
            text="I accept the terms and conditions",
            variable=self.check,
            bg="#272A37",
            font=("yu gothic ui", 12),
            anchor="w",
        )
        check_box.place(x=300, y=450)
        self.show_hide.bind("<Button-1>", self.show_hide_pass)
        self.submit = tk.Button(
            self.bg_image,
            text="Submit",
            width=25,
            command=self.get_user_input,
            bg="#FFFFFF",
            fg="#272A37",
            font=("yu gothic ui", 12),
        )
        self.submit.place(x=300, y=500)

    def create_widgets_SignIn(self):
        self.backgroundImage = tk.PhotoImage(file="assets\\image_1.png")
        self.bg_image = tk.Label(
            self.home_frame, image=self.backgroundImage, bg="#525561"
        )
        self.bg_image.place(x=120, y=28)

        # Email
        email = tk.Label(
            self.bg_image,
            text="Email:",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        email.place(x=200, y=50)
        self.emailVar = tk.StringVar()
        emailEntry = tk.Entry(
            self.bg_image,
            width=40,
            textvariable=self.emailVar,
            bd=3,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        emailEntry.place(x=300, y=50)

        # password
        password = tk.Label(
            self.bg_image,
            text="Password:",
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        password.place(x=200, y=100)
        self.passwordVar = tk.StringVar()
        self.passwordEntry = tk.Entry(
            self.bg_image,
            width=40,
            textvariable=self.passwordVar,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
            bd=3,
            show="*",
        )
        self.passwordEntry.place(x=300, y=100)
        self.show_hide = tk.Button(
            self.bg_image, text="Show", width=5, bg="#272A37", fg="#FFFFFF", bd=0
        )
        self.show_hide.place(x=670, y=150)
        self.show_hide.bind(
            "<Button-1>",
            lambda e: self.show_hide.config(
                text="Hide" if self.show_hide.cget("text") == "Show" else "Show"
            ),
        )
        self.show_hide.bind("<Button-1>", self.show_hide_pass)
        self.submit = tk.Button(
            self.bg_image,
            text="Submit",
            width=25,
            command=self.get_user_input_login,
            bg="#272A37",
            fg="#FFFFFF",
            font=("yu gothic ui", 12),
        )
        self.submit.place(x=300, y=150)

    def show_hide_pass(self, text):
        if self.passwordEntry.cget("show") == "":
            self.passwordEntry.config(show="*")
        else:
            self.passwordEntry.config(show="")
            self.show_hide["text"] = (
                "Hide" if self.show_hide["text"] == "Show" else "Show"
            )

    def get_user_input_login(self):
        global name_value, email_value, password_value, gender_value, status_value, country_value, bio_value, check_value

        email_value = self.emailVar.get()
        password_value = self.passwordVar.get()

        if email_value == info_array[1] and password_value == info_array[2]:
            print("Login Success")
            tk.messagebox.showinfo("Information", "LogedIn Successful!")
            login_successful = True
        else:
            tk.messagebox.showwarning("Warning", "Please Enter Correct Credentials")

    def show_hide_pass(self, text):
        if self.passwordEntry.cget("show") == "":
            self.passwordEntry.config(show="*")
        else:
            self.passwordEntry.config(show="")
            self.show_hide["text"] = (
                "Hide" if self.show_hide["text"] == "Show" else "Show"
            )

    def get_user_input(self):
        global name_value, email_value, password_value, gender_value, status_value, country_value, bio_value, check_value

        name_value = self.nameEntry.get()
        email_value = self.emailVar.get()
        password_value = self.passwordVar.get()
        gender_value = self.gender.get()
        status_value = self.selected_choice.get()
        country_value = self.selected_country.get()
        bio_value = self.bio_text.get("1.0", "end-1c")
        check_value = self.check.get()

        if (
            name_value == ""
            or email_value == ""
            or password_value == ""
            or gender_value == ""
            or status_value == ""
            or country_value == ""
            or bio_value == ""
            or check_value != 1
        ):
            tk.messagebox.showwarning("Warning", "All field andatory!")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_value):
            tk.messagebox.showwarning("Warning", "Enter Valid Email!")

        # Validate password
        elif len(password_value) < 8:
            tk.messagebox.showwarning(
                "Warning", "Password should be at least 8 characters long"
            )

        else:
            # append data to info array
            info_array.append(name_value)
            info_array.append(email_value)
            info_array.append(password_value)
            info_array.append(gender_value)
            info_array.append(status_value)
            info_array.append(country_value)
            info_array.append(bio_value)
            info_array.append(check_value)
            global user
            user = 2
            print(info_array)
            print(user)
            for child in self.home_frame.winfo_children():
                child.destroy()
            self.create_widgets_SignIn()


# Button


# Add  Label to the window


# Now you can print or use these values as per your requirement

if __name__ == "__main__":
    user = 1
    if user == 1:
        app = RegistrationForm()
        app.mainloop()
