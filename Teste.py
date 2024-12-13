# import pandas as pd
import pyautogui
import pygetwindow as gw

# tabela = pd.DataFrame({"Nome":["Lira","Fabrico"], "Idade": [29,25]})
# print(tabela)

# for i in range(0,27):
#     if i % 2 == 0:
#         print(i)

# nome = "Fernando"

# print(f"O seu nome é '{nome}'")
# tamanho = pyautogui.size()
# print(tamanho)

# Obter a janela ativa
janela_ativa = gw.getActiveWindow()

if janela_ativa:
    # Tamanho da janela
    janela_largura = janela_ativa.width
    janela_altura = janela_ativa.height

    # Resolução da tela
    tela_largura = pyautogui.size()
    tela_altura = pyautogui.size()

    # Verificar se o tamanho da janela corresponde à resolução da tela
    if janela_largura == tela_largura and janela_altura == tela_altura:
        print("A janela está maximizada.")
    else:
        print("A janela não está maximizada.")
else:
    print("Nenhuma janela ativa encontrada.")
