import minimalmodbus
import sys

wantedtemp=float(sys.argv[1])
print(wantedtemp)
instrument = minimalmodbus.Instrument('COM3', 44)  # port name, slave address (in decimal)
instrument.serial.timeout = 0.2
instrument.serial.baudrate = 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
effect = instrument.write_register(1208, wantedtemp, 1, signed=True)  # Registernumber, number of decimals
effect = instrument.write_register(1015, 1, 0)  #1 temperature control ON 0 OFF
# k2=3009
# instrument.write_string(k2, " C", number_of_registers=1)
# instrument.write_string(k2+1, " A", number_of_registers=1)
# instrument.write_string(k2+2, " T", number_of_registers=1)
# effect = instrument.write_register(3000, 1, 0)  #Reset the display

