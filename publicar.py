import requests
from config import PAGE_ID, PAGE_ACCESS_TOKEN, INSTAGRAM_ID, INSTAGRAM_TOKEN

def publicar_facebook(mensaje):
    """Publica un texto en el feed de la página de Facebook."""
    url = f"https://graph.facebook.com/v25.0/{PAGE_ID}/feed"
    datos = {
        "message": mensaje,
        "access_token": PAGE_ACCESS_TOKEN
    }
    r = requests.post(url, data=datos)
    resultado = r.json()
    
    if "id" in resultado:
        print(f"✅ Facebook publicado! ID: {resultado['id']}")
    else:
        print(f"❌ Error en Facebook: {resultado}")
    
    return resultado

def publicar_instagram(imagen_url, caption):
    """Publica una imagen en Instagram (requiere permiso instagram_content_publish)."""
    
    # Paso 1: Crear container
    url1 = f"https://graph.facebook.com/v25.0/{INSTAGRAM_ID}/media"
    datos1 = {
        "image_url": imagen_url,
        "caption": caption,
        "access_token": INSTAGRAM_TOKEN
    }
    r1 = requests.post(url1, data=datos1)
    res1 = r1.json()
    print(f"Container: {res1}")
    
    container_id = res1.get("id")
    
    if not container_id:
        print(f"❌ Error creando container: {res1}")
        return res1
    
    # Paso 2: Publicar container
    url2 = f"https://graph.facebook.com/v25.0/{INSTAGRAM_ID}/media_publish"
    datos2 = {
        "creation_id": container_id,
        "access_token": INSTAGRAM_TOKEN
    }
    r2 = requests.post(url2, data=datos2)
    res2 = r2.json()
    
    if "id" in res2:
        print(f"✅ Instagram publicado! ID: {res2['id']}")
    else:
        print(f"❌ Error publicando en Instagram: {res2}")
    
    return res2


# ──────────────────────────────────────────
# Prueba — comenta estas líneas cuando no las necesites
# ──────────────────────────────────────────
if __name__ == "__main__":
    # Prueba Facebook
    publicar_facebook("¡Oferta increíble en Doctor Gadget Op! 🚀")
    
    # Prueba Instagram (necesita URL pública de imagen real)
    # publicar_instagram(
    #     "https://TU_IMAGEN_PUBLICA.jpg",
    #     "¡Mira este gadget! 🔥 #tecnologia #gadgets"
    # )