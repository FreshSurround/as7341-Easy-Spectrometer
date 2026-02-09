from serial_comm import SerialManager
from processor import DataProcessor
from crudo import DataManager
from config import BAUDRATE
import time


class Controller:
    def __init__(self, port, baudrate=9600):
        self.serial = SerialManager(port, baudrate)
        self.processor = DataProcessor()
        self.storage = DataManager()

        self.running = False

    def start(self):
        self.serial.connect()
        self.running = True
        print("Controlador iniciado")

        while self.running:
            self.loop()
            time.sleep(0.05)

    def stop(self):
        self.running = False
        self.serial.disconnect()
        print("Controlador detenido")

    def loop(self):
        raw_data = self.serial.read_line()

        if raw_data is None:
            return

        processed = self.processor.process(raw_data)

        if processed is not None:
            self.storage.registrarDatos(processed)

    def send_command(self, command):
        self.serial.write(command)

