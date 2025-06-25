from tkinter import messagebox

import matplotlib.pyplot as plt


def show_price_chart(energy_manager):
    try:
        devices = energy_manager.devices

        if len(devices) == 0:
            raise Exception("No devices found")

        names = [device.name for device in devices]
        costs = [device.calculate_energy() * energy_manager.price for device in devices]

        plt.figure(figsize=(8, 8))
        plt.pie(costs, labels=names, autopct='%1.1f%%', startangle=90)
        plt.title("Full price")
        plt.axis('equal')
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))
