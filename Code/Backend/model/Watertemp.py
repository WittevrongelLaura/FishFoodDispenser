class Watertemp:
    def __init__(self, sensor_file_name="/sys/bus/w1/devices/28-3c01d075c50e/w1_slave"):
        self.sensor_file = sensor_file_name

    def read_temp(self):
        self.sensor_file = open(self.sensor_file, 'r')

        for line in self.sensor_file:

            if line.find('t') > 0:
                temperatuur = int(line[line.find('t')+2:])/1000
            
        return format(temperatuur, '.2f')

    def close_file(self):
        self.sensor_file.close()

try:
    temp = Watertemp()
    print(temp.read_temp())
            
except KeyboardInterrupt as e:
    print(e)
finally:
    temp.close_file()