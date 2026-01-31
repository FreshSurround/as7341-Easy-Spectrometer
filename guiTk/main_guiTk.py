import tkinter as tk
from tkinter import ttk

# Se asume que gui_controls.py define la clase GUIControls
from .gui_controlsTk import GUIControls
from .gui_layoutTk import SpectrometerGUI
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

        # Manejo de cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Frame raíz
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Inicialización de controles
        self.controls = GUIControls(self.main_frame, controller=None)
        self.controls.pack(fill=tk.BOTH, expand=True)
        
        ##Creacion de botones
        self.btns = SpectrometerGUI(self.main_frame)
        self.btns.pack(fill=tk.BOTH, expand=True)
        #self.btns.__init__()

        ##cola 
        self.after(50, self.poll_queue)

    def on_close(self):
        """
        Cierre limpio de la GUI.
        GUIControls NO tiene disconnect(), así que solo
        se destruye la ventana.
        Si en el futuro se agrega un método de cleanup,
        se puede llamar acá.
        """
        try:
            # Ejemplo futuro:
            # if hasattr(self.controls, "stop"):
            #     self.controls.stop()
            pass
        finally:
            self.destroy()

    ##mira la cola actual que actualizo main.py dentro del loop
    def poll_queue(self):
        while not data_queue.empty():
            datos = data_queue.get()
            self.label.config(text=str(datos))  # SOLO acá tocás la GUI
        self.after(50, self.poll_queue)


    def run(self):
        self.mainloop()
