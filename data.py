from urllib import response
from pandas import json_normalize
import pandas as pd
import requests 
import json 
# # response = requests.get('http://127.0.0.1:8000/cobertura')
# # info = json.loads(response.text)    
# # info = json.dumps(info)
# # datos = pd.read_json(info, orient='index')
# # print(datos)


# data = pd.read_csv("datos.csv")
# data.dropna(axis = 0, how = "all", inplace = True) 
# Fechas2 = []
# for i in data["AÑO"]:
#     Fechas2.append( str(i)[:4] + "-01" )

# Fechas2 = pd.to_datetime(Fechas2)
# data.set_index(Fechas2, inplace = True)
# data_Cobertura = data["COBERTURA_NETA"].resample("Y").mean()
# data_Matriculacion = data["TASA_MATRICULACIÓN_5_16"].resample("Y").mean()
# Resumen = pd.concat([data_Cobertura, data_Matriculacion], axis = "columns", keys = ["Cobertura Neta", "Tasa de Matriculación"])
# print(Resumen)
