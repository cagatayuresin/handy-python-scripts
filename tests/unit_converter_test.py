import unittest
from unit_converter.unit_converter import (
    convert_temperature,
    convert_length,
    convert_weight,
    convert_speed,
    convert_pressure,
    convert_energy,
)


class TestUnitConverter(unittest.TestCase):

    # Temperature Conversion Tests
    def test_temperature_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert_temperature(0, "Celsius", "Fahrenheit"), 32)
        self.assertAlmostEqual(convert_temperature(100, "Celsius", "Fahrenheit"), 212)

    def test_temperature_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert_temperature(32, "Fahrenheit", "Celsius"), 0)
        self.assertAlmostEqual(convert_temperature(212, "Fahrenheit", "Celsius"), 100)

    def test_temperature_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert_temperature(0, "Celsius", "Kelvin"), 273.15)

    def test_temperature_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert_temperature(273.15, "Kelvin", "Celsius"), 0)

    # Length Conversion Tests
    def test_length_meters_to_kilometers(self):
        self.assertAlmostEqual(convert_length(1000, "Meters", "Kilometers"), 1)

    def test_length_miles_to_meters(self):
        self.assertAlmostEqual(convert_length(1, "Miles", "Meters"), 1609.34)

    def test_length_feet_to_meters(self):
        self.assertAlmostEqual(convert_length(1, "Feet", "Meters"), 0.3048)

    # Weight Conversion Tests
    def test_weight_grams_to_kilograms(self):
        self.assertAlmostEqual(convert_weight(1000, "Grams", "Kilograms"), 1)

    def test_weight_kilograms_to_pounds(self):
        self.assertAlmostEqual(
            convert_weight(1, "Kilograms", "Pounds"), 2.20462, places=5
        )

    def test_weight_pounds_to_grams(self):
        self.assertAlmostEqual(convert_weight(1, "Pounds", "Grams"), 453.592, places=3)

    # Speed Conversion Tests
    def test_speed_meters_per_second_to_kilometers_per_hour(self):
        self.assertAlmostEqual(
            convert_speed(1, "Meters/Second", "Kilometers/Hour"), 3.6, places=5
        )

    def test_speed_kilometers_per_hour_to_miles_per_hour(self):
        self.assertAlmostEqual(
            convert_speed(1, "Kilometers/Hour", "Miles/Hour"), 0.621371, places=5
        )

    # Pressure Conversion Tests
    def test_pressure_pascal_to_bar(self):
        self.assertAlmostEqual(convert_pressure(100000, "Pascal", "Bar"), 1)

    def test_pressure_bar_to_psi(self):
        self.assertAlmostEqual(convert_pressure(1, "Bar", "PSI"), 14.5038, places=4)

    def test_pressure_psi_to_pascal(self):
        self.assertAlmostEqual(convert_pressure(1, "PSI", "Pascal"), 6894.76, places=2)

    # Energy Conversion Tests
    def test_energy_joule_to_calorie(self):
        self.assertAlmostEqual(convert_energy(4.184, "Joule", "Calorie"), 1)

    def test_energy_calorie_to_kilowatt_hour(self):
        self.assertAlmostEqual(
            convert_energy(1_000_000, "Calorie", "Kilowatt-Hour"), 1.162222, places=5
        )

    def test_energy_kilowatt_hour_to_joule(self):
        self.assertAlmostEqual(convert_energy(1, "Kilowatt-Hour", "Joule"), 3.6e6)


if __name__ == "__main__":
    unittest.main()
