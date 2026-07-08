# pip install pyautogui

import time
import pyautogui
import pandas

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
    codigo = tabela_produtos.loc[linha, "codigo"]
    marca = tabela_produtos.loc[linha, "marca"]
    tipo = tabela_produtos.loc[linha, "tipo"]
    categoria = tabela_produtos.loc[linha, "categoria"]
    preco_unitario = tabela_produtos.loc[linha, "preco_unitario"]
    custo = tabela_produtos.loc[linha, "custo"]
    obs = tabela_produtos.loc[linha, "obs"]


    pyautogui.click(x=690, y=292)  # Clique no campo de código do produto
    pyautogui.write(str(codigo))  # Digitar o código do produto
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    if obs != "nan":  # Verifica se há observações para o produto
        pyautogui.write(str(obs))
    pyautogui.press("enter")
    pyautogui.scroll(5000) # Rolar a tela para cima para cadastrar o próximo produto

# Passo 5: Repetir o passo 4 até acabar a lista de produtos