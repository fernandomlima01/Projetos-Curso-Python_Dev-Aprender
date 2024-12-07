# Digitando com PyAutoGUI
# Tela NoteBook 2560 x 1600
# Dividido tela ao meio (esquerda = VS Code, direita = Bloco de Notas)
import pyautogui
import pyperclip    # Biblioteca para mostrar acentuação e cedilha.

# Criar uma função para escrever com acentuações
def escrever_frase (frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')    # comando para atalhos, atalho para colar

# Mover o mouse até o Bloco de Notas (lateral direita) e clicar dentro
pyautogui.click(1320,140,duration=2)

# Escrever a frase no Bloco de Notas
escrever_frase('Automação é Incrível!')
pyautogui.press('enter')    # Comando para quebra de linha

# Frase de comparação
# Comando do pyautogui para escrever, porém não sai acentuação e cedilha
pyautogui.typewrite('Automacao e Incrivel')    # Para comparativo, não sai todo

# Mover até Arquivo (Canto superior esquerdo do Bloco de Notas)
pyautogui.click(1320,80,duration=1)
# Salvar arquivo
pyautogui.click(1320,295,duration=1)
'''
# Mover cursor do mouse para dentro do Blocos de Notas e clicar dentro
pyautogui.click(1320,770,duration=1)
# Salvando novamente utilizando pyautogui.hotkey
pyautogui.hotkey('ctrl','s')    # comando para atalhos, atalho para salvar
'''