# Teclas de Atalho
# Tela NoteBook 2560 x 1600
# Dividido tela ao meio (esquerda = VS Code, direita = Bloco de Notas)
import pyautogui
import time

# Mover o mouse até o Bloco de Notas (lateral direita) e clicar dentro
pyautogui.click(1320,140,duration=2)
time.sleep(1)

# comando para simular uma tecla especifica do teclado
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.typewrite('Tab',interval=0.1)
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.typewrite('space',interval=0.1)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.typewrite('enter_backspace',interval=0.1)
time.sleep(3)
for i in range(10):
    pyautogui.press('backspace')
    time.sleep(0.5)

# Simular "Segurar uma tecla"
pyautogui.keyDown('ctrl')  # pressionar para baixo a tecla 'ctrl'
pyautogui.keyDown('a')     # pressionar para baixo a tecla 'a'
pyautogui.keyUp('ctrl')    # Solta a tecla 'ctrl'
pyautogui.keyUp('a')       # Solta a tecla 'a'
# Simular "Segurar uma tecla" poderia utilizar uma unica linha de comando
#pyautogui.hotkey('ctrl','a')  # Selecionar tudo


# Comando para atalhos (múltiplas teclas)
pyautogui.hotkey('ctrl','c')  # Copiar
pyautogui.press('down')  # Simula seta para baixo

# Desce 10 linhas
for i in range(10):
    pyautogui.press('enter')
    time.sleep(0.1)

# Comando para atalhos (múltiplas teclas)
pyautogui.hotkey('ctrl','v')  # Colar

# Para ver todas as possíveis teclas que possa ser colocada no "press":
#print(pyautogui.KEYBOARD_KEYS)
#print(pyautogui.KEY_NAMES)