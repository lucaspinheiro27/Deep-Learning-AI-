import speech_recognition as sr
import pyttsx3
alexa = pyttsx3.init()
alexa.setProperty('rate', 160)
alexa.setProperty('volume', 1.0)
#for voz in alexa.getProperty('voices'):
#    print(voz)
alexa.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
reconhecedor = sr.Recognizer()

with sr.Microphone() as mic:
    try:
        reconhecedor.adjust_for_ambient_noise(mic, duration=2)
        print("O que deseja calcular?")
        alexa.say("O que deseja calcular?")
        alexa.runAndWait()
        audio = reconhecedor.listen(mic, timeout=10)
        print("Reconhecendo áudio...")
        texto = reconhecedor.recognize_google(audio, language='pt')
        print(texto)
        conta = texto.split(" ")
        print("variável conta ", conta)
        resultado = None
        if conta[1] == '+':
            resultado = float(conta[0]) + float(conta[2])
            print("Resultado=", resultado)
        elif conta[1] == '-':
            resultado = float(conta[0]) - float(conta[2])
            print("Resultado=", resultado)
        elif conta[1] == 'x':
            resultado = float(conta[0]) * float(conta[2])
            print("Resultado=", resultado)
        elif conta[1] == '/' and float(conta[2]) != 0:
            resultado = float(conta[0]) / float(conta[2])
            print("Resultado=", resultado)
        else:
            print("Não entendi.")
        if resultado is not None:
            alexa.say("O resultado é "+str(resultado))
            alexa.runAndWait()
    except:
        print("Ops, aconteceu alguma coisa errada!")
        alexa.say("Ops, aconteceu alguma coisa errada!")
        alexa.runAndWait()