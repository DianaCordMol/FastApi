from fastapi import FastAPI
from metodos import metodos  as m

app = FastAPI(title="API de prueba", version="1.0.0")

@app.get("/nombre")
def getNombre(name: int): 
    return {'hola': 'mundo '+ str(name)}

@app.get("/metodos")
def getMetodo(): 
    data = m.prepararDatos()
    data=data.astype(str)
    return data.to_dict(orient="records")