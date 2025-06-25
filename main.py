import tkinter as tk
import tkinter.ttk as ttk

from charts.energy_chart import show_energy_chart
from charts.price_chart import show_price_chart
from model.energy_manager import EnergyManager
from gui.add_window import show_add_device_window
from gui.utils import on_price_change, show_load_file_window, show_save_file_window

def main():
    energy_manager = EnergyManager(1.52)
    
    root = tk.Tk()
    root.title("Energy Manager")
    root.geometry("1920x1080")
    
    control_frame = tk.Frame(root)
    control_frame.pack(fill="both")
    
    util_frame = tk.Frame(control_frame)
    util_frame.pack(side=tk.LEFT, expand=True)
    
    chart_frame = tk.Frame(control_frame)
    chart_frame.pack(side=tk.LEFT)
    
    center_frame = tk.Frame(control_frame)
    center_frame.pack(side=tk.LEFT, expand=True)
    
    right_frame = tk.Frame(control_frame)
    right_frame.pack(side=tk.RIGHT, expand=True)
    
    table = ttk.Treeview(root, show="headings")
    table['columns'] = ('ID', 'Name', 'Power', 'Hours', 'Total Energy', 'Price')
    table.column('ID', anchor=tk.CENTER, width=100)
    table.column('Name', anchor=tk.CENTER, width=100)
    table.column('Power', anchor=tk.CENTER, width=100)
    table.column('Hours', anchor=tk.CENTER, width=100)
    table.column('Total Energy', anchor=tk.CENTER, width=100)
    table.column('Price', anchor=tk.CENTER, width=100)
    table.heading('ID', text='ID', anchor=tk.CENTER)
    table.heading('Name', text='Name', anchor=tk.CENTER)
    table.heading('Power', text='Power (W)', anchor=tk.CENTER)
    table.heading('Hours', text='Hours', anchor=tk.CENTER)
    table.heading('Total Energy', text='Total Energy (kWh)', anchor=tk.CENTER)
    table.heading('Price', text='Price (PLN)', anchor=tk.CENTER)
    table.tag_configure('oddrow', background='#E8E8E8')
    table.tag_configure('evenrow', background='#FFFFFF')
    
    price_label = tk.Label(right_frame, text="Price per kWh")
    price_var = tk.StringVar()
    price_var.set("1.52")
    price_var.trace_add('write', lambda *args: on_price_change(energy_manager, price_var, table, total_price_label))
    price = tk.Entry(right_frame, textvariable=price_var, width=20)
    
    total_energy_label = tk.Label(center_frame, text="Total Energy (kWh)")
    total_energy_label.config(text=f"Total Energy: {energy_manager.calculate_total_energy():.2f} kWh")
    total_price_label = tk.Label(center_frame, text="Total Price (PLN)")
    total_price_label.config(text=f"Total Price: {energy_manager.calculate_total_energy():.2f} PLN")

    add_device_button = ttk.Button(util_frame, text="Add Device", command=lambda: show_add_device_window(energy_manager, table, total_energy_label, total_price_label))
    load_file_button = ttk.Button(util_frame, text="Load from CSV", command=lambda: show_load_file_window(energy_manager, table, total_energy_label, total_price_label))
    save_file_button = ttk.Button(util_frame, text="Save to CSV", command=lambda: show_save_file_window(energy_manager))
    create_energy_chart_button = ttk.Button(chart_frame, text="Create energy chart", command=lambda: show_energy_chart(energy_manager))
    create_price_chart_button = ttk.Button(chart_frame, text="Create price chart", command=lambda: show_price_chart(energy_manager))
    
    price_label.pack()
    price.pack()
    total_energy_label.pack()
    total_price_label.pack()
    add_device_button.pack(pady=5)
    load_file_button.pack(pady=5)
    save_file_button.pack(pady=5)
    create_energy_chart_button.pack(pady=5)
    create_price_chart_button.pack(pady=5)
    table.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

if __name__ == "__main__":
    main()
