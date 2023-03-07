import freenect
import numpy as np

# Configuración de la profundidad de la cámara
DEPTH_WINSIZE = 640
DEPTH_MAX = 2 ** 12 - 1
DEPTH_MIN = 0

# Esperar a recibir datos de la cámara
def get_depth():
    return freenect.sync_get_depth()[0]

while True:
    # Obtener los datos de profundidad de la cámara
    depth = get_depth()
    # Convertir los datos de profundidad en una matriz de distancia
    depth = depth.astype(np.float32)
    depth[depth == DEPTH_MAX] = np.nan
    depth = depth / DEPTH_MAX * DEPTH_WINSIZE

    # Obtener el esqueleto
    body = freenect.sync_get_skeleton()[0]
    if body is not None and body["tracked"]:
        # Obtener la posición del esqueleto
        position = body["position"]
        # Obtener la distancia del esqueleto
        distance = depth[int(position[1]), int(position[0])]
        print("Posición: ", position, "Distancia: ", distance)

"""
Este código utiliza la función sync_get_depth() de la librería freenect para obtener 
los datos de profundidad de la cámara, y la función sync_get_skeleton() para obtener 
el esqueleto. Luego, convierte los datos de profundidad en una matriz de distancia y 
utiliza la posición del esqueleto para obtener la distancia del mismo. Puedes ajustar 
el esqueleto y la matriz de profundidad según tus necesidades.
"""