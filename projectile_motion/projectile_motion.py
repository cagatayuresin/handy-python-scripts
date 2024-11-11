import math
import turtle
import time

LOGO = r"""
                     ________           ________________                           __________              
___________________________(_)____________  /___(_)__  /____      _______ ___________  /___(_)____________ 
___  __ \_  ___/  __ \____  /_  _ \  ___/  __/_  /__  /_  _ \     __  __ `__ \  __ \  __/_  /_  __ \_  __ \
__  /_/ /  /   / /_/ /___  / /  __/ /__ / /_ _  / _  / /  __/     _  / / / / / /_/ / /_ _  / / /_/ /  / / /
_  .___//_/    \____/___  /  \___/\___/ \__/ /_/  /_/  \___/______/_/ /_/ /_/\____/\__/ /_/  \____//_/ /_/ 
/_/                  /___/                                 _/_____/                                        
"""


def calculate_projectile_motion(velocity, angle, height=0, gravity=9.81):
    g = gravity  # acceleration due to gravity (m/s^2)
    angle_rad = math.radians(angle)

    # Calculate horizontal and vertical components of velocity
    velocity_x = velocity * math.cos(angle_rad)
    velocity_y = velocity * math.sin(angle_rad)

    # Calculate flight time
    if height == 0:
        flight_time = (2 * velocity_y) / g
    else:
        flight_time = (velocity_y + math.sqrt(velocity_y**2 + 2 * g * height)) / g

    # Calculate maximum height
    max_height = height + (velocity_y**2) / (2 * g)

    # Calculate horizontal range
    horizontal_range = velocity_x * flight_time

    # Calculate impact velocity and angle
    impact_velocity_y = velocity_y - g * flight_time
    impact_velocity = math.sqrt(velocity_x**2 + impact_velocity_y**2)
    impact_angle = math.degrees(math.atan2(impact_velocity_y, velocity_x))

    return (
        velocity_x,
        velocity_y,
        flight_time,
        {
            "flight_time": round(flight_time, 2),
            "max_height": round(max_height, 2),
            "horizontal_range": round(horizontal_range, 2),
            "impact_velocity": round(impact_velocity, 2),
            "impact_angle": round(impact_angle, 2),
        },
    )


def print_trajectory(trajectory_data):
    """
    Print the projectile motion summary in a formatted way.

    Parameters:
    trajectory_data (dict): The projectile motion data to be printed.
    """
    print("\nSummary:")
    print(f"Flight time: {trajectory_data['flight_time']} s")
    print(f"Maximum height: {trajectory_data['max_height']} m")
    print(f"Horizontal range: {trajectory_data['horizontal_range']} m")
    print(f"Impact velocity: {trajectory_data['impact_velocity']} m/s")
    print(f"Impact angle: {trajectory_data['impact_angle']} degrees")


def animate_projectile_motion(velocity, angle, height=0, gravity=9.81):
    velocity_x, velocity_y, flight_time, trajectory_data = calculate_projectile_motion(
        velocity, angle, height, gravity
    )
    g = gravity

    # Print trajectory summary before animation
    print_trajectory(trajectory_data)

    # Setup turtle
    screen = turtle.Screen()
    screen.setup(width=1200, height=800)
    screen.title("Projectile Motion Animation")
    screen.setworldcoordinates(-400, -400, 1000, 500)
    screen.tracer(0)
    start_button = turtle.Turtle()
    start_button.hideturtle()
    start_button.penup()
    start_button.goto(0, 200)
    start_button.write(
        "Press 's' to Start Animation", align="center", font=("Arial", 20, "bold")
    )

    def run_animation():
        t = 0
        max_height_reached = False
        projectile = turtle.Turtle()
        projectile.shape("circle")
        projectile.color("red")
        projectile.penup()
        projectile.goto(-300, height - 250)
        projectile.pendown()

        info = turtle.Turtle()
        info.hideturtle()
        info.penup()
        info.goto(-400, -310)
        info.color("blue")
        info.write(
            f"Initial velocity: {velocity} m/s    Angle: {angle} degrees    Height: {height} m    Gravity: {gravity} m/s^2",
            font=("Arial", 15, "normal"),
        )

        max_height_marker = turtle.Turtle()
        max_height_marker.hideturtle()
        max_height_marker.shape("triangle")
        max_height_marker.color("green")

        while t <= flight_time:
            # Update position
            x = velocity_x * t
            y = height + velocity_y * t - 0.5 * g * t**2

            if y < 0:
                break

            # Update projectile position
            projectile.goto(-300 + x, y - 250)

            # Mark the maximum height point
            if not max_height_reached and y >= trajectory_data["max_height"]:
                max_height_marker.penup()
                max_height_marker.goto(-300 + x, y - 250)
                max_height_marker.showturtle()
                max_height_reached = True

            # Update info text
            current_velocity_y = velocity_y - g * t
            current_velocity = math.sqrt(velocity_x**2 + current_velocity_y**2)
            info.clear()
            info.write(
                f"Time: {t:.2f} s    Height: {y:.2f} m    Velocity: {current_velocity:.2f} m/s\n"
                f"Initial velocity: {velocity} m/s    Angle: {angle} degrees    Height: {height} m    Gravity: {gravity} m/s^2",
                font=("Arial", 15, "normal"),
            )

            screen.update()
            time.sleep(0.05)
            t += 0.05

        # Display summary after animation
        info.clear()
        info.write(
            f"Flight time: {trajectory_data['flight_time']} s    "
            f"Max height: {trajectory_data['max_height']} m    "
            f"Range: {trajectory_data['horizontal_range']} m    "
            f"Impact velocity: {trajectory_data['impact_velocity']} m/s    "
            f"Impact angle: {trajectory_data['impact_angle']} degrees",
            font=("Arial", 15, "normal"),
        )

    def start_animation():
        start_button.clear()
        run_animation()

    screen.listen()
    screen.onkey(start_animation, "s")

    ground = turtle.Turtle()
    ground.hideturtle()
    ground.penup()
    ground.goto(-400, -250)
    ground.pendown()
    ground.forward(1400)

    if height > 0:
        height_line = turtle.Turtle()
        height_line.hideturtle()
        height_line.penup()
        height_line.goto(-300, -250)
        height_line.pendown()
        height_line.left(90)
        height_line.forward(height)

    screen.mainloop()


if __name__ == "__main__":
    print(LOGO)
    # Example usage
    initial_velocity = float(input("Enter the initial velocity (m/s): "))
    launch_angle = float(input("Enter the launch angle (degrees): "))
    initial_height = float(
        input("Enter the initial height (m) [optional, default is 0]: ") or 0
    )
    gravity = float(
        input(
            "Enter the acceleration due to gravity (m/s^2) [optional, default is 9.81]: "
        )
        or 9.81
    )

    animate = input("Do you want to see the animation? (y/n) [default: n]: ") or "n"
    if animate.lower() == "y":
        animate_projectile_motion(
            initial_velocity, launch_angle, initial_height, gravity
        )
    else:
        _, _, _, trajectory_data = calculate_projectile_motion(
            initial_velocity, launch_angle, initial_height, gravity
        )
        print_trajectory(trajectory_data)
