import pandas as pd
import numpy as np

# 1. CARGA DE DATOS
# Cargamos el archivo que creamos con NumPy en clase 1
try:
    df = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_transacciones.csv')
    data_numpy = np.load('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\transacciones_iniciales.npy')
    print("✅ Datos cargados exitosamente desde NumPy.\n")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo .npy. Asegúrate de ejecutar la Clase 1 primero.")

# 2. EXPLORACIÓN INICIAL
print("\n--- Primeras 5 filas ---")
print(df.head())  # Visualizar primeras filas 

print("\n--- Últimas 5 filas ---")
print(df.tail())  # Visualizar últimas filas

print("\n--- Información General ---")
print(df.info())  # Inspección de tipos de datos y nulos 

print("\n--- Estadísticas Descriptivas ---")
print(df.describe())  # Estadísticas básicas 

# 3. FILTROS CONDICIONALES
# Ejemplo: Transacciones con monto total mayor a 100,000
ventas_altas = df[df['Monto_Total'] > 100000]
print(f"\n🚀 Cantidad de ventas > 100,000: {len(ventas_altas)}")

# Ejemplo: Clientes con más de 4 compras
clientes_frecuentes = df[df['Total_Compras'] > 4]
print(f"🛒 Cantidad de clientes frecuentes (>4 compras): {len(clientes_frecuentes)}")

# 4. SUMARIZACIÓN Y VALORES ÚNICOS
print("\n--- Clientes por Ciudad ---")
print(df['Ciudad'].value_counts())  # Conteo por categorías

print("\n--- Ciudades Únicas ---")
print(df['Ciudad'].unique())  # Identificar valores únicos

# 5. GUARDAR PARA LA SIGUIENTE CLASE (Limpieza)
df.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_explorado.csv', index=False)
print("\n✅ Dataset estructurado guardado como 'data/dataset_explorado.csv'.")