# Tela NoteBook 2560 x 1600
# dividido tela ao meio (esquerda = explorador de arquivos, direita = VS Code)
import pyautogui
from time import sleep   # Biblioteca para pausa entre clicks

# clica no icone do explorador de arquivos na barra de tarefas
pyautogui.click(815,1560,duration=2)
# Leva o mouse até o botão de maximixar da janela (aparece as opções de arranjos de janela)
pyautogui.moveTo(2444,17,duration=2)
sleep(1)   # tempo para aparecer as opções de arranjos de janela
# selecionar o arranjo de tela vertical (metade-metade) ividido tela ao meio (esquerda = explorador de arquivos, direita = VS Code)
pyautogui.click(2301,114,duration=0.2)
# clica em documentos
pyautogui.click(104,515,duration=2)
# Leva o mouse até o icone "Novo" lado esquerdo superior
pyautogui.click(63,160,duration=1)
# Seleciona "pasta" (criando nova pasta)
pyautogui.click(86,234,duration=0.5)
# clica for para finalizar
pyautogui.click(482,883,duration=2)

# Criando uma segunda pasta, clicando dentro de documentos (botão direito)
pyautogui.click(482,883,duration=1,button='right')
# Leva o mouse até o icone "Novo" e clica para abrir (se não clicar não abre)
pyautogui.click(538,1114,duration=1)
# leva o mouse até 'pasta'
pyautogui.moveTo(1035,595,duration=1) # 955,1114
sleep(0.25)   # tempo para aparecer
# leva o mouse até 'pasta' e clica para criar uma
pyautogui.click(1035,595,duration=0.25)
# clica for para finalizar
pyautogui.click(1030,1142,duration=1)