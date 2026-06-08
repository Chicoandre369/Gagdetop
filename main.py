from scraper import buscar_producto_mercadolibre
from generador import generar_texto_post
from publicar import publicar_facebook

# Producto de prueba para cuando ML está bloqueado
PRODUCTO_PRUEBA = {
    "nombre": "Auriculares Bluetooth Sony WH-1000XM5",
    "precio": "189990",
    "link": "https://www.mercadolibre.cl/auriculares-sony"
}

def publicar_producto_automatico(query="auriculares", modo_prueba=False):
    print(f"\n🔍 Buscando producto: {query}")
    
    if modo_prueba:
        print("⚠️ Modo prueba — usando producto hardcodeado")
        producto = PRODUCTO_PRUEBA
    else:
        # Paso 1: Scraper
        productos = buscar_producto_mercadolibre(query, limit=1)
        
        if not productos:
            print("❌ No se encontraron productos")
            return
        
        producto = productos[0]
    
    nombre = producto["nombre"]
    precio = producto["precio"]
    link = producto["link"]
    
    print(f"✅ Producto: {nombre} - ${precio}")
    
    # Paso 2: Generar texto
    texto = generar_texto_post(nombre, precio, link)
    
    if not texto:
        print("❌ No se pudo generar el texto")
        return
    
    # Paso 3: Publicar en Facebook
    publicar_facebook(texto)
    print("\n🎉 ¡Publicación completada!")

if __name__ == "__main__":
    publicar_producto_automatico("auriculares", modo_prueba=True)