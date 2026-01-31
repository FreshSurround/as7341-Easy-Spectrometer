import tkinter as tk
from tkinter import ttk
from .gui_controlsTk import *


class SpectrometerGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self._create_layout()

    def _create_layout(self):
        # --- Frames principales ---
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.center_frame = ttk.Frame(self)
        self.center_frame.pack(expand=True, fill=tk.BOTH)

        self.right_frame = ttk.Frame(self, width=200)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Top: controles principales ---
        self.btn_connect = ttk.Button(self.top_frame, text="Conectar")
        self.btn_start = ttk.Button(self.top_frame, text="Iniciar")
        self.btn_stop = ttk.Button(self.top_frame, text="Detener")

        self.btn_connect.pack(side=tk.LEFT, padx=5, pady=5)
        self.btn_start.pack(side=tk.LEFT , padx=5, pady=5)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # --- Centro: área de gráfico ---
        self.plot_area = ttk.Label(
            self.center_frame,
            text="Área de visualización del espectro",
            anchor="center"
        )
        self.plot_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # --- Derecha: parámetros ---
        ttk.Label(self.right_frame, text="Parámetros").pack(pady=5)

        self.gain_slider = ttk.Scale(self.right_frame, from_=0, to=100)
        ttk.Label(self.right_frame, text="Ganancia").pack()
        self.gain_slider.pack(fill=tk.X, padx=10)

        self.avg_slider = ttk.Scale(self.right_frame, from_=1, to=50)
        ttk.Label(self.right_frame, text="Promediado").pack()
        self.avg_slider.pack(fill=tk.X, padx=10)

        # --- Bottom: estado ---
        self.status_label = ttk.Label(
            self.bottom_frame,
            text="Estado: desconectado",
            anchor="w"
        )
        self.status_label.pack(fill=tk.X, padx=5, pady=3)


if __name__ == "__main__":
    #app = SpectrometerGUI()
    #app.mainloop()
    pass
