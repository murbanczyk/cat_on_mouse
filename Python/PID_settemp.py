import minimalmodbus
import sys
wantedtemp=float(sys.argv[1])
print(wantedtemp)
instrument = minimalmodbus.Instrument('COM3', 44)  # port name, slave address (in decimal)
instrument.serial.timeout = 2
instrument.serial.baudrate = 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
effect = instrument.write_register(1200, wantedtemp, 1, signed=True)  # Registernumber, number of decimals
effect = instrument.write_register(1208, 1, 0)  #1 temperature control ON 0 OFF

