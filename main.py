import tkinter as tk
import tkinter.ttk as ttk

from model.energy_manager import EnergyManager
from gui.add_window import show_add_device_window
from gui.utils import on_price_change, show_load_file_window, show_save_file_window

def main():
    energy_manager = EnergyManager(1.52)
    
    root = tk.Tk()
    root.title("Energy Manager")
    root.geometry("1920x1080")
    
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
    table.heading('Power', text='Power (W)', anchor=tk.W)
    table.heading('Hours', text='Hours', anchor=tk.W)
    table.heading('Total Energy', text='Total Energy (kWh)', anchor=tk.W)
    table.heading('Price', text='Price (PLN)', anchor=tk.W)
    table.tag_configure('oddrow', background='#E8E8E8')
    table.tag_configure('evenrow', background='#FFFFFF')
    
    price_label = tk.Label(root, text="Price per kWh")
    price_var = tk.StringVar()
    price_var.set("1.52")
    price_var.trace_add('write', lambda *args: on_price_change(energy_manager, price_var, table))
    price = tk.Entry(root, textvariable=price_var, width=20)
    
    add_device_button = ttk.Button(root, text="Add Device", command=lambda: show_add_device_window(energy_manager, table))
    load_file_button = ttk.Button(root, text="Load from CSV", command=lambda: show_load_file_window(energy_manager, table))
    save_file_button = ttk.Button(root, text="Save to CSV", command=lambda: show_save_file_window(energy_manager))
    
    price_label.pack()
    price.pack()
    add_device_button.pack()
    load_file_button.pack()
    save_file_button.pack()
    table.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

if __name__ == "__main__":
    main()
