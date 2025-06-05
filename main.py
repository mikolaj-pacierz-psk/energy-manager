import csv
from functools import reduce

class EnergyManager:
    def __init__(self, price):
        self.devices = []
        self.price = price
        
    def add_device(self, name, power, hours_per_day):
        self.devices.append(Device(name, power, hours_per_day))
    
    def load_from_csv(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.devices.append(Device(row['name'], row['power'], row['hours_per_day']))

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'power', 'hours_per_day', 'total_energy', 'price'])
            writer.writeheader()
            for device in self.devices:
                writer.writerow({
                    'id': self.devices.index(device) + 1,
                    'name': device.name,
                    'power': device.power,
                    'hours_per_day': device.hours_per_day,
                    'total_energy': device.calculate_energy(),
                    'price': device.calculate_price()
                })
                
    def calculate_total_energy(self):
        return reduce(lambda energy, device: energy + device.calculate_energy(), self.devices, 0)

class Device:
    def __init__(self, name, power, hours_per_day):
        self.name = name
        self.power = float(power)
        self.hours_per_day = float(hours_per_day)
        assert 0 <= self.hours_per_day <= 24, f"{name}: hours_per_day must be a float value between 0 and 24"
        assert 0 < self.power <= 10000, f"{name}: power must be a float value between 0 and 10000"

    def calculate_energy(self):
        return self.power * self.hours_per_day / 1000

    def calculate_price(self, price):
        return round(self.calculate_energy() * price, 2)