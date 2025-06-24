import os
from tkinter import filedialog

def show_load_file_window(energy_manager, table):
    filepath = filedialog.askopenfilename(initialdir="data", initialfile="devices.csv", filetypes=[("CSV files", "*.csv")])
    if filepath:
        energy_manager.load_from_csv(filepath)
        reload_table(energy_manager, table)

def show_save_file_window(energy_manager):
    os.makedirs("output", exist_ok=True)
    filepath = filedialog.asksaveasfilename(initialdir="output", initialfile="devices_output.csv", filetypes=[("CSV files", "*.csv")])
    if filepath:
        energy_manager.save_to_csv(filepath)    

def reload_table(energy_manager, table):
    for item in table.get_children():
        table.delete(item)

    data = energy_manager.devices
    for i in range(len(data)):
        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
        table.insert(parent='', index='end', values=(
            data[i].name,
            data[i].power,
            data[i].hours_per_day,
            data[i].calculate_energy(),
            data[i].calculate_price(energy_manager.price)
        ), tags=(tag,))

def on_price_change(energy_manager, price_var, table):
    try:
        energy_manager.price = float(price_var.get())
        reload_table(energy_manager, table)
    except ValueError:
        return None