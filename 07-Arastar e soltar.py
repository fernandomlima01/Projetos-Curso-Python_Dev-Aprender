# Arrastar e soltar arquivos
# Tela NoteBook 2560 x 1600
# dividido tela ao meio (esquerda = VS Code, direita = 2 explorador de arquivos, em cima e em baixo)
# o VS Code começara maximizado
import pyautogui
from time import sleep   # Biblioteca para pausa entre clicks

# VS Code
# Leva o mouse até o botão de minimizar da janela (aparece as opções de arranjos de janela)
pyautogui.click(2390,20,duration=1)    

# Esplorador de arquivos 1
# clica no icone do explorador de arquivos na barra de tarefas
pyautogui.click(870,1560,duration=2)   # x= 820 com o cmd e mouseInfo abertos
# Leva o mouse até o botão de maximixar da janela (aparece as opções de arranjos de janela)
pyautogui.moveTo(2450,20,duration=2)
sleep(1)   # tempo para aparecer as opções de arranjos de janela
# selecionar o arranjo de tela vertical (metade-metade) dividindo tela ao meio (esquerda = explorador de arquivos 1, direita = explorador de arquivos 2)
pyautogui.click(2260,110,duration=0.2)

# Esplorador de arquivos 2
# clica (button right) no icone do explorador de arquivos na barra de tarefas
pyautogui.rightClick(870,1560,duration=2)    # x= 820 com o cmd e mouseInfo abertos
# abrir nova janela do explorador de arquivos
pyautogui.click(870,1380,duration=0.75)  
# Leva o mouse até o botão de maximixar da janela (aparece as opções de arranjos de janela)
pyautogui.moveTo(2450,20,duration=2)
sleep(1)   # tempo para aparecer as opções de arranjos de janela
# selecionar o arranjo de tela vertical (metade-metade) dividindo tela ao meio (esquerda = explorador de arquivos 1, direita = explorador de arquivos 2)
pyautogui.click(2340,110,duration=0.2)

# Pasta com arquivos (explorador 1 - Lado Esquerdo Tela)
# clica em documentos
pyautogui.click(120,520,duration=2)
# Abrir "pasta com arquivos"
pyautogui.doubleClick(555,260,duration=1)

# Pasta SEM arquivos (explorador 2 - Lado Direito tela)
# clica em documentos
pyautogui.click(1400,520,duration=2)
# Abrir "pasta com arquivos"
pyautogui.doubleClick(1850,315,duration=1)

# Arrastar arquivos da "Pasta com Arquivos" para "Pasta SEM Arquivos"
# Loop para arrastar os 13 arquivos
for i in range(13):
    # Mouse vai até o primeiro arquivo
    pyautogui.moveTo(555,260,duration=0.5)
    pyautogui.dragTo(1850,260,button='left',duration=1)