import pandas as pd
import numpy as np

# --- 1. CARGA DE CSV (Ventas del E-commerce) ---
# Usamos parámetros avanzados para optimizar la carga
try:
    # Simulamos la carga del CSV que generamos en la Clase 2
    df_ventas = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_transacciones.csv', 
                            sep=',', 
                            encoding='utf-8',
                            dtype={'ID_Cliente': 'int32', 'Cantidad': 'int8'})
    print("✅ CSV de ventas cargado exitosamente.")
except FileNotFoundError:
    print("⚠️ No se encontró el CSV. Generando uno de prueba...")
    # (Código de respaldo por si no tienes el archivo a mano)
    df_ventas = pd.DataFrame({'ID_Cliente': [1001, 1002], 'Monto': [500.0, 300.0], 'Cantidad': [2, 1]})

# --- 2. CARGA DE EXCEL (Catálogo de Categorías) ---
# En un entorno real, aquí leerías un .xlsx de proveedores
try:
    # Si no tienes un excel real, creamos uno para demostrar la escritura y lectura
    df_categorias = pd.DataFrame({
        'ID_Producto': [1, 2, 3],
        'Categoria': ['Electrónica', 'Hogar', 'Moda']
    })
    df_categorias.to_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\categorias_productos.xlsx', index=False, sheet_name='Catalogo')
    
    # Lectura especificando la hoja
    df_excel = pd.read_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\categorias_productos.xlsx', sheet_name='Catalogo')
    print("✅ Archivo Excel cargado exitosamente.")
except Exception as e:
    print(f"❌ Error con Excel: {e}")

# --- 3. EXTRACCIÓN WEB (Indicadores Económicos) ---
try:
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tablas = pd.read_html(url)
    df_sp500 = tablas[0] # La primera tabla es la que nos interesa
    print(f"✅ Tabla Web extraída exitosamente.")
except Exception as e:
    print(f"⚠️ No se pudo extraer la tabla web: {e}")
    # Creamos un dataframe vacío con las columnas esperadas
    df_sp500 = pd.DataFrame(columns=['Symbol', 'Security', 'Sector'])
    print("ℹ️ Usando DataFrame de respaldo vacío para evitar errores.")
    

# --- 4. OPTIMIZACIÓN Y MUESTREO ---
print("\n--- Vista rápida del S&P 500 (Primeras 3 filas) ---")
if not df_sp500.empty:
    print(df_sp500[['Symbol', 'Security', 'Sector']].head(3))
else:
    print("La tabla está vacía debido al error de extracción.")

# --- 5. EXPORTACIÓN CONSOLIDADA ---
# Guardamos todo en un formato estándar para la Clase 4
df_ventas.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\ventas_consolidadas.csv', index=False, sep=';', encoding='latin1')

print("\n🚀 Datos exportados a 'data/ventas_consolidadas.csv' listos para limpieza.")