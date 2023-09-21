# import serial
from decorators import *
import time

class ISHT35:
    serial_connection = None
    serialPort = None

    def __init__(self, serialPort):
        self.serialPort = serialPort

    
    def connect(self): # Mock-up functie voor serial connectie:
        # try:
        #     self.serial_connection = serial.Connect(self.serial_port)
        #     return True
        # except serial.SerialException as e:
        #     print(f"Failed to connect: {e}")
        #     return False
        self.serial_connection = True
        print("Connected")
        pass

    def disconnect(self): # Mock-up functie voor serial connectie:
        # if self.serial_connection:
        #     self.serial_connection.disconnect()
        if self.serial_connection:
            self.serial_connection = False
            print ("Disconnected")
        pass
    
    @check_command
    @log_command
    def send_command(self, command): # Mock-up functie voor interface:
        if self.serial_connection:
            print(f'sending command: "{command}"')
            # some send logic
            pass
    
    
    @measure_rate
    def get_humidity(self): # Mock-up functie voor interface:
        # if self.serial_connection:
        #     return self.serial_connection.read()
        if self.serial_connection:
            self.send_command("measure_humidity")
            # return self.serial_connection.read()
            time.sleep(0.025) # simulating read time
            pass

SHT35 = ISHT35("COM1")
SHT35.connect()
print()
SHT35.send_command("configure")
print()
SHT35.send_command("unknown_command")
print()
SHT35.get_humidity()
print()
SHT35.disconnect()
