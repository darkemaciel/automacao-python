# pip install pyautogui

import time
import pyautogui

# Configurações do PyAutoGUI, como tempo de pausa entre as ações.
pyautogui.PAUSE = 0.5

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa

# Abrir o navegador e acessar o link do sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# Aguardar o carregamento da página
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=740, y=406)  # Clique no campo de usuário
pyautogui.write("teste@gmail.com")  # Substitua pelo seu usuário
pyautogui.press("tab")
pyautogui.write("teste123!")  # Substitua pela sua senha
pyautogui.press("enter")
time.sleep(3)  # Aguardar o carregamento da página após o login


# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos