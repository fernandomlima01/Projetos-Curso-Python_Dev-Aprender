#Modulo 4
# Fazer o mouse ir até a pedra no jogo e clicar até passar a fase
# Site
# https://www.crazygames.com/game/doge-miner-2
# Estava utilizando 2 monitores
import pyautogui   # Biblioteca para usar o mouseInfo
from time import sleep   # Biblioteca para pausa entre clicks

# Posição algo - use o mouseInfo

# Fazer algo com essa posição
pyautogui.moveTo(-1275,672,duration=1)
# Repetição de clicks
for i in range(400):
    sleep(0.1)
    pyautogui.click()
    i = i + 1
    print(i)
    