import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

from main import *

def show_add_device_window():
    window = tk.Tk()
    window.geometry("360x250")
    window.title("Add Device")

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    name_label = ttk.Label(window, text="Name:")
    name_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

    name_entry = ttk.Entry(window)
    name_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

    power_label = ttk.Label(window, text="Power:")
    power_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

    power_entry = ttk.Entry(window)
    power_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    hours_label = ttk.Label(window, text="Hours:")
    hours_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

    hours_entry = ttk.Entry(window)
    hours_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

    def on_add():
        name = name_entry.get()
        power = power_entry.get()
        hours = hours_entry.get()
        energy_manager.add_device(name, power, hours)
        window.destroy()

    confirm_button = ttk.Button(window, text="Add", command=lambda: on_add())
    confirm_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    window.mainloop()

def show_load_file_window():
    filepath = tk.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        energy_manager.load_from_csv(filepath)

def show_save_file_window():
    filepath = tk.filedialog.asksaveasfilename()
    if filepath:
        energy_manager.save_to_csv(filepath)

root = tk.Tk()
root.title("Energy Manager")
root.geometry("1920x1080")

price_label = tk.Label(root, text="Price per kWh")
price = tk.Entry(root, width=20)
price.insert(0, "1.52")
price_label.pack()
price.pack()

energy_manager = EnergyManager(float(price.get()))

add_device_button = ttk.Button(root, text="Add Device", command=show_add_device_window)
add_device_button.pack()

load_file_button = ttk.Button(root, text="Load from CSV", command=show_load_file_window)
load_file_button.pack()

save_file_button = ttk.Button(root, text="Save to CSV", command=show_save_file_window)
save_file_button.pack()

table = ttk.Treeview(root)
table['columns'] = ('Name', 'Power', 'Hours', 'Total Energy', 'Price')
table.column('#0', stretch=tk.NO)
table.column('Name', anchor=tk.W, width=100)
table.column('Power', anchor=tk.W, width=100)
table.column('Hours', anchor=tk.W, width=100)
table.column('Total Energy', anchor=tk.W, width=100)
table.column('Price', anchor=tk.W, width=100)

table.heading('#0', text='', anchor=tk.W)
table.heading('Name', text='Name', anchor=tk.W)
table.heading('Power', text='Power', anchor=tk.W)
table.heading('Hours', text='Hours', anchor=tk.W)
table.heading('Total Energy', text='Total Energy', anchor=tk.W)
table.heading('Price', text='Price', anchor=tk.W)

energy_manager.load_from_csv("devices.csv")
data = energy_manager.devices

table.tag_configure('oddrow', background='#E8E8E8')
table.tag_configure('evenrow', background='#FFFFFF')

for i in range(len(data)):
    if i % 2 == 0:
        table.insert(parent='', index=i, values=(data[i].name, data[i].power, data[i].hours_per_day, data[i].calculate_energy, data[i].calculate_price(1.52)), tags=('evenrow',))
    else:
        table.insert(parent='', index=i, values=(data[i].name, data[i].power, data[i].hours_per_day, data[i].calculate_energy, data[i].calculate_price(1.52)), tags=('oddrow',))

table.pack(expand=True, fill=tk.BOTH)

root.mainloop()
