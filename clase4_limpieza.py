import pandas as pd
import numpy as np

# 1. CARGA DE DATOS (Conexión con Clase 3)
try:
    df = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\ventas_consolidadas.csv', sep=';', encoding='latin1')
    print("✅ Dataset cargado para limpieza.")
except FileNotFoundError:
    print("❌ Error: Ejecuta primero la Clase 3.")
    exit()

# Insertamos algunos nulos y duplicados aleatorios
df.loc[df.sample(frac=0.05).index, 'Edad'] = np.nan
df = pd.concat([df, df.iloc[:5]], ignore_index=True) 

# 2. GESTIÓN DE NULOS Y DUPLICADOS
print(f"\n Nulos detectados:\n{df.isnull().sum()}")
print(f" Duplicados iniciales: {df.duplicated().sum()}")

# Decisiones de limpieza:
df.drop_duplicates(inplace=True) # Eliminamos duplicados
df['Edad'] = df['Edad'].fillna(df['Edad'].median()) # Imputación por mediana

# 3. DETECCIÓN DE OUTLIERS (Método IQR)
# El IQR es ideal para variables financieras
Q1 = df['Monto_Total'].quantile(0.25)
Q3 = df['Monto_Total'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['Monto_Total'] < limite_inferior) | (df['Monto_Total'] > limite_superior)]
print(f"\n Outliers detectados en Monto_Total: {len(outliers)}")

# Filtramos el dataset para mantener solo datos "normales"
df_limpio = df[(df['Monto_Total'] >= limite_inferior) & (df['Monto_Total'] <= limite_superior)]

# 5. GUARDAR DATASET LIMPIO PARA LA SIGUIENTE CLASE
df_limpio.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_limpio.csv', index=False, sep=';', encoding='latin1')
print("\n Dataset limpio guardado en 'data/dataset_limpio.csv'.")