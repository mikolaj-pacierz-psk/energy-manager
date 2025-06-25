import unittest

from models.device import Device


class TestDevice(unittest.TestCase):
    def test_calculate_energy(self):
        device = Device("Fridge", 100, 24)
        self.assertEqual(device.calculate_energy(), 2.4)

    def test_calculate_price(self):
        device = Device("Fridge", 100, 24)
        self.assertEqual(device.calculate_price(1.52), 3.65)

    def test_invalid_hours(self):
        self.assertRaises(AssertionError, Device, "Fridge", 100, 25)

    def test_invalid_power(self):
        self.assertRaises(AssertionError, Device, "Fridge", 10001, 24)


if __name__ == '__main__':
    unittest.main()
