import serial
import json
import time


class SerialManager:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)
            return True
        except serial.SerialException as e:
            print(f"Error al abrir el puerto serie: {e}")
            return False

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def is_connected(self):
        return self.ser is not None and self.ser.is_open

    def send(self, message):
        if not self.is_connected():
            return False

        try:
            self.ser.write((message + "\n").encode("utf-8"))
            return True
        except serial.SerialException as e:
            print(f"Error enviando datos: {e}")
            return False

    def read_line(self):
        if not self.is_connected():
            return None

        try:
            line = self.ser.readline().decode("utf-8", errors='ignore').strip()
            if not line:
                return

            if not line.startswith("{"):
                return

            return line if line else None
        except serial.SerialException as e:
            print(f"Error leyendo datos: {e}")
            return None

    def read_json(self):
        line = self.read_line()
        if not line:
            return None

        try:
            return json.loads(line)
        except json.JSONDecodeError:
            return None


    
