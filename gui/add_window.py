import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from gui.utils import reload_table

def show_add_device_window(energy_manager, table):
    window = tk.Toplevel()
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
        try:
            name = name_entry.get()
            power = power_entry.get()
            hours = hours_entry.get()
            energy_manager.add_device(name, power, hours)
            reload_table(energy_manager, table)
            window.destroy()
        except AssertionError as e:
            messagebox.showerror("Error", str(e), parent=window)
        except ValueError:
            messagebox.showerror("Error", "Power and hours must be a float value", parent=window)

    confirm_button = ttk.Button(window, text="Add", command=on_add)
    confirm_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    window.mainloop()   