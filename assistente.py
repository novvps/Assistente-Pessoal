import pyautogui as pyag
from time import sleep
import speech_recognition as sr
# pip install SpeechRecognition
# pip install PyAudio

rec = sr.Recognizer()
pyag.size()
pyag.position()

# print(sr.Microphone().list_microphone_names())
with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("O que você quer fazer?\n1 - VS Code\n2 - Discord\n3 - ChatGPT\n4 - GitHub\n5 - Whatsapp\n")
    audio = rec.listen(mic)
    tarefa = rec.recognize_google(audio, language="pt-BR")
    tarefa = tarefa.lower()
    print(tarefa)

match tarefa:
    case "vs code":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Visual Studio Code... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o vs code
        pyag.press('winleft')
        pyag.write('visual studio code')
        pyag.press('enter')

        sleep(1)
    case "discord":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Discord... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o chrome
        pyag.press('winleft')
        pyag.write('chrome')
        pyag.press('enter')

        sleep(2)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://discord.com/channels/@me')
        pyag.press('enter')

        sleep(1)

    case "chatgpt":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o ChatGPT... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o chrome
        pyag.press('winleft')
        pyag.write('chrome')
        pyag.press('enter')

        sleep(3)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://chatgpt.com/')
        pyag.press('enter')

        sleep(1)

    case "github":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu GitHub... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o brave
        pyag.press('winleft')
        pyag.write('chrome')
        pyag.press('enter')

        sleep(3)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://github.com/dashboard')
        pyag.press('enter')

        sleep(1)
    case "whatsapp":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Whatsapp... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o brave
        pyag.press('winleft')
        pyag.write('chrome')
        pyag.press('enter')

        sleep(3)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://web.whatsapp.com/')
        pyag.press('enter')

        sleep(1)
    case _:
        pyag.alert(text='Tarefa não encontrada.', title='Divo Tech', button='Ok')