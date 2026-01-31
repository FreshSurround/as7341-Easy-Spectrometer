# gui_plot.py

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PlotWidget(ttk.Frame):
    """
    Widget de gráfico para visualización en vivo.
    No maneja comunicación: solo recibe datos y los grafica.
    """

    def __init__(self, parent, title="Espectro", xlabel="Frecuencia", ylabel="Amplitud"):
        super().__init__(parent)

        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        self._build_plot()

    def _build_plot(self):
        # Figura matplotlib
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.grid(True)

        # Línea inicial vacía
        self.line, = self.ax.plot([], [], lw=1)

        # Canvas Tk
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_data(self, x, y, autoscale=True):
        """
        Actualiza el gráfico con nuevos datos.

        x: lista / array de eje X
        y: lista / array de eje Y
        autoscale: ajusta límites automáticamente
        """
        if not x or not y:
            return

        self.line.set_data(x, y)

        if autoscale:
            self.ax.relim()
            self.ax.autoscale_view()

        self.canvas.draw_idle()

    def clear(self):
        """Limpia el gráfico"""
        self.line.set_data([], [])
        self.canvas.draw_idle()

    def set_title(self, title):
        self.ax.set_title(title)
        self.canvas.draw_idle()

    def set_labels(self, xlabel=None, ylabel=None):
        if xlabel:
            self.ax.set_xlabel(xlabel)
        if ylabel:
            self.ax.set_ylabel(ylabel)
        self.canvas.draw_idle()
