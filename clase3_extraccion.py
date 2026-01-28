import pandas as pd
import numpy as np

# 1. CARGA DE CSV (Ventas del E-commerce)
try:
    # Simulamos la carga del CSV que generamos en la Clase 2
    df_ventas = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_transacciones.csv', 
                            sep=',', 
                            encoding='utf-8',
                            dtype={'ID_Cliente': 'int32', 'Cantidad': 'int8'})
    print("✅ CSV de ventas cargado exitosamente.")
except FileNotFoundError:
    print("⚠️ No se encontró el CSV. Generando uno de prueba...")
    # (Código de respaldo por si no hay archivo a mano)
    df_ventas = pd.DataFrame({'ID_Cliente': [1001, 1002], 'Monto': [500.0, 300.0], 'Cantidad': [2, 1]})

# 2. CARGA DE EXCEL
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

# 3. EXTRACCIÓN WEB (Indicadores IPSA Chile)
# Extraeremos una tabla de ejemplo de la web, en este caso Wikipedia
try:
    url = "https://es.wikipedia.org/wiki/%C3%8Dndice_de_Precio_Selectivo_de_Acciones"
    tablas = pd.read_html(url)
    # Seleccionamos la tabla de las empresas que componen el IPSA
    df_ipsa = tablas[0] 
    print(f"✅ Tabla del IPSA extraída exitosamente.")
except Exception as e:
    print(f"⚠️ No se pudo extraer la tabla web: {e}")
    # Creación de respaldo con columnas reales de la página (Empresa, Rubro)
    df_ipsa = pd.DataFrame(columns=['Empresa', 'Ticker', 'Rubro'])
    print("ℹ️ Usando DataFrame de respaldo vacío para evitar errores.")

# 4. MUESTREO DE DATOS
print("\n--- Vista rápida de empresas IPSA (Primeras 5 filas) ---")
if not df_ipsa.empty:
    # Mostramos las columnas típicas de esa tabla de Wikipedia
    print(df_ipsa.head(5))
else:
    print("La tabla está vacía.")

# 5. EXPORTACIÓN PARA LA SIGUIENTE CLASE
# Consolidamos las ventas en un nuevo archivo para la Clase 4 (Limpieza)
df_ventas.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\ventas_consolidadas.csv', index=False, sep=';', encoding='latin1')

print("\n Datos exportados a 'data/ventas_consolidadas.csv' listos para limpieza.")