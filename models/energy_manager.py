import csv
from functools import reduce
from models.device import Device


class EnergyManager:
    def __init__(self, price):
        self.devices = []
        self.price = price

    def add_device(self, name, power, hours_per_day):
        self.devices.append(Device(name, power, hours_per_day))

    def load_from_csv(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.devices.append(Device(row['name'], row['power'], row['hours_per_day']))

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,
                                    fieldnames=['id', 'name', 'power', 'hours_per_day', 'total_energy', 'price'])
            writer.writeheader()
            for device in self.devices:
                writer.writerow({
                    'id': self.devices.index(device) + 1,
                    'name': device.name,
                    'power': device.power,
                    'hours_per_day': device.hours_per_day,
                    'total_energy': device.calculate_energy(),
                    'price': device.calculate_price(self.price)
                })

    def calculate_total_energy(self):
        return reduce(lambda energy, device: energy + device.calculate_energy(), self.devices, 0)

    def calculate_total_price(self):
        return reduce(lambda price, device: price + device.calculate_price(self.price), self.devices, 0)
