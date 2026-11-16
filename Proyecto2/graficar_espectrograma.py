import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


def espectrograma(archivo):
    muestreo, datos = wavfile.read(archivo)
    datos = datos[:]/ 2**15 
    f, t, espectro = signal.spectrogram(datos, muestreo, nfft=1024, noverlap=900, nperseg=1024)
    return f, t, espectro


archivos = ['adelante_1.wav', 'adelante_2.wav','adelante_3.wav',
'atras_1.wav',    'atras_2.wav',   'atras_3.wav',
'derecha_1.wav', 'derecha_2.wav', 'derecha_3.wav',
'izquierda_1.wav', 'izquierda_2.wav','izquierda_3.wav', 
 'para_1.wav', 'para_2.wav', 'para_3.wav',
'left_1.wav', 'left_2.wav', 'left_3.wav',
'stop_1.wav', 'stop_2.wav', 'stop_3.wav', 
]


for archivo in archivos:
    f, t, espectro = espectrograma(archivo)
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(t, f, 10 * np.log10(espectro), shading='gouraud')
    plt.colorbar(label='Intensidad (dB)')
    plt.title(f"Espectrograma de {archivo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Frecuencia (Hz)")
    plt.tight_layout()
    plt.show()

