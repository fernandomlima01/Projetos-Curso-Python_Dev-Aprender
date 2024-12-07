#pyautogui.typewrite(interval)
# Tela NoteBook 2560 x 1600
# Dividido tela ao meio (esquerda = VS Code, direita = Bloco de Notas)
import pyautogui
from time import sleep

# Mover o mouse até o Bloco de Notas (lateral direita) e clicar dentro
pyautogui.click(1320,140,duration=2)

# Escrever texto longo sem o espaço (clocando Underline no lugar do espaço)
# NÃO necessita colocar o interval, mas a escrita ficará muito rápido
pyautogui.typewrite('teste_de_escrita_sem_acentuacao_e_sem_espaco_utilizando_underline') 
sleep(0.5)
pyautogui.press('enter')

# Não usar o intervalo (ou usala-lo zerado) da erro na escrita (não escreve textos mais longos completos)
pyautogui.typewrite('teste de escrita sem acentuacao e sem espaco utilizando underline',interval=0.0) 
sleep(0.5)
pyautogui.press('enter')

# Colocando o 'interval' em 0.1 ou maior o texto sai completo, com velocidade de escrita melhor (opnião)
pyautogui.typewrite('teste de escrita sem acentuacao e com espaco utilizando o interval em 0.1',interval=0.1) 