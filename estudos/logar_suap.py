import pyautogui
import time
import os

pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')
pyautogui.write('chrome.exe')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','t')
pyautogui.write('https://cav.receita.fazenda.gov.br/')
pyautogui.press('enter')
time.sleep(3)

# Inserir CPF
pyautogui.click(x=-782, y=440)
pyautogui.write('04173636482')
time.sleep(1)

# Inserir Código de Acesso
pyautogui.click(x=-782, y=501)
pyautogui.write('168145753957')
time.sleep(1)

# Inserir Senha
pyautogui.click(x=-782, y=568)
pyautogui.write('D3nys0781')
time.sleep(1)

# Entrar no site
pyautogui.click(x=-657, y=615)
time.sleep(2)
pyautogui.click(x=-1511, y=385)
time.sleep(4)

# clicar nas pendências de 2021
pyautogui.click('pendencias.PNG')