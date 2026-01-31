# main_general.py
from threading import Thread
from main import main
from guiTk.main_guiTk import GUIMain

def mainG():
    app = GUIMain()

    backend_thread = Thread(
        target=main,
        daemon=True
    )
    backend_thread.start()     #backend en segundo plano

    app.run()


if __name__ == "__main__":
    mainG()
