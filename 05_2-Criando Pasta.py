# Criando pastas
# Tela NoteBook 2560 x 1600
# dividido tela ao meio (esquerda = explorador de arquivos, direita = VS Code)
import pyautogui
from time import sleep   # Biblioteca para pausa entre clicks

# clica no icone do explorador de arquivos na barra de tarefas
pyautogui.click(870,1560,duration=2)    # x= 820 com o cmd e mouseInfo abertos
# Leva o mouse até o botão de maximixar da janela (aparece as opções de arranjos de janela)
pyautogui.moveTo(2450,20,duration=2)
sleep(1)    # tempo para aparecer as opções de arranjos de janela
# selecionar o arranjo de tela vertical (metade-metade) dividindo tela ao meio (esquerda = explorador de arquivos, direita = VS Code)
pyautogui.click(2300,115,duration=0.2)
# clica em documentos
pyautogui.click(120,520,duration=2)
# Leva o mouse até o icone "Novo" lado esquerdo superior
pyautogui.click(65,160,duration=1)
# Seleciona "pasta" (criando nova pasta)
pyautogui.click(85,235,duration=0.5)
# clica for para finalizar
pyautogui.click(480,885,duration=2)

# Criando uma segunda pasta, clicando dentro de documentos (botão direito)
pyautogui.click(480,885,duration=1,button='right')
# Leva o mouse até o icone "Novo" e clica para abrir (se não clicar não abre)
pyautogui.click(540,1115,duration=1)
# leva o mouse até 'pasta'
pyautogui.moveTo(1035,595,duration=1) # 955,1114
sleep(0.25)    # tempo para aparecer
# leva o mouse até 'pasta' e clica para criar uma
pyautogui.click(1035,595,duration=0.25)
# clica for para finalizar
pyautogui.click(1030,1140,duration=1)