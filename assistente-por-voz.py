import speech_recognition as sr
# pip install SpeechRecognition
# pip install PyAudio
rec = sr.Recognizer()

# print(sr.Microphone().list_microphone_names())
with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)