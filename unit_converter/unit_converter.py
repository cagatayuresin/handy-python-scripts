import argparse
import questionary
from rich.console import Console
from tabulate import tabulate

LOGO = r"""
 _______         __ __   ______                                __              
|   |   |.-----.|__|  |_|      |.-----.-----.--.--.-----.----.|  |_.-----.----.
|   |   ||     ||  |   _|   ---||  _  |     |  |  |  -__|   _||   _|  -__|   _|
|_______||__|__||__|____|______||_____|__|__|\___/|_____|__|  |____|_____|__|  
"""

console = Console()


# Conversion functions
def convert_temperature(value, from_unit, to_unit):
    """
    Converts temperature between Celsius, Fahrenheit, and Kelvin.
    """
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5 / 9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value * 9 / 5) - 459.67


def convert_weight(value, from_unit, to_unit):
    """
    Converts weight between grams, kilograms, pounds, and tons.
    """
    weight_units = {"Grams": 1, "Kilograms": 1000, "Pounds": 453.592, "Tons": 1_000_000}
    return value * (weight_units[from_unit] / weight_units[to_unit])


def convert_speed(value, from_unit, to_unit):
    """
    Converts speed between meters/second, kilometers/hour, and miles/hour.
    """
    speed_units = {
        "Meters/Second": 1,
        "Kilometers/Hour": 3.6,  # 1 meter/second = 3.6 kilometers/hour
        "Miles/Hour": 2.23694,  # 1 meter/second = 2.23694 miles/hour
    }

    if from_unit == to_unit:
        return value
    elif from_unit in speed_units and to_unit in speed_units:
        # Dönüşüm katsayıları doğru kullanılıyor
        return value * (speed_units[to_unit] / speed_units[from_unit])
    else:
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")


def convert_pressure(value, from_unit, to_unit):
    """
    Converts pressure between Pascal, Bar, and PSI.
    """
    pressure_units = {"Pascal": 1, "Bar": 100000, "PSI": 6894.76}
    return value * (pressure_units[from_unit] / pressure_units[to_unit])


def convert_energy(value, from_unit, to_unit):
    """
    Converts energy between Joules, Calories, and Kilowatt-Hour.
    """
    energy_units = {"Joule": 1, "Calorie": 4.184, "Kilowatt-Hour": 3.6e6}
    return value * (energy_units[from_unit] / energy_units[to_unit])


def convert_length(value, from_unit, to_unit):
    """
    Converts length between meters, kilometers, miles, and feet.
    """
    length_units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
    return value * (length_units[from_unit] / length_units[to_unit])


# Display results
def display_result(value, from_unit, to_unit, result):
    """
    Nicely formats and displays the conversion result.
    """
    table = [[f"{value} {from_unit}", f"{result} {to_unit}"]]
    console.print(tabulate(table, headers=["From", "To"], tablefmt="grid"))


# Handle conversions
def handle_conversion(category, value, from_unit, to_unit):
    """
    Handles the conversion logic based on the selected category.
    """
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Speed":
        result = convert_speed(value, from_unit, to_unit)
    elif category == "Pressure":
        result = convert_pressure(value, from_unit, to_unit)
    elif category == "Energy":
        result = convert_energy(value, from_unit, to_unit)
    else:
        console.print("Unknown category!", style="bold red")
        return
    display_result(value, from_unit, to_unit, result)


# CLI Interface for flag-based input
def cli_interface():
    """
    Command Line Interface using argparse for flag-based operation.
    """
    parser = argparse.ArgumentParser(description="Unit Converter")

    parser.add_argument(
        "--category",
        help="Category of conversion (Temperature, Length, Weight, Speed, Pressure, Energy)",
        type=str,
    )
    parser.add_argument("--value", help="Value to be converted", type=float)
    parser.add_argument("--from-unit", help="Unit to convert from", type=str)
    parser.add_argument("--to-unit", help="Unit to convert to", type=str)

    args = parser.parse_args()

    if args.category and args.value and args.from_unit and args.to_unit:
        handle_conversion(args.category, args.value, args.from_unit, args.to_unit)
    else:
        interactive_menu()


# Interactive terminal menu
def interactive_menu():
    """
    Interactive menu that uses PyInquirer to create navigable selections for conversion.
    """
    answers = {
        "category": questionary.select(
            "Select the category for conversion:",
            choices=["Temperature", "Length", "Weight", "Speed", "Pressure", "Energy"],
        ).ask(),
        "value": float(questionary.text("Enter the value to be converted:").ask()),
    }

    answers["from_unit"] = questionary.select(
        "Convert from:", choices=get_unit_choices(answers["category"])
    ).ask()

    answers["to_unit"] = questionary.select(
        "Convert to:", choices=get_unit_choices(answers["category"])
    ).ask()
    value = float(answers["value"])
    handle_conversion(
        answers["category"], value, answers["from_unit"], answers["to_unit"]
    )


def get_unit_choices(category):
    """
    Returns the appropriate units for the selected category.
    """
    if category == "Temperature":
        return ["Celsius", "Fahrenheit", "Kelvin"]
    elif category == "Length":
        return ["Meters", "Kilometers", "Miles", "Feet"]
    elif category == "Weight":
        return ["Grams", "Kilograms", "Pounds", "Tons"]
    elif category == "Speed":
        return ["Meters/Second", "Kilometers/Hour", "Miles/Hour"]
    elif category == "Pressure":
        return ["Pascal", "Bar", "PSI"]
    elif category == "Energy":
        return ["Joule", "Calorie", "Kilowatt-Hour"]


# Entry point
if __name__ == "__main__":
    print(LOGO)
    cli_interface()
