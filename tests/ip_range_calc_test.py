import unittest
from ipaddress import IPv4Network
from ip_range_calc.ip_range_calc import calculate_network_info


class TestNetworkInfo(unittest.TestCase):

    def test_valid_network(self):
        network_input = "192.168.1.0/24"
        expected_network_address = IPv4Network(network_input).network_address

        result = calculate_network_info(network_input)

        self.assertEqual(result["Network Address"], expected_network_address)
        self.assertEqual(result["Total IPs"], 254)  # Based on a /24 subnet
        self.assertEqual(result["IP Type"], "Private")  # 192.168 is a private IP range

    def test_smaller_subnet(self):
        network_input = "10.0.0.0/30"
        expected_network_address = IPv4Network(network_input).network_address

        result = calculate_network_info(network_input)

        self.assertEqual(result["Network Address"], expected_network_address)
        self.assertEqual(result["Total IPs"], 2)  # /30 has only 2 usable IPs
        self.assertEqual(result["IP Type"], "Private")  # 10.0.0.0 is a private IP range

    def test_public_network(self):
        network_input = "8.8.8.0/24"
        expected_network_address = IPv4Network(network_input).network_address

        result = calculate_network_info(network_input)

        self.assertEqual(result["Network Address"], expected_network_address)
        self.assertEqual(result["Total IPs"], 254)
        self.assertEqual(result["IP Type"], "Public")  # 8.8.8.0 is a public IP range

    def test_invalid_network(self):
        with self.assertRaises(ValueError):
            calculate_network_info("invalid_network")

    def test_broadcast_address(self):
        network_input = "192.168.1.0/24"
        result = calculate_network_info(network_input)

        self.assertEqual(
            result["Broadcast Address"], IPv4Network(network_input).broadcast_address
        )

    def test_subnet_mask(self):
        network_input = "192.168.1.0/24"
        result = calculate_network_info(network_input)

        self.assertEqual(str(result["Subnet Mask"]), "255.255.255.0")

    def test_binary_subnet_mask(self):
        network_input = "192.168.1.0/24"
        result = calculate_network_info(network_input)

        self.assertEqual(
            result["Binary Subnet Mask"], "11111111111111111111111100000000"
        )


if __name__ == "__main__":
    unittest.main()
