import schedule
import time
from main import publicar_producto_automatico

# Lista de productos que va rotando
PRODUCTOS = [
    "auriculares bluetooth",
    "smartwatch",
    "teclado mecanico",
    "mouse gamer",
    "camara web",
    "parlante bluetooth",
    "cargador inalambrico",
    "disco duro externo"
]

indice = 0

def publicar_turno():
    global indice
    query = PRODUCTOS[indice % len(PRODUCTOS)]
    print(f"\n⏰ Turno automático — buscando: {query}")
    publicar_producto_automatico(query, modo_prueba=True)
    indice += 1

# Publicar cada 3 horas
schedule.every(3).hours.do(publicar_turno)

# También publicar una vez al arrancar
print("🚀 Scheduler iniciado — publicando ahora y luego cada 3 horas")
publicar_turno()

while True:
    schedule.run_pending()
    time.sleep(60)