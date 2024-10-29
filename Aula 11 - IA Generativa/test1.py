import speech_recognition as sr

reconhecedor = sr.Recognizer()

with sr.Microphone() as mic:
    reconhecedor.adjust_for_ambient_noise(mic, duration=2)
    print("Fale algo...")
    audio = reconhecedor.listen(mic)
    print("Reconhecendo áudio...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print(texto)