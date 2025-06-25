import os
from tkinter import filedialog


def show_load_file_window(energy_manager, table, total_energy_label, total_price_label):
    filepath = filedialog.askopenfilename(initialdir="data", initialfile="devices.csv",
                                          filetypes=[("CSV files", "*.csv")])
    if filepath:
        energy_manager.load_from_csv(filepath)
        reload_table(energy_manager, table)
        reload_total_energy_label(energy_manager, total_energy_label)
        reload_total_price_label(energy_manager, total_price_label)


def show_save_file_window(energy_manager):
    os.makedirs("output", exist_ok=True)
    filepath = filedialog.asksaveasfilename(initialdir="output", initialfile="devices_output.csv",
                                            filetypes=[("CSV files", "*.csv")])
    if filepath:
        energy_manager.save_to_csv(filepath)


def reload_table(energy_manager, table):
    for item in table.get_children():
        table.delete(item)

    devices = energy_manager.devices

    for i in range(len(devices)):
        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
        table.insert(parent='', index='end', values=(
            i + 1,
            devices[i].name,
            devices[i].power,
            devices[i].hours_per_day,
            devices[i].calculate_energy(),
            devices[i].calculate_price(energy_manager.price)
        ), tags=(tag,))


def reload_total_energy_label(energy_manager, total_energy_label):
    energy = energy_manager.calculate_total_energy()
    total_energy_label.config(text=f"Total Energy: {energy:.2f} kWh")


def reload_total_price_label(energy_manager, total_price_label):
    price = energy_manager.calculate_total_price()
    total_price_label.config(text=f"Total Price: {price:.2f} PLN")


def on_price_change(energy_manager, price_var, table, total_price_label):
    try:
        energy_manager.price = float(price_var.get())
        reload_table(energy_manager, table)
        reload_total_price_label(energy_manager, total_price_label)
    except ValueError:
        return None
