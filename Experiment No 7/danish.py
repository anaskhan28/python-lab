import tkinter as tk
from tkinter import messagebox

class VehicleForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Information Form")

        # Vehicle Name
        self.vehicle_name_label = tk.Label(root, text="Vehicle Name:")
        self.vehicle_name_label.grid(row=0, column=0, sticky=tk.E)
        self.vehicle_name_entry = tk.Entry(root)
        self.vehicle_name_entry.grid(row=0, column=1)

        # Model
        self.model_label = tk.Label(root, text="Model:")
        self.model_label.grid(row=1, column=0, sticky=tk.E)
        self.model_entry = tk.Entry(root)
        self.model_entry.grid(row=1, column=1)

        # Colour
        self.colour_label = tk.Label(root, text="Colour:")
        self.colour_label.grid(row=2, column=0, sticky=tk.E)
        self.colour_entry = tk.Entry(root)
        self.colour_entry.grid(row=2, column=1)

        # Company
        self.company_label = tk.Label(root, text="Company:")
        self.company_label.grid(row=3, column=0, sticky=tk.E)
        self.company_entry = tk.Entry(root)
        self.company_entry.grid(row=3, column=1)

        # Insurance
        self.insurance_label = tk.Label(root, text="Insurance:")
        self.insurance_label.grid(row=4, column=0, sticky=tk.E)
        self.insurance_var = tk.StringVar()
        self.insurance_checkbox = tk.Checkbutton(root, variable=self.insurance_var, onvalue="Yes", offvalue="No")
        self.insurance_checkbox.grid(row=4, column=1, sticky=tk.W)

        # Accident
        self.accident_label = tk.Label(root, text="Ever had an accident:")
        self.accident_label.grid(row=5, column=0, sticky=tk.E)
        self.accident_var = tk.StringVar()
        self.accident_checkbox = tk.Checkbutton(root, variable=self.accident_var, onvalue="Yes", offvalue="No")
        self.accident_checkbox.grid(row=5, column=1, sticky=tk.W)

        # License
        self.license_label = tk.Label(root, text="License:")
        self.license_label.grid(row=6, column=0, sticky=tk.E)
        self.license_entry = tk.Entry(root)
        self.license_entry.grid(row=6, column=1)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=7, columnspan=2)

    def submit(self):
        vehicle_name = self.vehicle_name_entry.get()
        model = self.model_entry.get()
        colour = self.colour_entry.get()
        company = self.company_entry.get()
        insurance = self.insurance_var.get()
        accident = self.accident_var.get()
        license = self.license_entry.get()

        # Here you can save the data to a file or database, or perform any other desired actions
        messagebox.showinfo("Information Submitted", "Vehicle Information Saved Successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleForm(root)
    root.mainloop()