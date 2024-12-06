# Click personalizado
# x e y = São as coordenadas do click;
# clicks = É onde define a quantidade de clicks;
# interval = Definição do tempo (segundos) entre um click e outro;
# button = Define qual botão do mouse será clicado ('left', 'right' e middle);
# duration = Definição do tempo (segundos) em que o ponteiro do mouse vai até o local do click

import pyautogui

pyautogui.click(1910,965,clicks=200, interval=0.1,button='left',duration=1)

# Clica na posição atual (Padrão = botão esquerdo)
pyautogui.click()
# definindo botões
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
# Clicar X vezes
pyautogui.click(clicks=20)
# Funções prontas para clicks
pyautogui.doubleClick
pyautogui.tripleClick
pyautogui.rightClick
pyautogui.middleClick