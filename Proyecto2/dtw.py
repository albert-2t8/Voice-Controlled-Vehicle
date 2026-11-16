import numpy as np
from scipy.spatial import distance as dist

def dista_dtw(matriz_distancia):
    N, M = matriz_distancia.shape
    matriz_costo = np.full((N + 1, M + 1), np.inf)
    matriz_costo[0, 0] = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            cost = matriz_distancia[i - 1, j - 1]
            matriz_costo[i, j] = cost + min(
                matriz_costo[i - 1, j],     
                matriz_costo[i, j - 1],     
                matriz_costo[i - 1, j - 1]  
            )

    return matriz_costo[N, M]


def costoMin(audio_espectro, audio_grabado):
    distancia = dist.cdist(np.log(audio_espectro.T + 1e-8), np.log(audio_grabado.T + 1e-8), 'cosine')
    return round(dista_dtw(distancia), 4)

