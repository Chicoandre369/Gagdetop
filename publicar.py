import requests
from config import PAGE_ID, PAGE_ACCESS_TOKEN, INSTAGRAM_ID, INSTAGRAM_TOKEN

def publicar_facebook(mensaje):
    url = f"https://graph.facebook.com/v25.0/{PAGE_ID}/feed"
    datos = {"message": mensaje, "access_token": PAGE_ACCESS_TOKEN}
    r = requests.post(url, data=datos)
    print("Facebook:", r.json())

def publicar_instagram(imagen_url, caption):
    url = f"https://graph.facebook.com/v25.0/{INSTAGRAM_ID}/media"
    datos = {"image_url": imagen_url, "caption": caption, "access_token": PAGE_ACCESS_TOKEN}
    r = requests.post(url, data=datos)
    container_id = r.json().get("id")
    print("Container:", r.json())

    if container_id:
        url2 = f"https://graph.facebook.com/v25.0/{INSTAGRAM_ID}/media_publish"
        datos2 = {"creation_id": container_id, "access_token": PAGE_ACCESS_TOKEN}
        r2 = requests.post(url2, data=datos2)
        print("Instagram:", r2.json())

# Prueba
publicar_facebook("¡Oferta increíble en Doctor Gadget Op! 🚀")
publicar_instagram(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png",
    "¡Mira este gadget! 🔥 #tecnologia #gadgets"
)