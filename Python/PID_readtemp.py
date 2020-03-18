import minimalmodbus
import sys
import time
path = (sys.argv[1])
instrument = minimalmodbus.Instrument('COM3', 44)  # port name, slave address (in decimal)
instrument.serial.timeout = 0.2
instrument.serial.baudrate = 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
effect = instrument.write_register(3000,1, 0)  #Reset the display
temperature=instrument.read_register(1000, 1, signed=True)  # Registernumber, number of decimals
# print(temperature)
# HeatingOn = (instrument.read_register(1008, 1))  # Heating on of
heatingPower = instrument.read_register(1009, 0)  # Heating power 0-100%
setPoint = instrument.read_register(1001, 1, signed=True)  # setpoint temperature
# print(heatingPower)
# print(setPoint)
# for k in range(0,10):
instrument.write_string(3009, " C", number_of_registers=1)
instrument.write_string(3010, " A", number_of_registers=1)
instrument.write_string(3011, " T", number_of_registers=1)
effect = instrument.write_register(3000, 1, 0)  #Reset the display
path1 = path+"\\temprecord.txt"
file = open(path1, "w")
file.write(str(temperature))
file.close()
path2 = path+"\\temprecord2.txt"
file = open(path2, "a")
file.write(str(temperature)+"\t"+str(heatingPower)+"\t"+str(setPoint)+"\t"+str(time.time())+"\t"+time.asctime()+"\n")
file.close()

