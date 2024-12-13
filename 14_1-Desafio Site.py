""" DESAFIO
1) Navegue até o site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU" """

# Tela NoteBook 2560 x 1600

import pyautogui
import webbrowser
import pygetwindow as gw
from time import sleep

def salvar_arquivo():
     # Esclhendo o local de salvamento
    botao_downloads = pyautogui.locateCenterOnScreen('botao_downloads.png',confidence=0.9)  # Localiza o botão da pasta downloads
    sleep(0.5)
    pyautogui.click(botao_downloads[0],botao_downloads[1],duration=2)  # com a coordenada centro, clica na pasta downloads
    sleep(1)
    botao_salvar = pyautogui.locateCenterOnScreen('botao_salvar.png',confidence=0.9)  # Localiza o botão salvar
    sleep(0.5)
    pyautogui.click(botao_salvar[0],botao_salvar[1],duration=2)  # com a coordenada centro, clica no botão salvar
    sleep(1)

def janela_browser():
    # Obter a janela ativa
    janela_ativa = gw.getActiveWindow()
    print(janela_ativa)

    if janela_ativa:
        # Tamanho da janela
        janela_largura = janela_ativa.width
        janela_altura = janela_ativa.height

        # Resolução da tela
        tela_largura = pyautogui.size()[0] + 22 # ajuste, a largura do browser maximizado é maior que da tela(vai entender rsrsrsrs)
        tela_altura = pyautogui.size()[1] - 50 # ajuste, descontando a altura da 'barra de tarefas' do windows

        # Verificar se o tamanho da janela corresponde à resolução da tela
        if janela_largura == tela_largura and janela_altura == tela_altura:
            # move o mouse para o ponto inicial
            pyautogui.moveTo(2200,350,duration=1)
            sleep(2)
        else:
            # Localiza o botão de maximizar a janela do browser, pega coordenada centro
            maximizar = pyautogui.locateCenterOnScreen('maximize.png',confidence=0.9)
            sleep(1)
            # com a coordenada centro, clica e maximiza a janela
            pyautogui.click(maximizar[0],maximizar[1],duration=2)
            sleep(1)
            # move o mouse para o ponto inicial
            pyautogui.moveTo(2200,350,duration=1)
            sleep(2)
    else:
        pyautogui.alert(text='Nenhuma Janela Ativa Encontrada',title='Aviso!')

# Minimizando VS Code
pyautogui.click(2390,20,duration=1)
sleep(0.5)

# Confirmar se inicia ou não
confirmacao = pyautogui.confirm(text='Deseja Iniciar Automação?',title='Automação de Site',buttons=['Sim','Não'])
sleep(1)

if confirmacao == 'Sim':
    webbrowser.open_new('https://cursoautomacao.netlify.app/')  # Abrir site
    sleep(2)
    # Verificação da janela do browser (maximizada ou não?)
    janela_browser()
    
    # abaixa a pagina até "exemplos alertas"
    for i in range(3):
        pyautogui.scroll(-365)
        sleep(0.75)
    
    # clica dentro da caixa "Digite seu nome"
    pyautogui.click(2200,350)

    # Coloca o nome
    pyautogui.typewrite('Fernando Martins',interval=0.1)
    sleep(0.5)
    # Clica em Alerta
    pyautogui.click(1970,400,duration=0.5)
    sleep(0.5)
    # Fecha o Alerta
    pyautogui.click(1540,280,duration=1)
    sleep(0.5)

    # Voltando para o ponto de inicio
    pyautogui.moveTo(2200,350,duration=1)
    sleep(1)
    # sobe a pagina até em cima
    for i in range(3):
        pyautogui.scroll(365)
        sleep(0.75)
    sleep(1.25)
    # Desce até a seção para download de arquivos
    for i in range(4):
        pyautogui.scroll(-365)
        sleep(0.75)
    
    # Realizar o download do arquivo excel
    pyautogui.click(540,1200,duration=2)
    sleep(1)
    salvar_arquivo()
   
    # Realizar o download do arquivo pdf
    pyautogui.click(830,1200,duration=2)
    sleep(1)
    salvar_arquivo()
    # Finalizando o Programa
    pyautogui.alert(text='Programa Finalizado, VOCÊ TERMINOU',title='Aviso!')
else:
    pyautogui.alert(text='Programa CANCELADO',title='Aviso!')