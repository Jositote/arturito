import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

while True:
        
    # Seleccionar la tarjeta de sonido como fuente de audio
    with sr.Microphone() as source:
        while True:
            
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

