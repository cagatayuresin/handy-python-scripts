# Unit Converter

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

`unit_converter.py` is a versatile Python script designed to perform unit conversions across various categories, including temperature, length, weight, speed, pressure, and energy. The script offers both command-line argument functionality and an interactive terminal-based interface for ease of use. It’s perfect for students, engineers, and anyone needing quick, accurate unit conversions.

## Features

- **Temperature Conversion**: Converts between Celsius, Fahrenheit, and Kelvin.
- **Length Conversion**: Converts between meters, kilometers, miles, and feet.
- **Weight Conversion**: Converts between grams, kilograms, pounds, and tons.
- **Speed Conversion**: Converts between meters/second, kilometers/hour, and miles/hour.
- **Pressure Conversion**: Converts between Pascal, Bar, and PSI.
- **Energy Conversion**: Converts between Joules, Calories, and Kilowatt-Hour.
- **Flexible Input**: The program can accept conversions through command-line arguments or in an interactive mode, where users can choose categories and units via a navigable menu.

## Requirements

- Python 3.x
- Python packages: `questionary`, `Rich`, `tabulate`

You can install the required packages using the following command:

```bash
pip install questionary rich tabulate
```

## Usage

You can run the script either by providing command-line arguments or by using the interactive mode.

### Example 1: Using Command Line Argument

You can perform conversions directly from the command line using the following format:

```bash
python unit_converter.py --category Temperature --value 100 --from-unit Celsius --to-unit Fahrenheit
```

This will convert 100 degrees Celsius to Fahrenheit and display the result in the terminal.

### Example 2: Using Interactive Input

Simply run the script without arguments, and you will be prompted to select a category, provide a value, and choose the units to convert from and to.

```bash
python unit_converter.py
```

Then you will be asked to provide input via a user-friendly interface:

```plain
 _______         __ __   ______                                __              
|   |   |.-----.|__|  |_|      |.-----.-----.--.--.-----.----.|  |_.-----.----.
|   |   ||     ||  |   _|   ---||  _  |     |  |  |  -__|   _||   _|  -__|   _|
|_______||__|__||__|____|______||_____|__|__|\___/|_____|__|  |____|_____|__|  
? Select the category for conversion: (Use arrow keys)
 » Temperature
   Length
   Weight
   Speed
   Pressure
   Energy
```

### Example Output

Both methods will output a well-formatted table of the result. For example:

```bash
 _______         __ __   ______                                __              
|   |   |.-----.|__|  |_|      |.-----.-----.--.--.-----.----.|  |_.-----.----.
|   |   ||     ||  |   _|   ---||  _  |     |  |  |  -__|   _||   _|  -__|   _|
|_______||__|__||__|____|______||_____|__|__|\___/|_____|__|  |____|_____|__|  
? Select the category for conversion: Length
? Enter the value to be converted: 23
? Convert from: Kilometers
? Convert to: Miles
+-----------------+----------------+
| From            | To             |
+=================+================+
| 23.0 Kilometers | 37.01482 Miles |
+-----------------+----------------+
```

### Available Categories and Units

- **Temperature**: Celsius, Fahrenheit, Kelvin
- **Length**: Meters, Kilometers, Miles, Feet
- **Weight**: Grams, Kilograms, Pounds, Tons
- **Speed**: Meters/Second, Kilometers/Hour, Miles/Hour
- **Pressure**: Pascal, Bar, PSI
- **Energy**: Joules, Calories, Kilowatt-Hour

### Help

For help or more information, use the `-h` or `--help` flag:

```md
python unit_converter.py -h
```

This will display:

```md
usage: unit_converter.py [-h] [--category CATEGORY] [--value VALUE] [--from-unit FROM_UNIT] [--to-unit TO_UNIT]

Unit Converter for various categories.

optional arguments:
  -h, --help            show this help message and exit
  --category CATEGORY   Category of conversion (Temperature, Length, Weight, Speed, Pressure, Energy)
  --value VALUE         Value to be converted
  --from-unit FROM_UNIT Unit to convert from
  --to-unit TO_UNIT     Unit to convert to

Example usage: python unit_converter.py --category Length --value 1000 --from-unit Meters --to-unit Kilometers
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
