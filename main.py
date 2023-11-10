from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LigarDesligar(BaseModel):
    ligar: bool

class SensorTemperatura(BaseModel):
    temperatura: float  

@app.post('/ligar-desligar', response_model=dict, status_code=201)
def ligar_desligar(ligar_desligar: LigarDesligar):
    if ligar_desligar.ligar:
        return {'mensagem': 'Ventilador ligado'}
    else:
        return {'mensagem': 'Ventilador desligado'}

@app.get('/sensor-temperatura', response_model=SensorTemperatura, status_code=200)
def get_sensor_temperatura():
    # Simula a leitura de dados de temperatura (substitua com a lógica real, se aplicável)
    temperature_data = {'temperatura': 25.5}
    return temperature_data
