# Reconhecimento Imagem
# OBS: Deixar sempre no formato .png
import os
import pyautogui
from time import sleep

# Imprime o caminho do módulo pyautogui (opcional para depuração)
print(pyautogui.__file__)
# Base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
print("base_dir = ", base_dir)

# imagem_path = os.path.join(base_dir, "Calculadora_Imagem", "num_3.png")
# print("imagem_path = ", imagem_path)

# num3 = pyautogui.locateCenterOnScreen(imagem_path,confidence=0.9)
# print(num3)
# pyautogui.click(num3[0],num3[1],duration=2)

# Lista das imagens que você quer utilizar
imagens = {
    "num_3": os.path.join(base_dir, "Calculadora_Imagem", "num_3.png"),
    "num_5": os.path.join(base_dir, "Calculadora_Imagem", "num_5.png"),
    "num_mult": os.path.join(base_dir, "Calculadora_Imagem", "num_mult.png"),
    "num_7": os.path.join(base_dir, "Calculadora_Imagem", "num_7.png"),
    "num_9": os.path.join(base_dir, "Calculadora_Imagem", "num_9.png"),
    "num_igual": os.path.join(base_dir, "Calculadora_Imagem", "num_igual.png"),
    "num_c": os.path.join(base_dir, "Calculadora_Imagem", "num_c.png"),
}

# Percorre as imagens
for nome, caminho in imagens.items():
    print(f"Procurando pela imagem: {nome} no caminho: {caminho}")
    if not os.path.exists(caminho):
        print(f"Erro: A imagem {nome} não foi encontrada no caminho: {caminho}")
        continue

    # Tenta localizar a imagem na tela
    try:
        posicao = pyautogui.locateCenterOnScreen(caminho, confidence=0.9)
        if posicao:
            print(f"Imagem {nome} encontrada em {posicao}. Clicando...")
            pyautogui.click(posicao[0], posicao[1], duration=1)
            sleep(0.5)
        else:
            print(f"Imagem {nome} não encontrada na tela.")
    except Exception as e:
        print(f"Erro ao processar a imagem {nome}: {e}")







# # Caminho para a imagem
# imagem_path = r"c:\Users\ferna\Documents\Programacao\Repositorio_GitHub\Projetos-Curso-Python_Dev-Aprender\Calculadora_Imagem\num_3.png"

# # Verifique se o arquivo existe
# if not os.path.exists(imagem_path):
#     print("Erro: O arquivo não foi encontrado no caminho:", imagem_path)
# else:
#     print("Arquivo encontrado. Tentando localizar na tela...")

#     # Tenta localizar a imagem na tela
#     try:
#         num3 = pyautogui.locateCenterOnScreen(imagem_path, confidence=0.9)
#         if num3:
#             print("Imagem encontrada:", num3)
#             pyautogui.click(num3[0], num3[1], duration=2)
#         else:
#             print("Imagem não encontrada na tela.")
#     except Exception as e:
#         print("Erro ao localizar a imagem:", e)
