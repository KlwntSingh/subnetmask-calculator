from Address import Address

class SubnetCalculator():
    def __init__(self, ip_address, subnet_mask):
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        self.network_address = self.calculate_network_address()
        self.broadcast_address = self.calculate_broadcast_address()
        self.min_host_address = self.calculate_min_host_address()
        self.max_host_address = self.calculate_max_host_address()

    def calculate_network_address(self):
        network_address_range = []
        print(self.ip_address.get_address_array())
        for i in range(4):
            network_address_range.append(str(self.ip_address.get_address_array()[i] & self.subnet_mask.get_address_array()[i]))

        return Address(".".join(network_address_range))

    def calculate_broadcast_address(self):
        network_address_arr = self.network_address.get_address_array()
        broadcast_address_arr = []

        for i in range(4):
            if network_address_arr[i] == 0:
                broadcast_address_arr.append('255')
            else:
                broadcast_address_arr.append(str(network_address_arr[i]))

        return Address(".".join(broadcast_address_arr))

    def calculate_min_host_address(self):
        network_address_arr = self.network_address.get_address_array()
        min_host_address_arr = [str(network_address_arr[0]), str(network_address_arr[1]), str(network_address_arr[2]), str(network_address_arr[3] + 1)]

        return Address(".".join(min_host_address_arr))

    def calculate_max_host_address(self):
        broadcast_address_arr = self.broadcast_address.get_address_array()
        max_host_address_arr = [str(broadcast_address_arr[0]), str(broadcast_address_arr[1]), str(broadcast_address_arr[2]), str(broadcast_address_arr[3] - 1 )]
        return Address(".".join(max_host_address_arr))

ip_address = Address("192.168.0.45")
subnet_address = Address('24')
sc = SubnetCalculator(ip_address, subnet_address)

print(sc.broadcast_address)
print(sc.network_address)
print(sc.min_host_address)
print(sc.max_host_address)