import pandas as pd
import requests # Librería necesaria para consultar APIs

# 1. CARGA DEL CSV (Ventas del E-commerce)
    # Cargamos el archivo generado en la Clase 2
try:
    df_ventas = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_explorado.csv')
    print("✅ CSV de ventas cargado exitosamente.")
except FileNotFoundError:
    print("⚠️ No se encontró el archivo. Verifique la Clase 2.")

# 2. CARGA DE EXCEL
try:
    # Simulamos un catálogo de categorías
    df_categorias = pd.DataFrame({
        'ID_Producto': [1, 2, 3, 4, 5],
        'Categoria': ['Electrónica', 'Hogar', 'Moda', 'Deportes', 'Juguetes']
    })
    df_categorias.to_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\categorias_productos.xlsx', index=False)
    df_excel = pd.read_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\categorias_productos.xlsx')
    print("✅ Archivo Excel de categorías cargado.")
except Exception as e:
    print(f"❌ Error con Excel: {e}")

# 3. EXTRACCIÓN WEB (API mindicador.cl)
try:
    url_api = "https://mindicador.cl/api/dolar"
    response = requests.get(url_api)
    data = response.json()
    
    # Extraemos el valor del dólar más reciente
    valor_dolar = data['serie'][0]['valor']
    print(f"✅ Valor del dólar extraído de la API: ${valor_dolar}")
except Exception as e:
    print(f"⚠️ Error al consultar la API: {e}")
    valor_dolar = 950.0         # Valor de respaldo (Plan de contingencia)

# Consulté a Gemini por errores como el 429, entre otros y me sugirió utilizar la página con API.
# Esto lo realicé con ayuda de Gemini, ya que no estaba en el material del curso.
# Es muy complejo extraer datos de páginas que tienen protecciones, incluso del sii.cl

# 4. UNIFICACIÓN DE FUENTES
# En esta etapa consolidamos la información para la limpieza futura
df_consolidado = df_ventas.copy()
df_consolidado['Valor_Dolar_Referencia'] = valor_dolar
df_consolidado['Fuente_Dolar'] = "mindicador.cl"

# 5. GUARDAR DATOS CONSOLIDADOS
# Consolidamos las ventas en un nuevo archivo para la Clase 4 (Limpieza)
df_consolidado.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\ventas_consolidadas.csv', index=False, sep=';')
print("\n Dataset consolidado guardado en 'data/ventas_consolidadas.csv' listo para limpieza.")