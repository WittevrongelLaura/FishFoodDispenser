import time
from RPi import GPIO
from smbus import SMBus


class Waterlevel:

    def __init__(self, i2c=SMBus()):
        # commando: i2cdetect -y 1 --> 0x77
        self.arr_allvalues = None
        self.i2c = i2c
        self.setup()

    def setup(self):
        self.i2c.open(1)

    def __read_data(self, slave_address, register_address, amount):
        arr = self.i2c.read_i2c_block_data(slave_address, register_address, amount)
        
        return arr

    def read_waterlevel(self):
        #bovenste 12 inlezen -> slave address 0x78
        arr_values_12 = self.__read_data(0x78, 0x01, 12)

        #bovenste 8 inlezen -> slave address 0x77
        arr_values_8 = self.__read_data(0x77, 0x01, 8)

        self.arr_allvalues = arr_values_8 + arr_values_12
        #print(self.arr_allvalues)
        # self.get_percentage(self.arr_allvalues)
        return self.get_percentage(self.arr_allvalues)

    @staticmethod
    def get_percentage(arr):
        arr_values = []
        count = 0
        for i in arr:
            #print(i)
            if i == 0:
                arr_values.append(0)
            else:
                arr_values.append(1)
                
        for i in arr_values:
            if i == 1:
                count +=1 

        
        length = len(arr_values)

        percentage = round((count / length) * 100)
        #print(percentage)

        return percentage

    @staticmethod
    def bytes_shifting(msb, lsb):
        # shift msb naar links en plak lsb eraan
        value = msb << 8 | lsb

        # als value negatief is
        if value & 0x80:
            value2 = 2**8  # 2^n n=8
            value -= value2

        return value

    def close_waterlevel(self):
        self.i2c.close()


try:
    waterlevel = Waterlevel()
    while True:
        
        print(waterlevel.read_waterlevel())
        time.sleep(1)

except KeyboardInterrupt as e:
    print(e)
finally:
    waterlevel.close_waterlevel()
