import pyautogui as pyag
from time import sleep
import speech_recognition as sr
# pip install SpeechRecognition
# pip install PyAudio
# pip install pyautogui

rec = sr.Recognizer()
pyag.size()
pyag.position()

# print(sr.Microphone().list_microphone_names())
with sr.Microphone(0) as mic:
    try:
        rec.adjust_for_ambient_noise(mic)
        print("O que você quer fazer?\n1 - VS Code\n2 - Discord\n3 - ChatGPT\n4 - GitHub\n5 - Whatsapp\n6 - Sair\n")
        audio = rec.listen(mic)
        tarefa = rec.recognize_google(audio, language="pt-BR")
        tarefa = tarefa.lower()
        print(tarefa)
    except:
        pyag.alert('Falha no Sistema :(', title='RPA DDS', button='Ok')
match tarefa:
    case "visual studio":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Visual Studio Code... Aguarde.', title='RPA DDS', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o vs code
        pyag.press('winleft')
        pyag.write('visual studio code')
        pyag.press('enter')

        sleep(1)
    case "discord":
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Discord... Aguarde.', title='RPA DDS', button='Ok')
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
        pyag.alert(text='Vou abrir o ChatGPT... Aguarde.', title='RPA DDS', button='Ok')
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
        pyag.alert(text='Vou abrir o seu GitHub... Aguarde.', title='RPA DDS', button='Ok')
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
        pyag.alert(text='Vou abrir o seu Whatsapp... Aguarde.', title='RPA DDS', button='Ok')
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
    case "sair":
        saida = True
        pyag.alert(text='Saindo... Até logo.', title='RPA DDS', button='Até logo')
    case _:
        pyag.alert(text='Tarefa não encontrada.', title='RPA DDS', button='Ok')
