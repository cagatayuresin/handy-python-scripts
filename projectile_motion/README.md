# Projectile Motion Calculator

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

`projectile_motion.py` is a Python script that calculates and simulates projectile motion based on user inputs such as initial velocity, launch angle, initial height, and gravity. The script can provide a detailed animation of the projectile's trajectory using the Turtle graphics library or simply output the calculated results to the console. It is ideal for students, educators, and anyone interested in learning about the physics of projectile motion.

## Features

- **Customizable Inputs:** Users can specify initial velocity, launch angle, height, and gravity.

- **Animated Simulation:** An interactive Turtle animation displays the projectile's trajectory in real-time.

- **Console Output:** Displays flight time, maximum height, horizontal range, impact velocity, and impact angle in the console.

- **User Interaction:** Provides an option to animate or simply print the results to the console.

- **Pause Before Animation:** The animation only starts upon user input, allowing the user to control when to begin.

- **Maximum Height Marker:** A green marker indicates the maximum height reached by the projectile.

## Requirements

- Python 3.x
- Python packages: `turtle`, `math`, `time`

## Usage

Run the script and follow the prompts to input the initial velocity, launch angle, initial height, and gravity. You will then have the option to view the animation or see the calculated results in the console.

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
Do you want to see the animation? (y/n) [default: n]: y
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

Animation Output:
![Animation](/projectile_motion/docs/img/projectile-animation.gif)

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
