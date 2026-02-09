from collections import deque

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SerialHistogram:
    def __init__(self, parent):
        self.data = []

        self.parent = parent

        #self.data = deque(maxlen=256)

        self.fig = Figure(figsize=(4, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)



    def set_data(self, values):
        self.data = values


    def update(self):
        if not self.data:
            return

        self.ax.clear()

        labels = list(self.data.keys())
        values = list(self.data.values())

        colors = [
            "#4B0082",  # 415
            "#0000FF",  # 445
            "#00BFFF",  # 480
            "#00FF00",  # 515
            "#FFFF00",  # 555
            "#FFA500",  # 590
            "#FF4500",  # 630
            "#FF0000",  # 680
            "#CCCCCC",  # CLEAR
            "#8B0000",  # NIR
        ]

        self.ax.bar(labels, values, color=colors)
        self.ax.set_ylim(0, 1.2)
        #self.ax.set_yscale("log")
        self.canvas.draw_idle()
