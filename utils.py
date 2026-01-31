import json
import time
from datetime import datetime


def now_str():
    """Devuelve fecha y hora actual como string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sleep_ms(ms):
    """Sleep en milisegundos"""
    time.sleep(ms / 1000)


def load_json(path):
    """Carga un archivo JSON"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def save_json(path, data):
    """Guarda datos en un archivo JSON"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def clamp(value, min_value, max_value):
    """Limita un valor entre un mínimo y un máximo"""
    return max(min_value, min(value, max_value))


def log(msg):
    """Log simple por consola con timestamp"""
    print(f"[{now_str()}] {msg}")
