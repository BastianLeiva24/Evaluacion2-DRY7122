import requests
import sys

API_KEY = "2338100b-d6c4-4609-a484-0101d9b9313a"

URL = "https://graphhopper.com/api/1/route"

ciudades = {
    "Santiago": "-33.4489,-70.6693",
    "Ovalle": "-30.5983,-71.2003",
    "La Serena": "-29.9045,-71.2489",
    "Coquimbo": "-29.9533,-71.3436"
}

def calcular_ruta(origen, destino):

    if origen not in ciudades or destino not in ciudades:
        print("\nCiudad no registrada.\n")
        return

    parametros = {
        "point": [
            ciudades[origen],
            ciudades[destino]
        ],
        "vehicle": "car",
        "locale": "es",
        "instructions": "true",
        "calc_points": "true",
        "key": API_KEY
    }

    respuesta = requests.get(URL, params=parametros)

    if respuesta.status_code != 200:
        print("Error al conectar con la API")
        return

    datos = respuesta.json()

    ruta = datos["paths"][0]

    distancia = ruta["distance"] / 1000
    tiempo = ruta["time"] / 1000

    horas = int(tiempo // 3600)
    minutos = int((tiempo % 3600) // 60)
    segundos = int(tiempo % 60)

    combustible = distancia / 12

    print("\n================================")
    print("      INFORME DE VIAJE")
    print("================================")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Distancia: {distancia:.2f} KM")
    print(f"Tiempo estimado: {horas}h {minutos}m {segundos}s")
    print(f"Combustible: {combustible:.2f} litros")

    print("\nNarrativa del viaje:\n")

    contador = 1

    for paso in ruta["instructions"]:
        print(f"{contador}. {paso['text']}")
        contador += 1

    print()

while True:

    print("================================")
    print(" SISTEMA DE RUTAS")
    print("================================")

    origen = input("Ciudad Origen (q para salir): ")

    if origen.lower() == "q":
        print("Programa finalizado")
        sys.exit()

    destino = input("Ciudad Destino (q para salir): ")

    if destino.lower() == "q":
        print("Programa finalizado")
        sys.exit()

    calcular_ruta(origen, destino)