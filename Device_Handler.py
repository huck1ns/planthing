import serial
import time
import threading
import queue
import serial.tools.list_ports

class Device_Handler:
    def __init__(self):
        self.data_queue = queue.Queue()
        self.connection = False
        self.ser = None
        self.port = None
        self.thread = None
        self.connect()
        
        
    def find_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if 'ch340' in port.description.lower():
                return port.device
        return None
    
    def connect(self):
        self.disconnect()
        self.port = self.find_port()
        if self.port is None:
                        self.connection = False
                        print ("Planthing not found.")
                        return False
        try: 
            self.ser = serial.Serial(self.port, baudrate =9600, timeout = 1)
            time.sleep(2) 
            self.ser.reset_input_buffer() 
            self.connection = True
            self.thread = threading.Thread(target=self.read_serial, daemon = True)
            self.thread.start()
            return True

        except serial.SerialException as e:
            print(f"Could not open {self.port}: {e}")
            self.connection = False
            return False
        
    def disconnect(self):
        self.connection = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2)
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.ser = None
        self.thread = None
            
    def checkConnection(self):
        con = self.find_port() is not None
        if con and not self.connection:
            self.connect()
        return con
            
        

    def read_serial(self): 
        ser = self.ser
        try: 
            while self.connection:
                if ser.in_waiting > 0:
                    raw_data = ser.readline()
                    decoded_data = raw_data.decode('utf-8', errors='ignore').strip()
                    if decoded_data:
                        self.data_queue.put(decoded_data)
                else:
                    time.sleep(0.01)
        except (serial.SerialException, OSError) as e:
            print(f"Serial connection lost: {e}")

        finally:
            self.connection = False
            
            
    def process_queue(self):
        latest = None
        while True:
            try:
                latest = self.data_queue.get_nowait()
            except queue.Empty:
                break
        return latest
            