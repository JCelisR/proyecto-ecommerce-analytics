import pandas as pd
import numpy as np

# 1. CARGA DE DATOS (Conexión con Clase 4)
try:
    # Cargamos el dataset que ya no tiene nulos ni outliers extremos
    df = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_limpio.csv', sep=';', encoding='latin1')
    print("✅ Dataset limpio cargado para Data Wrangling.")
except FileNotFoundError:
    print("❌ Error: Ejecuta primero la Clase 4.")
    exit()

# 2. TRANSFORMACIÓN Y CONVERSIÓN
df['Monto'] = df['Monto'].astype(float)
df['Cantidad'] = df['Cantidad'].astype(int)

# 3. DISCRETIZACIÓN / BINNING
bins = [0, 300, 700, np.inf]
labels = ['Económica', 'Estándar', 'Premium']
df['Categoria_Venta'] = pd.cut(df['Monto'], bins=bins, labels=labels)

# 4. ENRIQUECIMIENTO CON FUNCIONES LAMBDA Y MAP
# Aplicamos un impuesto del 15% a cada transacción usando lambda
df['Impuesto'] = df['Monto'].apply(lambda x: x * 0.15)

# Creamos una columna de 'Total' sumando Monto + Impuesto
df['Total_Con_Impuesto'] = df['Monto'] + df['Impuesto']

# 5. MANIPULACIÓN DE ESTRUCTURA
df = df.rename(columns={
    'Monto': 'Subtotal',
    'ID_Cliente': 'Cliente_ID'
})

# 6. ORDENAMIENTO
df = df.sort_values(by='Total_Con_Impuesto', ascending=False)

# 7. ELIMINACIÓN DE DUPLICADOS RESIDUALES
df = df.drop_duplicates()

# 8. EXPORTACIÓN FINAL
df.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_final_wrangled.csv', index=False, sep=';', encoding='latin1')
print("\n--- Muestra del Dataset Transformado ---")
print(df[['Cliente_ID', 'Subtotal', 'Categoria_Venta', 'Total_Con_Impuesto']].head())
print("\n Data Wrangling completado. Archivo 'data/dataset_final_wrangled.csv' generado.")