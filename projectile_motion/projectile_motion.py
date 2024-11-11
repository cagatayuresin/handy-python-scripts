import math


LOGO = r"""
                     ________           ________________                           __________              
___________________________(_)____________  /___(_)__  /____      _______ ___________  /___(_)____________ 
___  __ \_  ___/  __ \____  /_  _ \  ___/  __/_  /__  /_  _ \     __  __ `__ \  __ \  __/_  /_  __ \_  __ \
__  /_/ /  /   / /_/ /___  / /  __/ /__ / /_ _  / _  / /  __/     _  / / / / / /_/ / /_ _  / / /_/ /  / / /
_  .___//_/    \____/___  /  \___/\___/ \__/ /_/  /_/  \___/______/_/ /_/ /_/\____/\__/ /_/  \____//_/ /_/ 
/_/                  /___/                                 _/_____/                                        
"""


def calculate_projectile_motion(velocity, angle, height=0, gravity=9.81):
    """
    Calculate the projectile motion trajectory given initial velocity, angle, and optional height.

    Parameters:
    velocity (float): Initial velocity in meters per second (m/s)
    angle (float): Launch angle in degrees
    height (float, optional): Initial height in meters (default is 0)
    gravity (float, optional): Acceleration due to gravity in meters per second squared (default is 9.81)

    Returns:
    dict: A dictionary containing flight time, maximum height, horizontal range, impact velocity, and impact angle.
    """
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

    return {
        "flight_time": round(flight_time, 2),
        "max_height": round(max_height, 2),
        "horizontal_range": round(horizontal_range, 2),
        "impact_velocity": round(impact_velocity, 2),
        "impact_angle": round(impact_angle, 2),
    }


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

    trajectory_data = calculate_projectile_motion(
        initial_velocity, launch_angle, initial_height, gravity
    )
    print_trajectory(trajectory_data)
