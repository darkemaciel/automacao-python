# pip install pyautogui pandas openpyxl pynput

import time
import threading

import pandas
import pyautogui
from pynput import keyboard

# ==========================
# CONFIGURAÇÕES
# ==========================

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

# Evento para cancelar a automação
parar = threading.Event()


# ==========================
# LISTENER DO TECLADO
# ==========================

def on_press(key):
    if key == keyboard.Key.esc:
        parar.set()
        print("\n🛑 ESC pressionado. Cancelando automação...")


listener = keyboard.Listener(on_press=on_press)
listener.start()


# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def verificar_parada():
    """Interrompe imediatamente a automação."""
    if parar.is_set():
        listener.stop()
        raise SystemExit("Automação cancelada pelo usuário.")


def esperar(segundos):
    verificar_parada()
    time.sleep(segundos)
    verificar_parada()


def clicar(x, y):
    verificar_parada()
    pyautogui.click(x=x, y=y)


def escrever(texto):
    verificar_parada()
    pyautogui.write(str(texto))


def pressionar(tecla):
    verificar_parada()
    pyautogui.press(tecla)


def scroll(valor):
    verificar_parada()
    pyautogui.scroll(valor)


# ==========================
# AUTOMAÇÃO
# ==========================

try:

    # Abrir Chrome
    pressionar("win")
    escrever("chrome")
    pressionar("enter")

    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

    escrever(link)
    pressionar("enter")

    esperar(2)

    # Login
    clicar(740, 406)
    escrever("teste@gmail.com")
    pressionar("tab")
    escrever("senha muito3 tensa! braba demais slk!")
    pressionar("enter")

    esperar(3)

    # Ler tabela
    tabela_produtos = pandas.read_csv("produtos.csv")

    print(tabela_produtos)

    # Cadastro dos produtos
    for indice, produto in tabela_produtos.iterrows():

        verificar_parada()

        clicar(690, 292)

        escrever(produto["codigo"])
        pressionar("tab")

        escrever(produto["marca"])
        pressionar("tab")

        escrever(produto["tipo"])
        pressionar("tab")

        escrever(produto["categoria"])
        pressionar("tab")

        escrever(produto["preco_unitario"])
        pressionar("tab")

        escrever(produto["custo"])
        pressionar("tab")

        if not pandas.isna(produto["obs"]):
            escrever(produto["obs"])

        pressionar("enter")
        scroll(5000)

except SystemExit as e:
    print(e)

finally:
    listener.stop()
    print("Programa finalizado.")