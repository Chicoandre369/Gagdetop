import requests

def buscar_producto_mercadolibre(query):
    url = f"https://api.mercadolibre.com/sites/MLC/search?q={query}&limit=5"
    r = requests.get(url)
    data = r.json()
    
    productos = []
    for item in data.get("results", []):
        productos.append({
            "nombre": item["title"],
            "precio": item["price"],
            "link": item["permalink"],
            "imagen": item.get("thumbnail", "")
        })
    
    return productos

# Prueba
import requests
url = "https://api.mercadolibre.com/sites/MLC/search?q=auriculares&limit=5"
r = requests.get(url)
print("Status:", r.status_code)
print("Respuesta:", r.text[:500])