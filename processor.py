import numpy as np
from typing import Dict, List
import json

AS7341_CHANNELS = [
    "F1_415nm", "F2_445nm", "F3_480nm", "F4_515nm",
    "F5_555nm", "F6_590nm", "F7_630nm", "F8_680nm",
    "CLEAR", "NIR"
]

i = [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9]


class DataProcessor:
    def __init__(self, normalize: bool = True):
        self.normalize = normalize

    def clean_data(self, raw: Dict[str, float]) -> Dict[str, float]:
        cleaned = {}
        for chans,idx in zip(AS7341_CHANNELS, i):
            print(raw)
            #print("-------")
            value = raw.get(f"ch{idx}", 0.0)
            #print(value)
            #print("=============================")
            cleaned[chans] = max(0.0, float(value))

        #print(cleaned)
        return cleaned

    def normalize_data(self, data: Dict[str, float]) -> Dict[str, float]:
        if not data:
            return data

        values = np.array(list(data.values()))
        # tomamos el percentil 80 como referencia
        ref = np.percentile(values, 80)
        if ref == 0:
            ref = 1.0

        # normalizamos y recortamos entre 0 y 1
        norm_values = np.clip(values / ref, 0, 1)

        return {k: float(v) for k, v in zip(data.keys(), norm_values)}

    
    def process_frame(self, raw: Dict[str, float]) -> Dict[str, float]:

        raw_str = raw                       # le pasamos la string que manda el ESP32
        raw_dict = json.loads(raw_str)      # la formatea a json
        data = self.clean_data(raw_dict)
        if self.normalize:
            data = self.normalize_data(data)
        return data

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


    def fft_signal(self, signal: List[float], fs: float):
        
        signal = np.asarray(signal, dtype=float)
        n = len(signal)

        fft_vals = np.fft.fft(signal)
        freqs = np.fft.fftfreq(n, d=1/fs)

        magnitude = np.abs(fft_vals) / n
        return freqs[:n // 2], magnitude[:n // 2]


    def lux_proxy(self, data: Dict[str, float]) -> float:
        return data.get("CLEAR", 0.0)

    def nir_ratio(self, data: Dict[str, float]) -> float:
        visible_sum = sum(
            data.get(ch, 0.0) for ch in AS7341_CHANNELS if "F" in ch
        )
        if visible_sum == 0:
            return 0.0
        return data.get("NIR", 0.0) / visible_sum

