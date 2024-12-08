# Alertas_adquirindo dados usuarios
# Tela NoteBook 2560 x 1600
# Dividido tela ao meio (esquerda = VS Code, direita = Bloco de Notas)
import pyautogui
from time import sleep

# Alertar
#pyautogui.alert(text='Iniciar Automação?',title='Automação de Login',button='Iniciar')

# Confirmar se inicia ou não
confirmacao = pyautogui.confirm(text='Deseja Iniciar Automação?',title='Automação de Login',buttons=['Sim','Não'])

if confirmacao == 'Sim':
    # Pedir Informação
    email = pyautogui.prompt(text='Digite seu e-mail',title='Dados Login')
    print(f'O e-mail digitado foi: {email}')

    senha = pyautogui.password(text='Digite sua Senha',title='Dados Login',mask='*')
    print(f'A Senha digitada foi: {senha}')
    
    #Abrindo Bloco de Notas (Rascunho.txt)
    pyautogui.press('winleft')
    sleep(1)
    pyautogui.typewrite(r'C:\Users\ferna\Documents\Rascunho.txt')
    pyautogui.press('enter')
    
    # Indo até o Bloco de Notas 
    pyautogui.click(1500,230,duration=2)
    sleep(1)

    #Colando o email
    pyautogui.typewrite(email,interval=0.1)
    sleep(0.5)
    pyautogui.press('enter')

    # Colando a Senha
    pyautogui.typewrite(senha,interval=0.1)
else:
    pyautogui.alert(text='Programa Finalizado',title='Aviso!')
    print('Programa Finalizado')