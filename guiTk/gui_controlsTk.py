"""
gui_controls.py
----------------
Lógica de controles de la GUI.

Responsabilidades:
- Recibir eventos de UI (sliders, botones, toggles)
- Validar y normalizar valores
- Enviar comandos al ControlManager / SerialManager
- Mantener estado local simple de controles
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any
import tkinter as tk
from tkinter import ttk


@dataclass
class ControlState:
    gain: float = 1.0
    offset: float = 0.0
    paused: bool = False
    channel: int = 0
    extra: Dict[str, Any] = None


class GUIControls(tk.Frame):
    def __init__(self, parent, controller):
        """
        controller: instancia de ControlManager (o similar)
        """
        super().__init__(parent)
        self.controller = controller
        self.state = ControlState(extra={})

    # -----------------
    # Utilidades
    # -----------------
    def _clamp(self, value: float, vmin: float, vmax: float) -> float:
        return max(vmin, min(vmax, value))

    # -----------------
    # Handlers públicos
    # -----------------
    def set_gain(self, value: float):
        value = float(value)
        value = self._clamp(value, 0.1, 10.0)
        self.state.gain = value
        self.controller.set_param("gain", value)

    def set_offset(self, value: float):
        value = float(value)
        value = self._clamp(value, -5.0, 5.0)
        self.state.offset = value
        self.controller.set_param("offset", value)

    def toggle_pause(self, paused: bool):
        paused = bool(paused)
        self.state.paused = paused
        self.controller.set_param("paused", paused)

    def select_channel(self, channel: int):
        channel = int(channel)
        if channel < 0:
            channel = 0
        self.state.channel = channel
        self.controller.set_param("channel", channel)

    # -----------------
    # Acciones
    # -----------------
    def request_calibration(self):
        self.controller.send_command({"cmd": "calibrate"})

    def reset_defaults(self):
        self.set_gain(1.0)
        self.set_offset(0.0)
        self.toggle_pause(False)
        self.select_channel(0)

    # -----------------
    # Sincronización
    # -----------------
    def sync_from_device(self, params: Dict[str, Any]):
        """
        Actualiza el estado local a partir de parámetros recibidos
        desde el ESP32.
        """
        if "gain" in params:
            self.state.gain = float(params["gain"])
        if "offset" in params:
            self.state.offset = float(params["offset"])
        if "paused" in params:
            self.state.paused = bool(params["paused"])
        if "channel" in params:
            self.state.channel = int(params["channel"])
