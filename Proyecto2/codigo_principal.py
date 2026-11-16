import numpy as np
from joblib import Parallel, delayed
import serial
import audio
import dtw
import espectograma


try:
    BT=serial.Serial('COM7', 115200)
    print('Conexión exitosa')
    
    direcciones = [
        'adelante_1.wav', 'adelante_2.wav','adelante_3.wav',
        'atras_1.wav',    'atras_2.wav',   'atras_3.wav',
        'derecha_1.wav', 'derecha_2.wav', 'derecha_3.wav',
        'left_1.wav', 'left_2.wav', 'left_3.wav',
        'stop_1.wav', 'stop_2.wav', 'stop_3.wav'

    ]

    espectrogramas = {audio: espectograma.obtener_espectrograma(audio) for audio in direcciones}


    while True:  
        audio.grabar_audio()
        archivo_grabado = 'voz.wav'
        espectro_grabado = espectograma.obtener_espectrograma(archivo_grabado)
        
        
        costos = Parallel(n_jobs=-1)(delayed(dtw.costoMin)(espectrogramas[num], espectro_grabado) for num in direcciones)
        
        
        posicion_minima = np.argmin(costos)
        print("Posición mínima:", posicion_minima)
        
        
        mapa_direcciones = {
            (0, 1, 2): 'ADELANTE',
            (3, 4, 5): 'ATRAS',
            (6, 7, 8): 'DERECHA',
            (9, 10, 11): 'IZQUIERDA',
            (12, 13, 14): 'PARA'
          
        }
        
        
        for rango, nombre in mapa_direcciones.items():
            if posicion_minima in rango:
                print(f"El número reconocido es: {nombre}")
                if nombre=='ADELANTE':
                    mensaje=('s')
                    BT.write(mensaje.encode('utf-8'))
                    print(mensaje)
                elif nombre=='ATRAS':
                    mensaje=('w')
                    BT.write(mensaje.encode('utf-8'))
                    print(mensaje)
                elif nombre=='DERECHA':
                     mensaje=('a')
                     BT.write(mensaje.encode('utf-8'))
                     print(mensaje)
                elif nombre=='IZQUIERDA':
                     mensaje=('d')
                     BT.write(mensaje.encode('utf-8'))
                     print(mensaje)
                elif nombre=='PARA':
                     mensaje=('q')
                     BT.write(mensaje.encode('utf-8'))
                     print(mensaje)
                
        otra_prueba = input("¿Deseas realizar otra prueba? (y/n): ").strip().lower()
        if otra_prueba != 'y':
            print("Fin del programa")
            break
    
    
except:
    print('Error de conexión')


