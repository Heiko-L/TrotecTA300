import serial
import struct

data = b'';
block = b'';

print(serial.__version__)

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    timeout = 1)

while True:
    bytesWaiting = ser.inWaiting()
    if(bytesWaiting != 0):
        data = data + ser.read(bytesWaiting)
        start_index = data.find(b'\xAA\xBB')
        if (start_index > 0):
            data = data[start_index:]
        if (len(data) >= 40):
            block = data[0:40]
            data = data[40:]
    if (len(block)>0):
        if (block[38:40].find(sum(block[0:38]).to_bytes(2,byteorder='little')) == 0):
            print("Checksum OK")
        else:
            print("Checksum invalid")
        [upper_display] = struct.unpack('f', block[2:6])
        [lower_display] = struct.unpack('f', block[6:10])
        [velocity] = struct.unpack('f', block[10:14])
        [temp] = struct.unpack('f', block[14:18])
        [flow] = struct.unpack('f', block[18:22])
        [area] = struct.unpack('f', block[22:26])
        print("Upper Display: ", upper_display, " Lower Display: ", lower_display)
        print("Velocity[m/s]: ", velocity, " Temperature[°C]: ", temp, " Flow[m³/min]: ", flow, " Area[m²]: ", area)

# high byte 1000: display unit 0000: unit not displayed
# velocity unit low byte: 1:m/s 2:ft/min 3:km/h 4:MPH 5:knots
#        print(block[26])
# flow unit low byte: 1:CMM 2:CFM
#        print(block[27])
# area unit low byte: 1:m² 2:ft² 3:in²
#        print(block[28])
# temperature unit low byte: 1:°C 2:°F
#        print(block[29])
        print(block[30:38].hex(':'))
        block = b''
