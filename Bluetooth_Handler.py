import serial
import time
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

target_port = None

for port in ports:
    print (port.description)
    if "HC-05" in port.description:
        target_port = port.device
        break

if target_port:
    print("Connecting to "+target_port)
    
    ser = serial.Serial(
        port=target_port,     
        baudrate=38400,
        timeout=1         
    )
        
    while True:
        data = ser.readline()
        if data:
                print(data.decode('utf-8'))