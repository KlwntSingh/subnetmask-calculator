class Address():
    def __init__(self, val):
        if len(val) == 2:
            numberOf255, numberOf1 = divmod(int(val), 8)
            finalVal = []
            for i in range(numberOf255):
                finalVal.append("255")
            last_octet_val = []
            for i in range(8):
                if numberOf1 > 0:
                    last_octet_val.append(1)
                else:
                    last_octet_val.append(0)
                numberOf1 -=1

            for i in range(8):
                last_octet_val[i] = last_octet_val[i] * 2**(7-i)

            last_octet = sum(last_octet_val)

            finalVal.append(str(last_octet))
            val = ".".join(finalVal)

        arr = val.split(".")

        self.firstOctet = int(arr[0])
        self.secondOctet = int(arr[1])
        self.thirdOctet = int(arr[2])
        self.fourthOctet = int(arr[3])

    def get_address_array(self):
        return [self.firstOctet, self.secondOctet, self.thirdOctet, self.fourthOctet]

    def __str__(self):
        return (str(self.firstOctet) +"."+ str(self.secondOctet) +"."+ str(self.thirdOctet) +"."+ str(self.fourthOctet))
