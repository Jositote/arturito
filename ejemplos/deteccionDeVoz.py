import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Seleccionar la tarjeta de sonido como fuente de audio
with sr.Microphone() as source:
    print("Di algo...")
    # Calibrar el nivel de ruido de fondo
    r.adjust_for_ambient_noise(source)
    # Escuchar el audio de la tarjeta de sonido
    audio = r.listen(source)

# Intentar reconocer el audio
try:
    # Utilizar el servicio de reconocimiento de voz de Google
    text = r.recognize_google(audio, language='es-ES')
    print(f"Has dicho: {text}")
except sr.UnknownValueError:
    print("No he podido reconocer lo que has dicho")
except sr.RequestError as e:
    print(f"Error al conectarse al servicio de reconocimiento de voz: {e}")

"""
Este código utiliza la biblioteca SpeechRecognition para reconocer palabras a través de una tarjeta de sonido. Primero, se crea un objeto Recognizer y se selecciona la tarjeta de sonido como fuente de audio. Se calibra el nivel de ruido de fondo y se escucha el audio de la tarjeta de sonido utilizando el método listen(). A continuación, se utiliza el servicio de reconocimiento de voz de Google a través del método recognize_google() para intentar reconocer el audio. Si se reconoce correctamente, se muestra el texto reconocido por la consola.

Nota: Este código es solo un ejemplo y puede requerir ajustes dependiendo del sistema de audio que esté utilizando. Además, asegúrese de tener una conexión a Internet estable para utilizar el servicio de reconocimiento de voz de Google.
"""