# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários (requirements.txt e a pasta do código fonte) para o diretório de trabalho
COPY requirements.txt /app/
COPY . /app/

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Expõe a porta em que a aplicação Django será executada
EXPOSE 8081

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
