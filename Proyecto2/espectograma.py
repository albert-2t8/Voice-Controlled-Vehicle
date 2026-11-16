from scipy.io import wavfile
from scipy import signal


def obtener_espectrograma(archivo):
    muestreo, datos = wavfile.read(archivo)
    datos = datos[:]/2**15
    _, _, espectro = signal.spectrogram(datos, muestreo, nfft=1024, noverlap=900, nperseg=1024)
    return espectro

