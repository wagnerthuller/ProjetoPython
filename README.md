# ProjetoPython — Automação de Cadastro com PyAutoGUI

**Autor:** Wagner  
**Commit inicial:** feat: projeto de automação com PyAutoGUI

Este projeto realiza a automação de cadastro de produtos em um sistema web utilizando a biblioteca PyAutoGUI. Ele simula ações humanas como abrir o navegador, preencher campos e enviar formulários com base em dados de um arquivo CSV.

---

## 📦 Estrutura do Projeto

ProjetoPython/ 
├─ codigo.py # Script principal da automação 
├─ auxilia.py # Funções auxiliares (validações, suporte, etc) 
├─ produtos.csv # Base de dados com os produtos 
├─ README.md # Documentação do projeto 
├─ requirements.txt # Dependências do projeto 
└─ .gitignore # Arquivos ignorados pelo Git


---

## 🚀 Funcionalidades

- Abre o navegador Chrome automaticamente
- Acessa a página de login do sistema
- Preenche e envia e-mail e senha
- Lê os dados de produtos de um arquivo CSV
- Cadastra até 10 produtos no sistema
- Usa funções auxiliares para modularizar o código

---

## 🛠️ Requisitos

- Python 3.9 ou superior
- Sistema operacional: Windows
- Navegador: Google Chrome
- Bibliotecas:
  - pyautogui
  - pandas

---
▶️ Como Executar
Ajuste o e-mail e senha no arquivo codigo.py.

Verifique se o Chrome está instalado e acessível.

Ajuste as coordenadas dos cliques com:

python
import pyautogui, time
time.sleep(5)
print(pyautogui.position())
Execute o script:

bash
python codigo.py
⚠️ Não mexa no mouse ou teclado durante a execução. Mantenha o Chrome em foco e evite mudar o zoom ou layout da página.

🧩 Sobre o auxilia.py
Este arquivo contém funções auxiliares que podem incluir:

Validação de dados

Conversão de tipos

Tratamento de campos vazios

Funções reutilizáveis para o codigo.py

✅ Dicas
Ative o fail-safe do PyAutoGUI:

python
pyautogui.FAILSAFE = True  # mover o mouse para o canto superior esquerdo aborta
pyautogui.PAUSE = 1        # intervalo entre ações
Ajuste tempos de espera com time.sleep() para garantir que a página carregue corretamente.

Para tratar campos NaN no CSV:

python
import math
obs = tabela.loc[linha, "obs"]
if not (isinstance(obs, float) and math.isnan(obs)):
    pyautogui.write(str(obs))
📌 Licença
