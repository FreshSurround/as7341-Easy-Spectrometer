"""
processor.py
Procesamiento de datos del sensor AS7341:
- Limpieza / normalización
- Conversión a estructura espectral
- FFT para análisis en frecuencia (temporal)
"""

import numpy as np
from typing import Dict, List
import json

# Canales típicos del AS7341 (según datasheet)
AS7341_CHANNELS = [
    "F1_415nm", "F2_445nm", "F3_480nm", "F4_515nm",
    "F5_555nm", "F6_590nm", "F7_630nm", "F8_680nm",
    "CLEAR", "NIR"
]

i = [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9]


class DataProcessor:
    """Clase central de procesamiento de datos del AS7341"""

    def __init__(self, normalize: bool = True):
        self.normalize = normalize

    # ----------------------------
    # Procesamiento básico
    # ----------------------------
    def clean_data(self, raw: Dict[str, float]) -> Dict[str, float]:
        """
        Elimina valores negativos y asegura presencia de canales válidos
        """
        cleaned = {}
        for chans,idx in zip(AS7341_CHANNELS, i):
            print(raw)
            print("-------")
            value = raw.get(f"ch{idx}", 0.0)
            print(value)
            print("=============================")
            cleaned[chans] = max(0.0, float(value))

        print(cleaned)
        return cleaned

    def normalize_data(self, data: Dict[str, float]) -> Dict[str, float]:
        """
        Normaliza respecto al valor máximo (0–1)
        """
        max_val = max(data.values()) if data else 1.0
        if max_val == 0:
            return data
        return {k: v / max_val for k, v in data.items()}

    def process_frame(self, raw: Dict[str, float]) -> Dict[str, float]:
        """
        Pipeline completo para una medición del AS7341
        """
        raw_str = raw                       # le pasamos la string que manda arduino
        raw_dict = json.loads(raw_str)      # la formatea a json
        data = self.clean_data(raw_dict)
        if self.normalize:
            data = self.normalize_data(data)
        return data

    # ----------------------------
    # Espectro
    # ----------------------------
    def to_spectrum(self, data: Dict[str, float]) -> np.ndarray:
        """
        Convierte el frame a vector espectral ordenado
        (solo F1–F8)
        """
        bands = [
            "F1_415nm", "F2_445nm", "F3_480nm", "F4_515nm",
            "F5_555nm", "F6_590nm", "F7_630nm", "F8_680nm"
        ]
        return np.array([data.get(b, 0.0) for b in bands], dtype=float)

    # ----------------------------
    # FFT (análisis temporal)
    # ----------------------------
    def fft_signal(self, signal: List[float], fs: float):
        """
        FFT sobre una señal temporal (ej. evolución de un canal)

        signal: lista de muestras
        fs: frecuencia de muestreo (Hz)
        """
        signal = np.asarray(signal, dtype=float)
        n = len(signal)

        fft_vals = np.fft.fft(signal)
        freqs = np.fft.fftfreq(n, d=1/fs)

        magnitude = np.abs(fft_vals) / n
        return freqs[:n // 2], magnitude[:n // 2]

    # ----------------------------
    # Utilidades específicas AS7341
    # ----------------------------
    def lux_proxy(self, data: Dict[str, float]) -> float:
        """
        Estimación simple de luminancia usando canal CLEAR
        (no es lux real)
        """
        return data.get("CLEAR", 0.0)

    def nir_ratio(self, data: Dict[str, float]) -> float:
        """
        Relación NIR / visible (indicador simple de IR)
        """
        visible_sum = sum(
            data.get(ch, 0.0) for ch in AS7341_CHANNELS if "F" in ch
        )
        if visible_sum == 0:
            return 0.0
        return data.get("NIR", 0.0) / visible_sum
