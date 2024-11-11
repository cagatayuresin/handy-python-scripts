# IP Range Calculator

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

`ip_range_calc.py` is a Python script that calculates and displays detailed network information based on an input IP address and subnet mask in CIDR notation. Additionally, the script now includes error handling, logging, and input flexibility.

## Features

- **Network Address**: Displays the calculated network address.
- **Broadcast Address**: Shows the broadcast address for the given network.
- **Gateway**: Identifies the first usable IP address as the gateway.
- **Usable IP Range**: Provides the range of all usable IP addresses in the network.
- **Total IPs**: Displays the total number of usable IPs in the network.
- **Subnet Mask & Wildcard Mask**: Shows both the subnet mask and its wildcard mask.
- **Binary Masks**: Displays the subnet mask and wildcard mask in binary format.
- **IP Type**: Indicates whether the IP is private or public.
- **IP Class**: Displays the class of the network based on the IP address.
- **Binary, Integer, and Hex IDs**: Displays the network identifier in binary, integer, and hexadecimal formats.
- **in-addr.arpa**: Shows the reverse DNS lookup for the network.
- **Error Handling**: Invalid inputs are caught and the user is prompted to try again without crashing the program.
- **Logging**: All requests and results are logged to a `.txt` file, with the newest logs appearing at the top, including timestamps.
- **Flexible Input**: The program can accept inputs directly as arguments or prompt the user if no argument is provided.

## Requirements

- Python 3.x

## Usage

You can run the script either by passing a network address in CIDR notation as an argument or by allowing the program to prompt you for input.

### Example 1: Using Command Line Argument

```md
python ip_range_calc.py 34.222.54.3/24
```

### Example 2: Using Interactive Input

Simply run the script without arguments, and you will be prompted to enter a network address in CIDR notation.

```md
python ip_range_calc.py
```

Then you will be asked to provide an input like so:

```md
Please enter a network address in CIDR notation (e.g., 192.168.1.0/24):
```

### Example Output

Both methods will output:

```md
  _____ _____    _____                           _____      _            _       _
 |_   _|  __ \  |  __ \                         / ____|    | |          | |     | |
   | | | |__) | | |__) |__ _ _ __   __ _  ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   | | |  ___/  |  _  // _` | '_ \ / _` |/ _ \ | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  _| |_| |      | | \ \ (_| | | | | (_| |  __/ | |___| (_| | | (__| |_| | | (_| | || (_) | |
 |_____|_|      |_|  \_\__,_|_| |_|\__, |\___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
                                    __/ |
                                   |___/

Network Info     : 34.222.54.3/24

Network Address  : 34.222.54.0
Broadcast Address: 34.222.54.255
Gateway          : 34.222.54.1
Usable IP Range  : 34.222.54.1 - 34.222.54.254
Total IPs        : 254
Subnet Mask      : 255.255.255.0
Wildcard Mask    : 0.0.0.255
Subnet Mask Bin  : 11111111111111111111111100000000
Wildcard Bin     : 00000000000000000000000011111111
IP Type          : Public
IP Class         : 34
Binary ID        : 00100010110111100011011000000000
Integer ID       : 584988160
Hex ID           : 0x22de3600
in-addr.arpa     : 0.54.222.34.in-addr.arpa
```

### Logging Feature

Every time the script is run, the result of the calculation, including the timestamp, is logged in a text file (`network_info_log.txt`). The log entries are ordered from newest to oldest, and if the file doesn't exist, it will be automatically created.

Example log file format:

```md
2024-09-28 14:05:15 - Network Info: 34.222.54.3/24
Network Address: 34.222.54.0
Broadcast Address: 34.222.54.255
Gateway: 34.222.54.1
Usable IP Range: 34.222.54.1 - 34.222.54.254
Total IPs: 254
Subnet Mask: 255.255.255.0
Wildcard Mask: 0.0.0.255
Subnet Mask Bin: 11111111111111111111111100000000
Wildcard Bin: 00000000000000000000000011111111
IP Type: Public
IP Class: 34
Binary ID: 00100010110111100011011000000000
Integer ID: 584988160
Hex ID: 0x22de3600
in-addr.arpa: 0.54.222.34.in-addr.arpa
----------------------------------------
```

### Help

For help or more information, use the `-h` or `--help` flag:

```md
python ip_range_calc.py -h
```

This will display:

```md
usage: ip_range_calc.py [-h] [network]

A simple IP address range calculator.

positional arguments:
  network     Network address in CIDR notation (e.g., 192.168.1.0/24).

optional arguments:
  -h, --help  show this help message and exit

Example usage: python ip_range_calc.py 192.168.1.10/24
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
