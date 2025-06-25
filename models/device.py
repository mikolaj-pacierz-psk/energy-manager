class Device:
    def __init__(self, name, power, hours_per_day):
        self.name = name
        self.power = int(power)
        self.hours_per_day = float(hours_per_day)
        assert 0 < self.hours_per_day <= 24, f"Hours must be a float value between 0 and 24"
        assert 0 < self.power <= 10000, f"Power must be a float value between 0 and 10000"

    def calculate_energy(self):
        return round(self.power * self.hours_per_day / 1000, 2)

    def calculate_price(self, price):
        return round(self.calculate_energy() * price, 2)