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

# 2. TRANSFORMACIÓN DE TIPOS DE DATOS
# Aseguramos que los tipos sean correctos para cálculos y ahorro de memoria
df['ID'] = df['ID'].astype(int)
df['Total_Compras'] = df['Total_Compras'].astype(np.int32)
df['Monto_Total'] = df['Monto_Total'].astype(float)

# 3. CREACIÓN DE COLUMNAS CALCULADAS Y FUNCIONES LAMBDA
# Calculamos el Ticket Promedio por cliente
df['Ticket_Promedio'] = (df['Monto_Total'] / df['Total_Compras']).round(2)

# Aplicamos una función personalizada con lambda para categorizar por edad
df['Segmento_Etario'] = df['Edad'].apply(lambda x: 'Joven' if x < 30 else ('Adulto' if x < 60 else 'Sénior'))

# 4. NORMALIZACIÓN Y ESTRUCTURACIÓN DE DATOS
# Binning: Categorizamos el valor del cliente según su gasto
# Creamos 3 niveles: Bronce, Plata, Oro
bins = [0, 50000, 150000, np.inf]
labels = ['Bronce', 'Plata', 'Oro']
df['Rango_Valor_Cliente'] = pd.cut(df['Monto_Total'], bins=bins, labels=labels)

# Normalización simple: Score de compras (0 a 1) para identificar clientes activos
df['Score_Actividad'] = (df['Total_Compras'] - df['Total_Compras'].min()) / (df['Total_Compras'].max() - df['Total_Compras'].min())

# 5. ELIMINACIÓN DE DUPLICADOS RESIDUALES
# Por si la integración de fuentes generó duplicados nuevos
df = df.drop_duplicates()

# 6. EXPORTACIÓN FINAL PARA ANÁLISIS DE CLASE FINAL
df.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_final_wrangled.csv', index=False, sep=';', encoding='latin1')
print("\n Data Wrangling completado. Columnas nuevas: Ticket_Promedio, Segmento_Etario, Rango_Valor_Cliente.")
print(df[['Nombre', 'Segmento_Etario', 'Rango_Valor_Cliente', 'Score_Actividad']].head())