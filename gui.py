import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Energy Manager")
root.geometry("1920x1080")

def show_add_device_window():
    window = tk.Tk()
    window.geometry("240x500")
    window.title("Add Device")

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
        
    username_label = ttk.Label(window, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)
    
    username_entry = ttk.Entry(window)
    username_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

    password_label = ttk.Label(window, text="Password:")
    password_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
    
    password_entry = ttk.Entry(window,  show="*")
    password_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)
    
    login_button = ttk.Button(window, text="Login")
    login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


    window.mainloop()
    
price_label = tk.Label(root, text="Price per kWh")
    
price = tk.Entry(root, width=20)
price.insert(0, 'Price')

button = ttk.Button(root, text="Add Device", command=show_add_device_window)
button.pack()

root.mainloop()