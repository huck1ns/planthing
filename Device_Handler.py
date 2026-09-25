import serial
import time
import threading
import queue
import serial.tools.list_ports

class Device_Handler:
    def __init__(self):
        self.data_queue = queue.Queue()
        self.ser = None
        self.connect()
        self.process_queue()
        self.port = self.find_port()
        self.connection = False
        
    def find_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if 'ch340' in port.description.lower():
                return port
        return ""
        

    def connect(self):
        try: 
            if self.port()=="":
                self.connection == False
                return "Planthing not found."
            else:
                self.ser = serial.Serial(self.port, baudrate =9600, timeout = 1)
                time.sleep(2)  
                self.thread = threading.Thread(target=self.read_serial, daemon = True)
                self.connection = True
        except Exception as e:
            print("Device not found.")
            
        
        
        

    def read_serial(self): 
        try: 
            while self.connection:
                if self.ser.in_waiting > 0:
                    raw_data = self.ser.readline()
                    
                    decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
                    if decoded_data:
                        self.data_queue.put(decoded_data)
        except Exception as e:
            print("\nStopping script...: {e}")
            
            

        finally:
            self.ser.close()
            
    def process_queue(self):
        while not self.data_queue.empty():
            data = self.data_queue.get_no_wait()
            return data
        
test = Device_Handler()
            
            