import ipaddress
import argparse
import logging
import os

LOGO = r"""
  _____ _____    _____                           _____      _            _       _             
 |_   _|  __ \  |  __ \                         / ____|    | |          | |     | |            
   | | | |__) | | |__) |__ _ _ __   __ _  ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   | | |  ___/  |  _  // _` | '_ \ / _` |/ _ \ | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  _| |_| |      | | \ \ (_| | | | | (_| |  __/ | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |_____|_|      |_|  \_\__,_|_| |_|\__, |\___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                    __/ |                                                      
                                   |___/                                                       
"""

LOG_FILE = "network_info_log.txt"


def setup_logger():
    """
    Sets up the logger to log to the specified log file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def log_network_info(network, network_info):
    """
    Logs the network information to the log file, ensuring logs are in reverse chronological order.

    Args:
        network (str): The network input in CIDR notation.
        network_info (dict): A dictionary containing network-related information.
    """
    log_message = (
        f"Network Info: {network}\n"
        f"Network Address: {network_info['Network Address']}\n"
        f"Broadcast Address: {network_info['Broadcast Address']}\n"
        f"Gateway: {network_info['Gateway']}\n"
        f"Usable IP Range: {network_info['Usable IP Range']}\n"
        f"Total IPs: {network_info['Total IPs']}\n"
        f"Subnet Mask: {network_info['Subnet Mask']}\n"
        f"Wildcard Mask: {network_info['Wildcard Mask']}\n"
        f"Subnet Mask Bin: {network_info['Binary Subnet Mask']}\n"
        f"Wildcard Bin: {network_info['Binary Wildcard Mask']}\n"
        f"IP Type: {network_info['IP Type']}\n"
        f"IP Class: {network_info['IP Class']}\n"
        f"Binary ID: {network_info['Binary ID']}\n"
        f"Integer ID: {network_info['Integer ID']}\n"
        f"Hex ID: {network_info['Hex ID']}\n"
        f"in-addr.arpa: {network_info['in-addr.arpa']}\n"
        f"{'-'*40}\n"
    )

    # Read existing log content if the file exists
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            existing_logs = file.read()
    else:
        existing_logs = ""

    # Write the new log at the beginning followed by existing logs
    with open(LOG_FILE, "w") as file:
        file.write(log_message + existing_logs)


def calculate_network_info(network_input):
    """
    Calculates various network-related information based on the given network input.

    Args:
        network_input (str): Network address in CIDR notation (e.g., '192.168.1.0/24').

    Returns:
        dict: A dictionary containing various network-related information.
    """
    try:
        network = ipaddress.IPv4Network(network_input.strip(), strict=False)
    except ValueError as e:
        raise ValueError(f"Invalid network address: {e}")

    network_address = network.network_address
    broadcast_address = network.broadcast_address
    gateway = list(network.hosts())[0]
    first_usable_ip = list(network.hosts())[0]
    last_usable_ip = list(network.hosts())[-1]
    total_ips = len(list(network.hosts()))
    subnet_mask = network.netmask
    wildcard_mask = network.hostmask
    binary_subnet_mask = "".join([f"{int(octet):08b}" for octet in subnet_mask.packed])
    binary_wildcard_mask = "".join(
        [f"{int(octet):08b}" for octet in wildcard_mask.packed]
    )
    ip_type = "Private" if network.is_private else "Public"
    ip_class = network.network_address.exploded.split(".")[0]
    binary_id = "".join(
        [f"{int(octet):08b}" for octet in network.network_address.packed]
    )
    integer_id = int(binary_id, 2)
    hex_id = hex(integer_id)
    in_addr_arpa = (
        ".".join(reversed(network_address.exploded.split("."))) + ".in-addr.arpa"
    )

    return {
        "Network Address": network_address,
        "Broadcast Address": broadcast_address,
        "Gateway": gateway,
        "Usable IP Range": f"{first_usable_ip} - {last_usable_ip}",
        "Total IPs": total_ips,
        "Subnet Mask": subnet_mask,
        "Wildcard Mask": wildcard_mask,
        "Binary Subnet Mask": binary_subnet_mask,
        "Binary Wildcard Mask": binary_wildcard_mask,
        "IP Type": ip_type,
        "IP Class": ip_class,
        "Binary ID": binary_id,
        "Integer ID": integer_id,
        "Hex ID": hex_id,
        "in-addr.arpa": in_addr_arpa,
    }


def main():
    """
    Main function to handle argument parsing and input for the IP range calculator.
    It also includes error handling to manage invalid inputs and logging of results.
    """
    setup_logger()

    parser = argparse.ArgumentParser(
        description="A simple IP address range calculator.",
        epilog="Example usage: python ip_range_calc.py 192.168.1.10/24",
    )

    parser.add_argument(
        "network",
        type=str,
        nargs="?",
        help="Network address in CIDR notation (e.g., 192.168.1.0/24).",
    )

    args = parser.parse_args()

    if args.network is None:
        while True:
            try:
                network_input = input(
                    "Please enter a network address in CIDR notation (e.g., 192.168.1.0/24): "
                )
                network_info = calculate_network_info(network_input)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    else:
        try:
            network_info = calculate_network_info(args.network)
        except ValueError as e:
            print(f"Error: {e}. Please restart the program and try again.")
            return

    # Log the network information
    log_network_info(args.network or network_input, network_info)

    print("\n" + LOGO)
    print(f"Network Info     : {args.network or network_input}")
    print("\n")
    print(f"Network Address  : {network_info['Network Address']}")
    print(f"Broadcast Address: {network_info['Broadcast Address']}")
    print(f"Gateway          : {network_info['Gateway']}")
    print(f"Usable IP Range  : {network_info['Usable IP Range']}")
    print(f"Total IPs        : {network_info['Total IPs']}")
    print(f"Subnet Mask      : {network_info['Subnet Mask']}")
    print(f"Wildcard Mask    : {network_info['Wildcard Mask']}")
    print(f"Subnet Mask Bin  : {network_info['Binary Subnet Mask']}")
    print(f"Wildcard Bin     : {network_info['Binary Wildcard Mask']}")
    print(f"IP Type          : {network_info['IP Type']}")
    print(f"IP Class         : {network_info['IP Class']}")
    print(f"Binary ID        : {network_info['Binary ID']}")
    print(f"Integer ID       : {network_info['Integer ID']}")
    print(f"Hex ID           : {network_info['Hex ID']}")
    print(f"in-addr.arpa     : {network_info['in-addr.arpa']}")
    print("\n")


if __name__ == "__main__":
    main()
