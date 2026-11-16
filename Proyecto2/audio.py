import pyaudio
import numpy as np
import wave
from winsound import *

def grabar_audio(tiempo_grabacion=3, nombre_archivo='voz.wav'):
   formato = pyaudio.paInt16
   canales = 1  #Mono
   tasa_muestreo = 44100
   tamano_bloque = 1024
   audio = pyaudio.PyAudio()
   try:
       flujo_sonido = audio.open(format=formato, channels=canales, rate=tasa_muestreo,
                                 input=True, frames_per_buffer=tamano_bloque)
       print('Inicia la grabación')
       datos_audio = []     
       fragmentos = []
      
       for i in range(0, int(tasa_muestreo / tamano_bloque * tiempo_grabacion)):
           
           datos_bloque = flujo_sonido.read(tamano_bloque)           
           datos_audio.append(datos_bloque)
           fragmentos.append(np.frombuffer(datos_bloque, dtype=np.int16))
           
       senal_audio = np.hstack(fragmentos)  
       if np.max(np.abs(senal_audio)) != 0:  
           senal_normalizada = senal_audio / np.max(np.abs(senal_audio)) * 32767  
           senal_normalizada = senal_normalizada.astype(np.int16)  
           
       print('Termina la Grabación')
       flujo_sonido.stop_stream()
       flujo_sonido.close()
   finally:
       audio.terminate()


   # Guardar el archivo
   archivo_wave = wave.open(nombre_archivo, 'wb')
   archivo_wave.setnchannels(canales)
   archivo_wave.setsampwidth(audio.get_sample_size(formato))
   archivo_wave.setframerate(tasa_muestreo)
   archivo_wave.writeframes(senal_normalizada.tobytes())
   archivo_wave.close()
   # Escuchar audio
   PlaySound(nombre_archivo, SND_FILENAME | SND_ASYNC)

   return senal_normalizada
