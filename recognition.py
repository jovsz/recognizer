import speech_recognition
import subprocess



recognizer = speech_recognition.Recognizer()
process = None
saludo = """Hola mundo!"""

def doTask(command):
  global process
  
  if "abrir" in command.lower():
    try:
      process = subprocess.Popen([f"{command.lower().split()[1]}.exe"])
    except:
      print('ejecutable no existe')
      
  elif "cerrar" in command.lower():
    print('entro a cerrar')
    print(process)
    process.terminate()
    
def listenCommand():
  with speech_recognition.Microphone() as source:
    print('listen voice command....')
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    
    try: 
      newCommand = recognizer.recognize_google(audio, language="es-ES")
      print(f"ejecutando comando: {newCommand}")
      doTask(newCommand)
    except speech_recognition.UnknownValueError:
      print(f"No se entendio el commando. ")
    except speech_recognition.RequestError as e:
      print(f"Error al realizar la solicitud del commando {e}")
  
while True:
  listenCommand()
    