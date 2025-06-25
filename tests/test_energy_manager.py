import os
import unittest
from models.energy_manager import EnergyManager


class TestEnergyManager(unittest.TestCase):
    def setUp(self):
        self.energy_manager = EnergyManager(1.52)

    def test_add_device(self):
        self.energy_manager.add_device("Fridge", 100, 24)
        self.assertEqual(len(self.energy_manager.devices), 1)
        self.assertEqual(self.energy_manager.devices[0].name, "Fridge")
        self.assertEqual(self.energy_manager.devices[0].power, 100)
        self.assertEqual(self.energy_manager.devices[0].hours_per_day, 24)

    def test_save_to_csv(self):
        path_output = "./output/test_devices_output.csv"
        self.energy_manager.save_to_csv(path_output)
        self.assertTrue(os.path.exists(path_output))
        os.remove(path_output)

    def test_calculate_total_energy(self):
        self.energy_manager.add_device("Fridge", 100, 10)  
        self.energy_manager.add_device("TV", 200, 5)       
        self.assertEqual(self.energy_manager.calculate_total_energy(), 2)
        
    def test_calculate_total_price(self):
        self.energy_manager.add_device("Fridge", 100, 10)
        self.energy_manager.add_device("TV", 200, 5)
        self.assertEqual(self.energy_manager.calculate_total_price(), 3.04)

if __name__ == '__main__':
    unittest.main()
