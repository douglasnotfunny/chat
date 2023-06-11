# Chat

Este projeto tem como objetivo criar uma integração com o ChatGPT e dar a melhor resposta sem a necessidade de usá-lo. É necessário ter o MySQL instalado no computador para salvar e recuperar os dados. Após a clonagem do projeto executar o tutorial abaixo:

  1. Criar ambiente virtual:
    
    python3.10 -m venv env
    
  1.1. Ativar ambiente de acordo com o seu sistema operacional - LINUX:
    
    source env/bin/activate
    
  1.2. Ativar ambiente de acordo com o seu sistema operacional - Windows:
    
    source env/Scripts/activate

  2. Instalar pacotes:
    
    pip install -r requirements.txt
   
  3. Criar .env baseado no .env.example e inserir as constantes do seu banco de dados:
  
  4. Executar a aplicação:
    
    python app.py
