import requests
from config import GROQ_API_KEY

def generar_texto_post(nombre, precio, link):
    """Genera un texto atractivo para publicar en Facebook usando Groq."""
    
    prompt = f"""Eres un experto en marketing digital para redes sociales.
Crea un post atractivo para Facebook sobre este producto de tecnología:

Producto: {nombre}
Precio: ${precio} CLP
Link: {link}

El post debe:
- Ser en español
- Tener máximo 3 líneas
- Incluir 2-3 emojis relevantes
- Terminar con el link
- Sonar natural y llamativo, no robótico

Responde SOLO con el texto del post, sin explicaciones."""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    datos = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }
    
    r = requests.post(url, headers=headers, json=datos)
    resultado = r.json()
    
    if "choices" in resultado:
        texto = resultado["choices"][0]["message"]["content"].strip()
        print(f"✅ Texto generado: {texto}")
        return texto
    else:
        print(f"❌ Error Groq: {resultado}")
        return None


if __name__ == "__main__":
    # Prueba
    texto = generar_texto_post(
        "Auriculares Bluetooth Sony WH-1000XM5",
        "189990",
        "https://www.mercadolibre.cl/auriculares-sony"
    )