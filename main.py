from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os
from faker import Faker

# Cria uma instância da classe FastAPI
app = FastAPI(title='Api do ADSXMEC')

# Configurações do MongoDB
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://root:root@mongo:27017/")
MONGO_DB = os.environ.get("MONGO_DB", "ads")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "ads")

# Conecta-se ao MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Cria uma instância do Faker
fake = Faker()

# Define um modelo Pydantic para representar o payload de requisição do endpoint /ligar-desligar
class LigarDesligar(BaseModel):
    ligar: bool

# Define um modelo Pydantic para representar o payload de resposta do endpoint /sensor-temperatura
class SensorTemperatura(BaseModel):
    temperatura: float  

# Manipula solicitações POST para o endpoint /ligar-desligar
@app.post('/ligar-desligar', response_model=dict, status_code=201)
def ligar_desligar(ligar_desligar: LigarDesligar):
    # Salva os dados no MongoDB
    collection.insert_one({"ligar": ligar_desligar.ligar})
    
    # Verifica o valor de ligar no payload da requisição
    if ligar_desligar.ligar:
        # Se ligar for True, retorna uma resposta indicando que o ventilador está ligado
        return {'mensagem': 'Ventilador ligado'}
    else:
        # Se ligar for False, retorna uma resposta indicando que o ventilador está desligado
        return {'mensagem': 'Ventilador desligado'}

# Manipula solicitações GET para o endpoint /sensor-temperatura
@app.get('/sensor-temperatura', response_model=SensorTemperatura, status_code=200)
def get_sensor_temperatura():
    # Cria dados fictícios usando o Faker
    temperature_data = {'temperatura': fake.pyfloat(left_digits=2, right_digits=1, positive=True)}
    
    # Salva os dados no MongoDB
    collection.insert_one({"temperatura": temperature_data['temperatura']})
    
    return temperature_data
