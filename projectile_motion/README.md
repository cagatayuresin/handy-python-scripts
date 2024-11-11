# Projectile Motion Calculator

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

`projectile_motion.py` is a Python script designed to calculate the trajectory of a projectile given its initial velocity, launch angle, and optional height. The script is ideal for students, engineers, and physics enthusiasts looking to understand projectile motion through key metrics such as flight time, maximum height, horizontal range, impact velocity, and impact angle.

## Features

- **Flight Time Calculation**: Computes the total duration of the projectile's flight.
- **Maximum Height Calculation**: Determines the highest point reached by the projectile.
- **Horizontal Range Calculation**: Calculates the total horizontal distance traveled by the projectile.
- **Impact Velocity and Angle**: Provides the velocity and angle at which the projectile impacts the ground.
- **Flexible Input**: Users can specify initial velocity, angle, height, and gravity for tailored calculations.

## Requirements

- Python 3.x

## Usage

Run the script and input the required values to calculate projectile motion metrics.

### Example

To use the script, simply run it and follow the prompts:

```bash
python projectile_motion.py
```

You will be prompted to provide input values such as initial velocity, launch angle, and optional initial height and gravity:

```plain
                     ________           ________________                           __________              
___________________________(_)____________  /___(_)__  /____      _______ ___________  /___(_)____________ 
___  __ \_  ___/  __ \____  /_  _ \  ___/  __/_  /__  /_  _ \     __  __ `__ \  __ \  __/_  /_  __ \_  __ \
__  /_/ /  /   / /_/ /___  / /  __/ /__ / /_ _  / _  / /  __/     _  / / / / / /_/ / /_ _  / / /_/ /  / / /
_  .___//_/    \____/___  /  \___/\___/ \__/ /_/  /_/  \___/______/_/ /_/ /_/\____/\__/ /_/  \____//_/ /_/ 
/_/                  /___/                                 _/_____/                                        

Enter the initial velocity (m/s): 20
Enter the launch angle (degrees): 45
Enter the initial height (m) [optional, default is 0]: 0
Enter the acceleration due to gravity (m/s^2) [optional, default is 9.81]: 9.81
```

The script will then output a summary of the projectile motion:

```plain
Summary:
Flight time: 2.04 s
Maximum height: 10.2 m
Horizontal range: 28.28 m
Impact velocity: 19.64 m/s
Impact angle: -45.0 degrees
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
