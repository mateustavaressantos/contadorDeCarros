# 🚗 Contador de Veículos em Rodovias (Visão Computacional)

Este projeto é um sistema de monitoramento e contagem automática de veículos em tempo real utilizando técnicas de Processamento Digital de Imagens (PDI) com Python e OpenCV. O sistema foi projetado para cobrir ambas as direções de uma rodovia movimentada através de sensores virtuais independentes.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **OpenCV (`opencv-python` / `opencv-contrib-python`):** Para manipulação, processamento de vídeo e binarização de imagem.
* **NumPy:** Para operações de matrizes (filtros morfológicos e máscaras).

---

## 🚀 Como Rodar o Projeto Passo a Passo

Siga as instruções abaixo para configurar o ambiente isolado e executar o contador.

### 1. Clonar ou Acessar a Pasta do Projeto
Abra o seu terminal (ou o terminal integrado do VS Code) na pasta raiz onde estão localizados os arquivos do projeto (`contador.py`, `requirements.txt` e `rodovia.mp4`).

### 2. Criar um Ambiente Virtual (`venv`)
Para evitar conflitos de versões de bibliotecas no seu computador, crie um ambiente virtual rodando:
`bash`
python -m venv venv

### 3. Ativar o Ambiente Virtual
Ative o ambiente de acordo com o terminal que você está utilizando no VS Code:
`Se estiver usando o CMD (Prompt de Comando):`
.\venv\Scripts\activate.bat

`Se estiver usando o PowerShell:`
.\venv\Scripts\Activate.ps1

`No Linux/macOS:`
source venv/bin/activate

Nota: Você saberá que deu certo quando o prefixo (venv) aparecer no início da linha do terminal.

### 4. Instalar as Dependências
Com o ambiente ativado, instale todas as bibliotecas necessárias listadas no arquivo requirements.txt:
pip install -r requirements.txt

### 5. Executar o Contador
Certifique-se de que o arquivo de vídeo rodovia.mp4 está no caminho correto configurado no código. Em seguida, execute:
python contadorCarros.py
