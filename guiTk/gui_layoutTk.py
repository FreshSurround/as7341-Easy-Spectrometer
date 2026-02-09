import tkinter as tk
from tkinter import ttk
from .gui_controlsTk import *


class SpectrometerGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = GUIControls()
        self._create_layout()

    def _create_layout(self):
        
        self.right_frame = ttk.Frame(self, width=200)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.btn_connect = ttk.Button(self.right_frame, text="Conectar")
        self.btn_start = ttk.Button(self.right_frame, text="Iniciar")
        self.btn_stop = ttk.Button(self.right_frame, text="Detener")
        self.btn_disc = ttk.Button(self.right_frame, text="Desconectar")
        
        self.btn_connect.pack(padx=5, pady=5)
        self.btn_start.pack(padx=5, pady=5)
        self.btn_stop.pack(padx=5, pady=5)
        self.btn_disc.pack(padx=5, pady=5)
        
        self.histogram_frame = tk.Frame(self, bg="black")
        self.histogram_frame.pack(fill="both", expand=True)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        ttk.Label(self.right_frame, text="Parámetros").pack(pady=5)

        self.gain_slider = ttk.Scale(self.right_frame, from_=0, to=100)
        ttk.Label(self.right_frame, text="Ganancia").pack()
        self.gain_slider.pack(fill=tk.X, padx=10)

        self.avg_slider = ttk.Scale(self.right_frame, from_=1, to=50)
        ttk.Label(self.right_frame, text="Promediado").pack()
        self.avg_slider.pack(fill=tk.X, padx=10)

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
