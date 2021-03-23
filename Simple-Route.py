from time import sleep
import serial

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Waits data configuration

usb.write(b"LT E1 RD50 GR0 BL0")    # Turn on led strip in red

usb.write(b"MT0 E1")                # Enables wheel motors

sleep(0.1)

usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")    # Move forward

usb.write(b"MT0 E1 D180 R AT3950 DT3950 V10")   # Move to the right

usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")    # Move forward

usb.write(b"MT0 E1 D180 L AT3950 DT3950 V10")   # Move to the left

sleep(1)

usb.write(b"LT E1 RD50 GR0 BL0")    # Turn off led strip

usb.write(b"MT0 E0")                # Desables wheel motors