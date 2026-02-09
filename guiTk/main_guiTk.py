import tkinter as tk
from tkinter import ttk

# Se asume que gui_controls.py define la clase GUIControls
from .gui_controlsTk import GUIControls
from .gui_layoutTk import SpectrometerGUI
from .gui_histograma import SerialHistogram
from processor import DataProcessor
from main import data_queue


class GUIMain(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #PRUEBA
        #print("hola hoal")
        #self.label = tk.Label(self, text="---")
        #self.label.pack()
        #PRUEBA

        self.title("Espectrometro")
        self.geometry("1000x600")
        self.minsize(800, 500)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.processor = DataProcessor()

        self.controls = GUIControls(controller=None)
        
        self.btns = SpectrometerGUI(self.main_frame)
        self.btns.pack(fill=tk.BOTH, expand=True)
        #self.btns.__init__()

        self.histogram = SerialHistogram(self.btns.histogram_frame)

        ##cola 
        self.after(50, self.poll_queue)

    def on_close(self):
        self.destroy()

    ##mira la cola actual
    def poll_queue(self):
        while not data_queue.empty():
            frame = data_queue.get()
            #print(type(frame))
            if isinstance(frame, str):
                datos_procesados = self.processor.process_frame(frame)
                #print(datos_procesados)
                self.histogram.set_data(datos_procesados)

        self.histogram.update()
        self.after(50, self.poll_queue)


    def run(self):
        self.mainloop()
