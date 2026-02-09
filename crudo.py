import json
import os
from datetime import datetime


class DataManager:
    def __init__(self, data_path="data", buffer_size=100):
        self.data_path = data_path
        self.buffer_size = buffer_size
        self.buffer = []

        os.makedirs(self.data_path, exist_ok=True)

    def registrarDatos(self, dato: dict):
        dato["timestamp"] = datetime.now().isoformat()
        self.bufferizarDatos(dato)

    def leerDatos(self, filename: str):
        path = os.path.join(self.data_path, filename)
        if not os.path.exists(path):
            #si esta vacio el archivo, devuelve una lista vacia
            return []

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)                             #Devuelve una lista de dicts

    def actualizarDatos(self, filename: str, nuevos_datos: list):
        path = os.path.join(self.data_path, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nuevos_datos, f, indent=2)

    def borrarDatos(self, filename: str):
        path = os.path.join(self.data_path, filename)
        if os.path.exists(path):
            os.remove(path)

    def bufferizarDatos(self, dato: dict):
        self.buffer.append(dato)

        if len(self.buffer) >= self.buffer_size:
            self.exportarDatos()

    def exportarDatos(self, filename="mediciones.json"):
        if not self.buffer:
            return

        path = os.path.join(self.data_path, filename)           

        datos_existentes = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                datos_existentes = json.load(f)

        datos_existentes.extend(self.buffer)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(datos_existentes, f, indent=2)

        self.buffer.clear()

    def guardarCalibracion(self, calibracion: dict, filename="calibracion.json"):
        path = os.path.join(self.data_path, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(calibracion, f, indent=2)

    def cargarCalibracion(self, filename="calibracion.json"):
        path = os.path.join(self.data_path, filename)
        if not os.path.exists(path):
            return {}

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

