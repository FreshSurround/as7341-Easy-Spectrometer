'''
Un programa rápido para asegurarse de que los datos se esten enviando correctamente
'''

import serial
import time
import json

ser = serial.Serial(
                port="/dev/ttyUSB0",
                baudrate=9600,
                timeout=1
            )

#ser.connect()

try:
    while True:
        linea = ser.readline().decode("utf-8", errors="ignore").strip()
        if not linea.startswith("{"):
            continue

        valores = list(json.loads(linea).values())
        #print(valores)
        print(f"{valores[0]}  {valores[1]}  {valores[2]}  {valores[3]}  {valores[4]}  {valores[5]}  {valores[6]}  {valores[7]}  {valores[8]}  {valores[9]}")


except KeyboardInterrupt:
    ser.close()

