import tkinter as tk
from tkinter import *
import tkinter.messagebox
import customtkinter
import customtkinter as ctk
import os
import psycopg2  # Instead of import mysql.connector

from PIL import Image
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

conn = psycopg2.connect(
    host="localhost",
    database="studyease",
    user="postgres",
    password="anas@123"
)
cursor = conn.cursor()


customtkinter.set_appearance_mode(
    "light"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

status = "logout"
session_id = 0000


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("StudyEase")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        global image_path
        image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_images"
        )
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
            size=(26, 26),
        )
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "course.png")), size=(450, 350)
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20)
        )
        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "home_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "home_light.png")),
            size=(20, 20),
        )
        self.login_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "login_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "login_light.png")),
            size=(20, 20),
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
            size=(20, 20),
        )
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")),
            size=(20, 20),
        )
        self.bino_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "bino_light.png")), size=(20, 20)
        )

        self.course_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "dash_courses.png")), size=(100, 100)
        )
        self.enrollment_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "enrollment.png")), size=(100, 100)
        )

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=30)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="  StudyEase",
            image=self.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)
        self.home_button = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image,
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        if status == "loginad":
            self.login_button = customtkinter.CTkButton(
                self.sidebar_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text="Dashboard",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=self.login_image,
                anchor="w",
                command=self.login_button_event,
            )
            self.login_button.grid(row=2, column=0, sticky="ew")
        else:
            self.login_button = customtkinter.CTkButton(
                self.sidebar_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text="login",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=self.login_image,
                anchor="w",
                command=self.login_button_event,
            )
            self.login_button.grid(row=2, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Frame 2",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.chat_image,
            anchor="w",
            command=self.frame_2_button_event,
        )
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Frame 3",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.add_user_image,
            anchor="w",
            command=self.frame_3_button_event,
        )
        self.frame_3_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create tabview
        self.login_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.login_frame.grid_columnconfigure(1, weight=1)
        self.tabview = customtkinter.CTkTabview(
            self.login_frame, width=250, corner_radius=30
        )
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Admin")
        self.tabview.add("Student")

        # configure grid of individual tabs
        self.tabview.tab("Admin").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Student").grid_columnconfigure(0, weight=1)

        # Tab Admin
        ad = self.tabview.tab("Admin")
        self.login_label = customtkinter.CTkLabel(
            ad,
            text="StudyEase",
            font=customtkinter.CTkFont(family="Magneto", size=25, weight="bold"),
            text_color="#4287f5",
        )
        self.login_label.grid(row=0, column=0, padx=20, pady=10)
        self.login_label2 = customtkinter.CTkLabel(
            ad,
            text="Admin Login",
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.login_label2.grid(row=1, column=0, padx=20, pady=10)
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.email_admin = customtkinter.CTkEntry(
            ad, width=200, textvariable=self.email_var, placeholder_text="Email"
        )
        self.email_admin.grid(row=2, column=0, padx=20, pady=10)
        self.password_admin = customtkinter.CTkEntry(
            ad,
            show="*",
            width=200,
            textvariable=self.password_var,
            placeholder_text="Password",
        )
        self.password_admin.grid(row=3, column=0, padx=20, pady=10)

        self.login_button = customtkinter.CTkButton(
            ad, text="Login", command=self.loginHandler
        )
        self.login_button.grid(row=4, column=0, padx=20, pady=10)

        # Tab Student
        st = self.tabview.tab("Student")
        self.login_label = customtkinter.CTkLabel(
            st,
            text="StudyEase",
            font=customtkinter.CTkFont(family="Magneto", size=25, weight="bold"),
            text_color="#4287f5",
        )
        self.login_label.grid(row=0, column=0, padx=20, pady=10)
        self.login_label2 = customtkinter.CTkLabel(
            st,
            text="Student Login",
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.login_label2.grid(row=1, column=0, padx=20, pady=10)
        self.email_st = tk.StringVar()
        self.password_st = tk.StringVar()
        self.email_student = customtkinter.CTkEntry(
            st, width=200, placeholder_text="Email", textvariable=self.email_st
        )
        self.email_student.grid(row=2, column=0, padx=20, pady=10)
        self.password_student = customtkinter.CTkEntry(
            st,
            show="*",
            width=200,
            placeholder_text="Password",
            textvariable=self.password_st,
        )
        self.password_student.grid(row=3, column=0, padx=20, pady=10)
        self.login_button = customtkinter.CTkButton(
            st, text="Login", command=self.loginHandler, fg_color="blue"
        )
        self.login_button.grid(row=4, column=0, padx=20, pady=10)

        # create home frame

        self.home_frame = customtkinter.CTkScrollableFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame,
            image=self.large_test_image,
            compound="top",
            text="",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=30, pady=(60, 0))
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame,
            text="Embark on a journey of learning and growth with",
            font=customtkinter.CTkFont(family="Bell MT", size=20, weight="bold"),
        )
        self.home_frame_large_image_label.grid(row=1, column=0, padx=30, pady=(10, 0))
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame,
            text="StudyEase",
            text_color="#4287f5",
            font=customtkinter.CTkFont(family="Magneto", size=25, weight="bold"),
        )
        self.home_frame_large_image_label.grid(row=2, column=0, padx=0, pady=(0, 20))

        self.label_info_1 = customtkinter.CTkLabel(
            self.home_frame,
            text="Our platform provides an effortless way to manage your students and facilitate their learning experience.\n"
            + "From course creation to student enrollment and progress tracking,StudyEasy offers a seamless solution for educators\n"
            + "and learners alike. Join us today and discover the easy path to academic success!",
            justify=tkinter.CENTER,
            font=customtkinter.CTkFont(size=14),
        )
        self.label_info_1.grid(row=3, column=0, padx=(20, 0), pady=(20, 20))

        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame,
            text=" Login to Explore",
            image=self.bino_image,
            compound="left",
            command=self.login_button_event,
        )
        self.home_frame_button_2.grid(row=4, column=0, padx=20, pady=10)

        # admin panel
        self.tab_bg = "white"
        self.admin_frame = customtkinter.CTkScrollableFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        # create tabview
        self.admin_frame.grid_columnconfigure(1, weight=1)
        admin = self.admin_frame
        self.adminTab = customtkinter.CTkTabview(admin, width=250, corner_radius=30)
        self.adminTab.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.adminTab.add("Dashboard")
        self.adminTab.add("Manage")

        # configure grid of individual tabs
        self.adminTab.tab("Dashboard").grid_columnconfigure((0, 1), weight=1)
        self.adminTab.tab("Dashboard").grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.adminTab.tab("Manage").grid_columnconfigure(0, weight=1)

        # Tab Admin
        self.dashboard_admin = self.adminTab.tab("Dashboard")
        self.dashboardAd_label = customtkinter.CTkLabel(
            self.dashboard_admin,
            text="Dashboard",
            text_color="#4287f5",
            font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
        )
        self.dashboardAd_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.update_dashboard_info()

        defines = int(1)

        def clicker(value):
            defines = value
            print(defines)

        # manage panel
        self.adminTab.tab("Manage").grid_columnconfigure(0, weight=1)
        self.manageTab = self.adminTab.tab("Manage")
        # Our button values
        my_values = ["My Courses", "Add Course"]
        # Create the button
        self.my_seg_button = customtkinter.CTkSegmentedButton(
            self.manageTab, values=my_values, command=self.clicker
        )
        self.my_seg_button.set(1)
        self.my_seg_button.grid(row=0, column=0, padx=6, pady=10, sticky="nsew")

        self.manage_frame = customtkinter.CTkFrame(
            self.manageTab, corner_radius=30, fg_color="#8f8f8f"
        )

        self.manage_frame.grid_columnconfigure(0, weight=1)
        self.manage_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.manage_frame_function()

        # Student panel
        self.student_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.student_label = customtkinter.CTkLabel(
            self.student_frame,
            text="Logged in as studnet",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.student_label.grid(row=0, column=0, padx=30, pady=(60, 0))
        self.logout = customtkinter.CTkButton(
            self.student_frame,
            text=" Logout",
            image=self.bino_image,
            compound="left",
            command=self.logout_button,
        )
        self.logout.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )

        # create third frame
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )

        # select default frame
        self.select_frame_by_name("home")

    def update_dashboard_info(self):
        # Course
        self.courseTab = customtkinter.CTkFrame(
            self.dashboard_admin,
            corner_radius=20,
            fg_color=self.tab_bg,
        )
        self.courseTab.grid(row=1, column=0, padx=(10, 10), sticky="nsew")
        self.courseTab.grid_columnconfigure(0, weight=1)
        variable = 0

        course_query = "SELECT * FROM courses WHERE admin_id = %s"
        cursor.execute(course_query, (session_id,))
        result = cursor.fetchall()
        count = len(result)
        coursename = []
        enrollment = []
        for row in result:
            coursename.append(row[1])
            enrollment.append(row[5])

        condition = " OR ".join(
            [f"FIND_IN_SET('{row[0]}', course_id)" for row in result]
        )
        enroll_query = f"SELECT COUNT(*) AS total_rows FROM student WHERE {condition};"
        cursor.execute(enroll_query)
        cresult = cursor.fetchone()
        if cresult is None or cresult[0] is None:
            variable = 0
        else:
            variable = cresult[0]

        self.total_courses = count

        self.course_label = customtkinter.CTkLabel(
            self.courseTab,
            text=f"Total Courses: {count}",
            font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
            text_color="black",
            image=self.course_image,
            compound="top",
        )
        self.course_label.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Enroll
        self.enrollTab = customtkinter.CTkFrame(
            self.dashboard_admin, corner_radius=20, fg_color=self.tab_bg
        )
        self.enrollTab.grid(row=1, column=1, padx=(15, 15), sticky="nsew")
        self.enrollTab.grid_columnconfigure(0, weight=1)

        self.enroll_label = customtkinter.CTkLabel(
            self.enrollTab,
            text=f"Total Enrollment : {variable}",
            font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
            text_color="black",
            image=self.enrollment_image,
            compound="top",
        )
        self.enroll_label.grid(row=0, column=0, padx=6, pady=10, sticky="nsew")
        self.logout_button = customtkinter.CTkButton(
            self.dashboard_admin, text="Logout", command=self.logout_button_event
        )
        self.logout_button.grid(
            row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew"
        )

        # Graph
        self.graphTab = customtkinter.CTkFrame(
            self.dashboard_admin, corner_radius=20, fg_color=self.tab_bg
        )
        self.graphTab.grid(
            row=2, column=0, columnspan=2, padx=(15, 15), pady=(30, 10), sticky="nsew"
        )

        # Sample data
        print(coursename)
        print(enrollment)
        courses = coursename
        enrollments = enrollment

        # Add a graph showing enrollment in courses
        fig = plt.Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.bar(courses, enrollments, color="skyblue")
        ax.set_xlabel("Courses")
        ax.set_ylabel("Enrollment")
        ax.set_title("Enrollment in Courses")

        canvas = FigureCanvasTkAgg(fig, self.graphTab)
        canvas.draw()
        canvas.get_tk_widget().grid(
            row=len(courses), column=0, padx=10, pady=(5, 30), sticky="w"
        )

        fig, ax = plt.subplots(
            figsize=(5, 3)
        )  # Adjust the figsize as per your requirement
        ax.pie(enrollments, labels=courses, autopct="%1.1f%%", startangle=140)
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
        ax.set_title("Enrollment in Courses")

        canvas = FigureCanvasTkAgg(fig, self.graphTab)
        canvas.draw()
        canvas.get_tk_widget().grid(
            row=len(courses), column=1, padx=10, pady=30, sticky="e"
        )

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        self.login_button.configure(
            fg_color=("gray75", "gray25") if name == "login" else "transparent"
        )
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent"
        )
        self.frame_3_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_3" else "transparent"
        )

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "login":
            self.login_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.login_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "admin":
            self.admin_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.admin_frame.grid_forget()
        if name == "student":
            self.student_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.student_frame.grid_forget()

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def manage_frame_function(self):
        global session_id

        image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_images/course"
        )
        select_query = "SELECT * FROM courses where admin_id = %s"
        cursor.execute(select_query, (session_id,))
        result = cursor.fetchall()

        i = 0

        for row in result:
            course_id = row[0]
            name_course = row[1]

            self.courses = customtkinter.CTkFrame(
                self.manage_frame, corner_radius=30, fg_color="#8f8f8f"
            )
            self.courses.grid(
                row=i,
                column=0,
                columnspan=2,
                padx=(10, 10),
                pady=(10, 10),
                sticky="nsew",
            )
            self.courses.grid_columnconfigure(0, weight=1)

            self.names_course = customtkinter.CTkImage(
                Image.open(os.path.join(image_path, f"{name_course}.png")),
                size=(100, 100),
            )
            self.visit_button = customtkinter.CTkButton(
                self.courses,
                height=40,
                border_width=0,
                text=name_course,
                text_color="#4287f5",
                font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
                fg_color="#3D404B",
                hover_color=("gray70", "gray30"),
                image=self.names_course,
                anchor="center",
                command=lambda id=course_id: self.view_selected_course(id),
                corner_radius=30,
            )
            self.visit_button.grid(
                row=i, padx=5, pady=5, column=0, columnspan=2, sticky="nsew"
            )
            i += 1

    def view_selected_course(self, cid):
        for child in self.manage_frame.winfo_children():
            child.destroy()

        image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_images/course"
        )
        select_query = "SELECT * FROM courses WHERE id = %s"
        data = cid
        cursor.execute(select_query, (data,))
        row = cursor.fetchone()
        print(row)

        student_query = "SELECT * FROM student WHERE FIND_IN_SET(%s, course_id) > 0;"
        students = cursor.execute(student_query, (cid,))
        std = cursor.fetchall()

        cursor.execute(
            "SELECT COUNT(*) AS total_rows FROM student WHERE FIND_IN_SET(%s, course_id) > 0;",
            (cid,),
        )
        cresult = cursor.fetchone()
        total_rows = cresult[0]
        print("Total number of rows:", total_rows)

        self.courses_header = customtkinter.CTkFrame(
            self.manage_frame, corner_radius=30, fg_color="#3D404B"
        )
        self.courses_header.grid(
            row=0,
            column=0,
            padx=(10, 10),
            pady=(10, 10),
            sticky="nsew",
        )

        variable = 55
        names_course_text = row[1]
        names_course = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, f"{names_course_text}.png")),
            size=(100, 100),
        )
        profile = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "round.png")),
            size=(50, 50),
        )
        header_title = customtkinter.CTkLabel(
            self.courses_header,
            text=names_course_text,
            height=40,
            text_color="#4287f5",
            font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
            fg_color="transparent",
            image=names_course,
            anchor="center",
            compound="top",
            width=100,
        )
        header_title.place(x=25, y=15)
        desc_header = ctk.CTkLabel(
            self.courses_header,
            text=row[4],
            text_color="white",
            font=customtkinter.CTkFont(family="Cambria", size=15),
            fg_color="transparent",
        )
        desc_header.place(x=35, y=150)
        enrollment_label = ctk.CTkLabel(
            self.courses_header,
            text=f"Enrollment: {total_rows}",
            text_color="white",
            font=customtkinter.CTkFont(family="Cambria", size=20),
            fg_color="transparent",
        )
        enrollment_label.place(x=700, y=150)
        creation_date = ctk.CTkLabel(
            self.courses_header,
            text="Created On: 15-03-2024",
            text_color="white",
            font=customtkinter.CTkFont(family="Cambria", size=15),
            fg_color="transparent",
        )
        creation_date.place(x=700, y=10)

        self.student = customtkinter.CTkFrame(
            self.manage_frame, corner_radius=30, fg_color="#3D404B"
        )
        self.student.grid(
            row=1,
            column=0,
            padx=(10, 10),
            pady=(10, 10),
            sticky="nsew",
        )

        student_head = customtkinter.CTkLabel(
            self.student,
            text="Student Name:",
            height=40,
            text_color="#4287f5",
            font=customtkinter.CTkFont(family="Cambria", size=20, weight="bold"),
            fg_color="transparent",
            width=100,
        )
        student_head.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        i = 0
        for studentName in std:
            student_profile = customtkinter.CTkLabel(
                self.student,
                text="   ",
                fg_color="transparent",
                image=profile,
                anchor="w",
                compound="left",
            )
            student_profile.grid(row=i + 1, column=0, padx=(10, 10), pady=(10, 10))
            retrive_name = studentName[1]
            first_letter = retrive_name[:1]
            student_profile_letter = customtkinter.CTkLabel(
                student_profile,
                text=first_letter,
                fg_color="#4287f5",
                bg_color="#4287f5",
                font=customtkinter.CTkFont(family="Cambria", size=25),
                text_color="white",
                anchor="w",
            )
            student_profile_letter.place(x=17, y=10)
            student_name = customtkinter.CTkLabel(
                self.student,
                text="   " + retrive_name,
                text_color="white",
                font=customtkinter.CTkFont(family="Cambria", size=20),
                fg_color="transparent",
                anchor="w",
            )
            student_name.grid(row=i + 1, column=1, padx=(10, 10), pady=(10, 10))
            i = i + 1

    def add_course_frame_function(self):
        self.course_name_var = tk.StringVar()
        self.category_var = tk.StringVar()

        self.input_bg = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "email.png")), size=(600, 55)
        )

        self.input_bg_half = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "input_img.png")), size=(280, 55)
        )

        self.input_desc = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "email.png")), size=(600, 70)
        )

        self.submit_button = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "button_1.png")), size=(280, 55)
        )

        self.add_course_form_frame = customtkinter.CTkFrame(
            self.manage_frame,
            corner_radius=20,
            height=500,
            width=750,
            fg_color="#3D404B",
        )

        self.add_course_form_frame.grid(
            row=0,
            padx=(10, 10),
            pady=(10, 10),
        )
        self.Add_label = customtkinter.CTkLabel(
            self.add_course_form_frame,
            text="ADD NEW COURSE",
            text_color="#4287f5",
            font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
        )
        self.Add_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        # COURSENAME
        self.coursename_image = customtkinter.CTkLabel(
            self.add_course_form_frame,
            text="",
            image=self.input_bg,
            compound="top",
            corner_radius=10,
            anchor="center",
        )
        self.coursename_image.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        CourseName_text = customtkinter.CTkLabel(
            self.coursename_image,
            text="Title:",
            font=("yu gothic ui SemiBold", 16 * -1),
            fg_color="#3D404B",
            bg_color="#3D404B",
            text_color="grey",
        )
        CourseName_text.place(x=25, y=5)
        self.firstName_icon = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "course_icon.png")), size=(30, 30)
        )
        firstName_icon_Label = customtkinter.CTkLabel(
            self.coursename_image,
            image=self.firstName_icon,
            bg_color="#3D404B",
            text="",
        )
        firstName_icon_Label.place(x=550, y=15)

        CourseName_entry = customtkinter.CTkEntry(
            self.coursename_image,
            fg_color="#3D404B",
            bg_color="#3D404B",
            border_width=0,
            placeholder_text="Enter Course Name...",
            font=("yu gothic ui SemiBold", 16 * -1),
            width=500,
            height=26,
            text_color="white",
            textvariable=self.course_name_var,
        )
        CourseName_entry.place(x=25, y=26)

        # CATEGORY
        self.category_image = customtkinter.CTkLabel(
            self.add_course_form_frame,
            text="",
            image=self.input_bg,
            compound="top",
            corner_radius=10,
        )
        self.category_image.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        category_text = customtkinter.CTkLabel(
            self.category_image,
            text="Category:",
            font=("yu gothic ui SemiBold", 16 * -1),
            fg_color="#3D404B",
            bg_color="#3D404B",
            text_color="white",
        )
        category_text.place(x=25, y=5)
        self.category_icon = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "category_icon.png")), size=(30, 30)
        )

        self.category_menu = ctk.CTkOptionMenu(
            self.category_image,
            values=[
                "Select Option...",
                "Technology",
                "Marketing",
                "Litrature",
                "Agriculture",
            ],
            button_hover_color="#3D404B",
            bg_color="#3D404B",
            fg_color="#3D404B",
            text_color="grey",
            width=500,
            button_color="#3D404B",
            font=("yu gothic ui SemiBold", 16 * -1),
            variable=self.category_var,
        )
        self.category_menu.place(x=25, y=30)

        category_icon_Label = customtkinter.CTkLabel(
            self.category_image,
            image=self.category_icon,
            bg_color="#3D404B",
            text="",
        )
        category_icon_Label.place(x=550, y=15)

        # STATUS
        self.status_image = customtkinter.CTkLabel(
            self.add_course_form_frame,
            text="",
            image=self.input_bg,
            compound="top",
            corner_radius=10,
        )
        self.status_image.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        status_text = customtkinter.CTkLabel(
            self.status_image,
            text="Status:",
            font=("yu gothic ui SemiBold", 16 * -1),
            fg_color="#3D404B",
            bg_color="#3D404B",
            text_color="white",
        )
        status_text.place(x=22, y=5)
        self.status_icon = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "privacy_icon.png")), size=(30, 30)
        )

        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="Open")

        self.openRadio = ctk.CTkRadioButton(
            self.status_image,
            text="Open",
            variable=self.genderVar,
            value="Open",
            bg_color="#3D404B",
            text_color="white",
            border_color="white",
        )
        self.openRadio.place(x=27, y=32)

        self.HideRadioButton = ctk.CTkRadioButton(
            self.status_image,
            text="Hide",
            variable=self.genderVar,
            value="Hide",
            bg_color="#3D404B",
            font=("yu gothic ui SemiBold", 16 * -1),
            text_color="grey",
            border_color="grey",
        )
        self.HideRadioButton.place(x=300, y=32)

        status_icon_Label = customtkinter.CTkLabel(
            self.status_image,
            image=self.status_icon,
            bg_color="#3D404B",
            text="",
        )
        status_icon_Label.place(x=547, y=17)

        # DESCRIPTION
        self.desc_image = customtkinter.CTkLabel(
            self.add_course_form_frame,
            text="",
            image=self.input_desc,
            compound="top",
        )
        self.desc_image.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        desc_text = customtkinter.CTkLabel(
            self.desc_image,
            text="Description:",
            font=("yu gothic ui SemiBold", 16 * -1),
            fg_color="#3D404B",
            bg_color="#3D404B",
            text_color="white",
        )
        desc_text.place(x=22, y=5)
        self.desc_icon = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "desc_icon.png")), size=(30, 30)
        )

        self.desc_entry = customtkinter.CTkTextbox(
            self.desc_image,
            fg_color="#3D404B",
            bg_color="#3D404B",
            border_width=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            width=450,
            height=30,
            text_color="grey",
        )
        self.desc_entry.insert("0.0", "Enter Here..")

        self.desc_entry.place(x=25, y=30)

        desc_icon_Label = customtkinter.CTkLabel(
            self.desc_image,
            image=self.desc_icon,
            bg_color="#3D404B",
            text="",
        )
        desc_icon_Label.place(x=547, y=15)

        self.alert_label = ctk.CTkLabel(
            self.add_course_form_frame,
            text="Fills all fields to add course",
            text_color="red",
            font=customtkinter.CTkFont(family="Cambria", size=15),
            fg_color="transparent",
        )
        self.alert_label.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        # SUBMIT BUTTON
        submit_button = ctk.CTkButton(
            self.add_course_form_frame,
            corner_radius=20,
            text="Submit",
            border_width=0,
            cursor="hand2",
            text_color="white",
            font=customtkinter.CTkFont(family="Cambria", size=25, weight="bold"),
            command=self.add_course,
            width=100,
        )
        submit_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

    def add_course(self):
        print("add Called")
        cname = self.course_name_var.get()
        catg = self.category_var.get()
        status = self.genderVar.get()
        desc = self.desc_entry.get("0.0", "end")

        # Check if any value is null
        if not cname or not catg or not status or not desc:
            self.alert_label.configure(
                text="All fields are mandatory", text_color="red"
            )
            return

        # Create the 'courses' table if it doesn't exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL,
            description VARCHAR(300) NOT NULL
            )
            """
        )
        conn.commit()

        # Insert the course data into the 'courses' table
        try:
            cursor.execute(
                "INSERT INTO courses (name, category, status, description,admin_id) VALUES (%s, %s, %s, %s, %s)",
                (cname, catg, status, desc, session_id),
            )
            conn.commit()
            print("Data inserted successfully")
            self.alert_label.configure(
                text="Course added successfully", text_color="green"
            )
        except Exception as e:
            print("Failed to add course:", e)
            self.alert_label.configure(text="Failed to add course", text_color="red")

        # Update the dashboard information
        self.update_dashboard_info()

    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)

    def createText(self):
        checkboxValue = ""

        # .get() is used to get the value of the checkboxes and entryfields

        if self.choice1._check_state and self.choice2._check_state:
            checkboxValue += self.choice1.get() + " and " + self.choice2.get()
        elif self.choice1._check_state:
            checkboxValue += self.choice1.get()
        elif self.choice2._check_state:
            checkboxValue += self.choice2.get()
        else:
            checkboxValue = "none of the available options"

        # Constructing the text variable
        text = f"{self.nameEntry.get()} : \n{self.genderVar.get()} {self.ageEntry.get()} years old and prefers {checkboxValue}\n"
        text += f"{self.genderVar.get()} currently a {self.occupationOptionMenu.get()}"

        return text

    def on_enter(self, event):
        self.courses.configure(fg_color="green")

    def on_leave(self, event):
        self.courses.configure(fg_color="blue")

    def clicker(self, value2):
        if value2 == "My Courses":
            for child in self.manage_frame.winfo_children():
                child.destroy()
            self.manage_frame_function()

        elif value2 == "Add Course":
            for child in self.manage_frame.winfo_children():
                child.destroy()
            self.add_course_frame_function()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog"
        )
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def home_button_event(self):
        self.select_frame_by_name("home")

    def login_button_event(self):
        if status == "loginad":
            self.refresh_admin_frame()
            self.select_frame_by_name("admin")
        elif status == "loginst":
            self.refresh_student_frame()
            self.select_frame_by_name("student")
        else:
            self.select_frame_by_name("login")

    def refresh_admin_frame(self):
        self.update_dashboard_info()
        self.manage_frame_function()

        pass

    def refresh_student_frame(self):
        # Code to refresh the content of the student frame
        # This method should update any data or widgets in the student frame
        pass

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def loginHandler(self):
        global status
        email = self.email_var.get()
        password = self.password_var.get()
        emailstudent = self.email_st.get()
        passstudent = self.password_st.get()
        print(email)
        print(password)

        cursor.execute(
            "SELECT * FROM admin WHERE email = %s AND password = %s", (email, password)
        )
        admin_user = cursor.fetchone()

        cursor.execute(
            "SELECT * FROM student WHERE email = %s AND password = %s",
            (emailstudent, passstudent),
        )
        student_user = cursor.fetchone()

        if admin_user:
            aid = admin_user[0]
            status = "loginad"
            global session_id
            session_id = aid
            if status == "loginad":
                print("successfully logged in!", aid)
                self.dashboard_event = customtkinter.CTkButton(
                    self.sidebar_frame,
                    corner_radius=0,
                    height=40,
                    border_spacing=10,
                    text="Dashboard",
                    fg_color="transparent",
                    text_color=("gray10", "gray90"),
                    hover_color=("gray70", "gray30"),
                    image=self.login_image,
                    anchor="w",
                    command=self.login_button_event,
                )
                self.dashboard_event.grid(row=2, column=0, sticky="ew")
                self.refresh_admin_frame()
                self.select_frame_by_name("admin")

            else:
                tkinter.messagebox.showerror("failed login")

        elif student_user:
            status = "loginst"
            sid = student_user[0]

            if status == "loginst":
                # save the user id to a global variable
                session_id = sid
                print("successfully logged in!")
                self.dashboard_event = customtkinter.CTkButton(
                    self.sidebar_frame,
                    corner_radius=0,
                    height=40,
                    border_spacing=10,
                    text="Dashboard",
                    fg_color="transparent",
                    text_color=("gray10", "gray90"),
                    hover_color=("gray70", "gray30"),
                    image=self.login_image,
                    anchor="w",
                    command=self.login_button_event,
                )
                self.dashboard_event.grid(row=2, column=0, sticky="ew")
                self.select_frame_by_name("student")
            else:
                tkinter.messagebox.showerror(
                    "Login Failed", "Invalid email or password"
                )

    def logout_button_event(self):
        global status, session_id
        status = "logout"
        session_id = 000
        self.login_button = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="login",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.login_image,
            anchor="w",
            command=self.login_button_event,
        )
        self.login_button.grid(row=2, column=0, sticky="ew")
        self.select_frame_by_name("login")


if __name__ == "__main__":
    app = App()
    app.mainloop()
