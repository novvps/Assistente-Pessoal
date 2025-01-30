import pyautogui as pyag
from time import sleep

pyag.size()
pyag.position()

tarefa = int(input('O que você quer fazer?\n1 - VS Code\n2 - Discord\n3 - ChatGPT\n4 - GitHub\n5 - Whatsapp\nDigite aqui: '))

match tarefa:
    case 1:
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Visual Studio Code... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o vs code
        pyag.press('winleft')
        pyag.write('visual studio code')
        pyag.press('enter')

        sleep(1)
    case 2:
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Discord... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o brave
        pyag.press('winleft')
        pyag.write('brave')
        pyag.press('enter')

        sleep(2)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://discord.com/channels/@me')
        pyag.press('enter')

        sleep(1)

    case 3:
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o ChatGPT... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o brave
        pyag.press('winleft')
        pyag.write('brave')
        pyag.press('enter')

        sleep(3)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://chatgpt.com/')
        pyag.press('enter')

        sleep(1)

    case 4:
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu GitHub... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o brave
        pyag.press('winleft')
        pyag.write('brave')
        pyag.press('enter')

        sleep(3)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://github.com/dashboard')
        pyag.press('enter')

        sleep(1)
    case 5:
        pyag.hotkey('winleft', 'm')
        pyag.alert(text='Vou abrir o seu Whatsapp... Aguarde.', title='Divo Tech', button='Ok')
        pyag.PAUSE = 0.5

        # abrir o brave
        pyag.press('winleft')
        pyag.write('brave')
        pyag.press('enter')

        sleep(3)

        pyag.hotkey('ctrlleft', 'l')
        pyag.write('https://web.whatsapp.com/')
        pyag.press('enter')

        sleep(1)
    case _:
        pyag.alert(text='Tarefa não encontrada.', title='Divo Tech', button='Ok')