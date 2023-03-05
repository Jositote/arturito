import cv2
import numpy as np
from primesense import openni2, nite2

# Inicializar los sensores Kinect
openni2.initialize()
nite2.initialize()

# Crear objetos de dispositivo
dev = openni2.Device.open_any()
depth_stream = dev.create_depth_stream()
color_stream = dev.create_color_stream()

# Iniciar streams
depth_stream.start()
color_stream.start()

# Crear objeto de rastreador de usuarios
user_tracker = nite2.UserTracker(dev)

while True:
    # Obtener imágenes de color y profundidad
    color_frame = color_stream.read_frame()
    color_image = np.array(color_frame.get_data())
    depth_frame = depth_stream.read_frame()
    depth_image = np.array(depth_frame.get_data())

    # Obtener los datos de seguimiento del usuario
    user_frame = user_tracker.read_frame()
    users = user_frame.get_users()
    for user in users:
        if user.is_new():
            user_tracker.start_skeleton_tracking(user.id)

        if user.skeleton.state == nite2.SkeletonState.TRACKED:
            # Obtener las posiciones de las articulaciones del esqueleto
            joints = user.skeleton.joints
            joint_positions = {}
            for joint_type in joints:
                joint = joints[joint_type]
                joint_positions[joint_type] = joint.position

            # Hacer algo con las posiciones de las articulaciones del esqueleto
            # ...

    # Mostrar imágenes
    cv2.imshow("Color", color_image)
    cv2.imshow("Depth", depth_image)
    cv2.waitKey(1)

# Detener streams y liberar memoria
user_tracker.destroy()
depth_stream.stop()
color_stream.stop()
nite2.unload()
openni2.unload()
cv2.destroyAllWindows()

"""
Este código utiliza la biblioteca OpenCV para mostrar imágenes y la biblioteca OpenNI para interactuar con los sensores Kinect. El rastreador de usuarios UserTracker se utiliza para identificar y seguir a los usuarios en la imagen, y las posiciones de las articulaciones del esqueleto se pueden obtener a través de las propiedades Skeleton.joints y Joint.position.

Nota: Este código es solo un ejemplo y puede requerir ajustes dependiendo del modelo de Kinect que esté utilizando y de cómo esté conectado a su sistema. Además, siempre tenga cuidado al manipular componentes electrónicos y asegúrese de seguir las precauciones de seguridad adecuadas.
"""