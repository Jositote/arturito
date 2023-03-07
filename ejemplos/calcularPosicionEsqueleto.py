import pykinect2
from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Body)

while True:
    # Esperar a recibir datos de la cámara
    if kinect.has_new_body_frame():
        # Obtener el esqueleto
        bodies = kinect.get_last_body_frame()
        if bodies is not None:
            # Seleccionar el primer esqueleto detectado
            body = bodies.bodies[0]
            if body.is_tracked:
                # Obtener la posición del esqueleto
                joints = body.joints
                # Obtener las coordenadas del centro de la cámara
                center = (kinect.color_frame_desc.Width // 2, kinect.color_frame_desc.Height // 2)
                # Obtener la posición del esqueleto respecto al centro de la cámara
                position = (joints[PyKinectV2.JointType_SpineMid].Position.x * center[0],
                            joints[PyKinectV2.JointType_SpineMid].Position.y * center[1])
                # Obtener la distancia del esqueleto al centro de la cámara
                distance = joints[PyKinectV2.JointType_SpineMid].Position.z
                print("Posición: ", position, "Distancia: ", distance)

"""
Este código utiliza la posición del punto medio de la columna vertebral del esqueleto (SpineMid) para calcular su posición y distancia respecto al centro de la cámara. Puedes ajustar esto según tus necesidades. Recuerda que necesitarás tener conectado y configurado correctamente tu dispositivo Kinect y haber instalado la librería pykinect2.
"""