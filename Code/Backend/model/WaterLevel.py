import time
from RPi import GPIO
from smbus import SMBus


class Waterlevel:

    def __init__(self, slave_address=0x78, i2c=SMBus()):
        # commando: i2cdetect -y 1 --> 0x77
        self.slave_address = slave_address
        self.i2c = i2c
        self.setup()

    def setup(self):
        self.i2c.open(1)

    def __read_data(self, register_address, amount):
        arr = self.i2c.read_i2c_block_data(
            self.slave_address, register_address, amount)
        print("read data")
        # print(arr)

        # values = []
        # for i in range(0, amount, 2):
        #     byte = self.bytes_shifting(arr[i], arr[i+1])
        #     values.append(byte)
        # print("bit shifted data")
        return arr

    def read_waterlevel(self):
        values = self.__read_data(0x01, 12)
        return values

    @staticmethod
    def bytes_shifting(msb, lsb):
        # shift msb naar links en plak lsb eraan
        value = msb << 8 | lsb

        # als value negatief is
        if value & 0x80:
            value2 = 2**8  # 2^n n=8
            value -= value2

        return value

    def print_data(self):
        print(self.read_waterlevel())

    def close_waterlevel(self):
        self.i2c.close()


# try:
#     waterlevel = Waterlevel()
#     while True:
#         waterlevel.print_data()
#         print()
#         time.sleep(1)

# except KeyboardInterrupt as e:
#     print(e)
# finally:
#     waterlevel.close_waterlevel()
