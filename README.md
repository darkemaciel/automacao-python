# Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em uma página web (ex.: ambiente de testes) usando o mouse e teclado por meio de `pyautogui`. O script lê uma tabela CSV com os produtos e preenche um formulário no navegador.

**Arquivos principais**
- [main.py](main.py): script principal que abre o navegador, faz login (credenciais no código) e cadastra os produtos a partir de `produtos.csv`.
- [auxiliar.py](auxiliar.py): utilitário para capturar posições do mouse (aguarda 5 segundos e imprime as coordenadas).
- [produtos.csv](produtos.csv): exemplo de tabela de produtos a ser importada.

**Requisitos**
- Python 3.8+ instalado
- Pacotes Python: `pyautogui`, `pandas`, `pynput`, `openpyxl` (se precisar salvar/ler Excel)

Instalação rápida:

```bash
pip install pyautogui pandas pynput openpyxl
```

**Como usar**
1. Ajuste a resolução e posicionamento do navegador para que os cliques automáticos atinjam os campos corretos.
2. (Opcional) Rode [auxiliar.py](auxiliar.py) para pegar coordenadas dos campos: `python auxiliar.py`. Posicione o cursor sobre o elemento e aguarde a impressão da posição.
3. Se necessário, edite as coordenadas em [main.py](main.py) (procure as chamadas `clicar(x, y)` e ajuste os valores).
4. Verifique/atualize as credenciais e a URL do login dentro de [main.py](main.py).
5. Coloque o arquivo `produtos.csv` na mesma pasta e rode: `python main.py`.

**Interrupção e segurança**
- Pressione `ESC` para cancelar a automação imediatamente (o script monitora a tecla Esc).
- O `pyautogui.FAILSAFE` está ativado: mover o mouse rapidamente para o canto superior esquerdo também interrompe o script.

**Formato do CSV esperado**
- Cabeçalho: `codigo,marca,tipo,categoria,preco_unitario,custo,obs`
- Exemplo de linha:

```
MOLO000251,Logitech,Mouse,1,25.95,6.50,
```

**Observações**
- Este script usa automação de interface (GUI) — qualquer mudança no layout da página ou resolução pode exigir ajuste de coordenadas.
- Use em ambiente de testes; evite rodar em sistemas de produção sem validação prévia.
