from Address import Address

class SubnetCalculator():
    def __init__(self, ip_address, subnet_mask):
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        self.network_address = self.calculate_network_address()
        self.wild_card = self.calculate_wild_card()

        self.broadcast_address = self.calculate_broadcast_address()
        self.min_host_address = self.calculate_min_host_address()
        self.max_host_address = self.calculate_max_host_address()

    def calculate_wild_card(self):
        subnet_address_arr = self.subnet_mask.get_address_array()
        wildcard_address_arr = []
        for i in subnet_address_arr:
            wildcard_address_arr.append(str(255-i))

        return Address(".".join(wildcard_address_arr))

    def calculate_network_address(self):
        network_address_range = []
        for i in range(4):
            network_address_range.append(str(self.ip_address.get_address_array()[i] & self.subnet_mask.get_address_array()[i]))

        return Address(".".join(network_address_range))

    def calculate_broadcast_address(self):
        network_address_arr = self.network_address.get_address_array()
        wild_card_arr = self.wild_card.get_address_array()

        broadcast_address_arr = []

        for i in range(len(wild_card_arr)):
            broadcast_address_arr.append(str(network_address_arr[i] + wild_card_arr[i]))

        return Address(".".join(broadcast_address_arr))

    def calculate_min_host_address(self):
        network_address_arr = self.network_address.get_address_array()
        wild_card_arr = self.wild_card.get_address_array()
        min_host_address_arr = network_address_arr.copy()

        for i in range(len(wild_card_arr)):
            if wild_card_arr[i] != 0:
                min_host_address_arr[i] += 1
                break

        for i in range(len(min_host_address_arr)):
            min_host_address_arr[i] = str(min_host_address_arr[i])

        return Address(".".join(min_host_address_arr))

    def calculate_max_host_address(self):

        broadcast_address_arr = self.broadcast_address.get_address_array()
        for i in range(3):
            broadcast_address_arr[i] = str(broadcast_address_arr[i])

        broadcast_address_arr[3] = str(broadcast_address_arr[3] -1)

        return Address(".".join(broadcast_address_arr))


ip_address = Address("192.168.0.45")
subnet_address = Address('26')
sc = SubnetCalculator(ip_address, subnet_address)

print(sc.ip_address)
print(sc.subnet_mask)
print(sc.network_address)
print(sc.broadcast_address)
print(sc.min_host_address)
print(sc.max_host_address)