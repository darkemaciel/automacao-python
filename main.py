# pip install pyautogui

import time
import pyautogui
import pandas

# Configurações do PyAutoGUI, como tempo de pausa entre as ações.
pyautogui.PAUSE = 0.5
# Configurações de segurança do PyAutoGUI, como a ativação do modo de segurança.
pyautogui.FAILSAFE = True


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
pyautogui.write("senha muito3 tensa! braba demais slk!")  # Substitua pela sua senha
pyautogui.press("enter")
time.sleep(3)  # Aguardar o carregamento da página após o login


# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl

tabela_produtos = pandas.read_csv("produtos.csv") # Ler a tabela de produtos do arquivo CSV
print(tabela_produtos)  # Exibe a tabela de produtos no console


# Passo 4: Cadastrar 1 produto
# Localizar os campos do formulário e preencher com os dados do produto
for linha in tabela_produtos.index:
 
    pyautogui.click(x=690, y=292)  # Clique no campo de código do produto
    pyautogui.write(str(tabela_produtos.loc[linha, "codigo"]))  # Digitar o código do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pandas.isna(tabela_produtos.loc[linha, "obs"]):  # Verifica se há observações para o produto
        pyautogui.write(str(tabela_produtos.loc[linha, "obs"]))
    pyautogui.press("enter")
    pyautogui.scroll(5000) # Rolar a tela para cima para cadastrar o próximo produto

# Passo 5: Repetir o passo 4 até acabar a lista de produtos