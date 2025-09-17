#%%
import pyautogui
import time

# pyautogui documentation:https://pyautogui.readthedocs.io/en/latest/
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinTESA0002010 Samsung Televisao   10  2000.0  TESA000729  Samsung Televisao   9   720.0TESA000108  Samsung Televisao   8   10000.0 3000.0      
# TESA000747  Samsung Televisao   7   740.0   214.6   TESA000125  Samsung Televisao   5   1260.0  
# TELG000524  LG  Televisao   4   520.0   145.6       
# TELG000252  LG  Televisao   2   250.0   62.5        
# ação de teclas

#%%

# Passo 1: Entrar no sistema da empresa -https://dlp.hashtagtreinamentos.com/p...
# Abrir o chome:
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")    


# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")



# Passo 2: Fazer login:


time.sleep(2)
#preencher email
pyautogui.click(x=635, y=371) # clicar email
pyautogui.write("guto@gmai.com") # preenche o email

# preencher senha
pyautogui.press("tab") # passa para o proximo campo
pyautogui.write("214356") # preenche a senha

# botão logar
pyautogui.press("enter") # faz o login  201.6   

# espera de 3 segundos
time.sleep(2)


# Passo 3: Importar a base de dados
import pandas as pd 


tabela = pd.read_csv("produtos.csv")

print(tabela)


# Passo 4: Cadastrar um produto
contador = 0  # inicializa o contador

for linha in tabela.index:
    pyautogui.click(x=653, y=260)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

    contador += 1  # incrementa o contador
    if contador >= 10:
        break  # interrompe o loop após 10 produtos


# Passo 5: Repetir para todos os produtos






