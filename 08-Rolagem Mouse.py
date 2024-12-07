# Rolagem Mouse (Scroll - Button Middle)
# Tela NoteBook 2560 x 1600
# Dividido tela ao meio (esquerda = VS Code, direita = Pagina WEB (Chrome))
# Site: https://pt.wikipedia.org/wiki/Brasil
# Rolar até aparecer o capitulo HISTÓRIA
import pyautogui
from time import sleep

pyautogui.moveTo(1800,400,duration=1)
# Colocado um laço de repetição e uma pausa (sleep) para ter uma rolagem mais lenta
for i in range(10):
    pyautogui.scroll(-340)
    sleep(0.75)