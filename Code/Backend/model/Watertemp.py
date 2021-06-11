from subprocess import check_output
class Watertemp:
    def __init__(self, sensor_file_name="/sys/bus/w1/devices/28-3c01d075c50e/w1_slave"):
        self.sensor_file = sensor_file_name

        #eerst onewire sensor opzoeken anders vind het programma het bestand niet op het pad hierboven
        check_output("ls /sys/bus/w1/devices", shell=True)

    def read_temp(self):
        self.sensor_file = open("/sys/bus/w1/devices/28-3c01d075c50e/w1_slave", 'r')

        for line in self.sensor_file:

            if line.find('t') > 0:
                temperatuur = int(line[line.find('t')+2:])/1000
            
        return round(temperatuur)

    def close_file(self):
        self.sensor_file.close()

# temp = Watertemp()
# try:
#     while True:
#         print(temp.read_temp())
            
# except KeyboardInterrupt as e:
#     print(e)
# finally:
#     temp.close_file()