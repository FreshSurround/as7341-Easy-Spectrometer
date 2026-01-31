from config import SERIAL_PORT, BAUDRATE, READ_INTERVAL
from serial_comm import SerialManager
from processor import DataProcessor
from crudo import DataManager
from queue import Queue
import time

data_queue = Queue()

def main():
    # Inicializaciones
    serial_mgr = SerialManager(SERIAL_PORT, BAUDRATE)
    processor = DataProcessor()
    storage = DataManager()

    serial_mgr.connect()
    print("Sistema iniciado")

    conect_flag = True
    cont = 0

    try:
        while conect_flag is True:
            raw_data = serial_mgr.read_line()
            print(raw_data)
            if raw_data is None:
                print("raw_data is Empty")
                cont=cont+1
                #print(f"cont = {cont}")
                if cont >= 3:
                    conect_flag = False
                    break

            else:
                processed = processor.process_frame(raw_data)
                if processed is None:
                    print("processed_frame is Empty")
                    continue

                storage.registrarDatos(processed)
                data_queue.put(processed)
                time.sleep(READ_INTERVAL)
                #print("todo ok")

            

    except KeyboardInterrupt:
        print("Cerrando sistema...")

    finally:
        serial_mgr.disconnect()


if __name__ == "__main__":
    main()
