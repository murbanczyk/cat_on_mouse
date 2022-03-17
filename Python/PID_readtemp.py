
import minimalmodbus
import sys
import time
path = (sys.argv[1])
instrument = minimalmodbus.Instrument('COM3', 44)  # port name, slave address (in decimal)
instrument.serial.timeout = 2
instrument.serial.baudrate = 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
temperature = instrument.read_register(1000, 1, signed=True)  # Registernumber, number of decimals
heatingPower = instrument.read_register(1212, 0)  # Heating power 0-100%
setPoint = instrument.read_register(1200, 1, signed=True)  # setpoint temperature
path1 = path+"\\temprecord.txt"
file = open(path1, "w")
file.write(str(temperature))
file.close()
path2 = path+"\\temprecord2.txt"
file = open(path2, "a")
file.write(str(temperature)+"\t"+str(heatingPower)+"\t"+str(setPoint)+"\t"+str(time.time())+"\t"+time.asctime()+"\n")
file.close()