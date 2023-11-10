# FastAPI API Simples com Docker

Esta é uma API simples construída usando o FastAPI, um framework web moderno e rápido (alto desempenho) para construir APIs com Python 3.7+. A API inclui suporte ao Docker para fácil implantação.

## Requisitos

Certifique-se de ter o Docker instalado em sua máquina. Se não tiver, você pode baixá-lo [aqui](https://www.docker.com/get-started).

## Execute a API com o Docker

Para executar a API usando o Docker, siga estas etapas:

1. Construa a imagem do Docker:
   ```bash
   docker-compose up --build
   ```

2. Acesse a API em [http://localhost:8000](http://localhost:8000) no seu navegador.

3. Para parar a API, pressione `Ctrl+C` no terminal onde o Docker está sendo executado.

## Endpoints da API

### 1. **POST /ligar-desligar**

- **Descrição:** Alterna o status do ventilador (liga ou desliga).

- **Corpo da Requisição:**
  ```json
  {
    "ligar": true
  }
  ```

- **Resposta:**
  ```json
  {
    "mensagem": "Ventilador ligado"
  }
  ```
  ou
  ```json
  {
    "mensagem": "Ventilador desligado"
  }
  ```

- **Código de Status:**
  - `201`: Criado (para solicitações bem-sucedidas)

### 2. **GET /sensor-temperatura**

- **Descrição:** Obtém dados simulados do sensor de temperatura.

- **Resposta:**
  ```json
  {
    "temperatura": 25.5
  }
  ```

- **Código de Status:**
  - `200`: OK

## Dockerfile

```Dockerfile
# Usa a imagem oficial do Python
FROM python:3.7

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o contêiner
COPY . /app/

# Expõe a porta em que o FastAPI será executado
EXPOSE 8000

# Comando para executar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## docker-compose.yml

```yaml
version: '3'

services:
  fastapi-app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
```