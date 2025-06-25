from tkinter import messagebox

import matplotlib.pyplot as plt

def show_energy_chart(energy_manager):
    try:
        devices = energy_manager.devices
        
        if len(devices) == 0:
            raise Exception("No devices found")
        
        names = [device.name for device in devices]
        energies = [device.calculate_energy() for device in devices]
    
        plt.figure(figsize=(10, 6))
        plt.bar(names, energies, color='skyblue')
        plt.title("Energy usage (kWh)")
        plt.xlabel("Device")
        plt.ylabel("Energy (kWh)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))