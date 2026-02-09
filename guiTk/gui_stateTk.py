from threading import Lock
from typing import Dict, Any


class GUIState:
    def __init__(self):
        self._lock = Lock()

        # Datos del ESP32
        self.data = {
            "ch1": 0.0,
            "ch2": 0.0,
            "ch3": 0.0,
            "timestamp": 0
        }

        # Estado de la GUI
        self.connected = False
        self.running = False
        self.last_error = None

    def update_from_esp32(self, frame: Dict[str, Any]):
        with self._lock:
            for key in self.data:
                if key in frame:
                    self.data[key] = frame[key]

    def set_connected(self, value: bool):
        with self._lock:
            self.connected = value

    def set_running(self, value: bool):
        with self._lock:
            self.running = value

    def set_error(self, error: str | None):
        with self._lock:
            self.last_error = error

    def snapshot(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "data": self.data.copy(),
                "connected": self.connected,
                "running": self.running,
                "last_error": self.last_error
            }
