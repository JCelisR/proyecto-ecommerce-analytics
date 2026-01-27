import pandas as pd
import numpy as np

# 1. CARGA DE DATOS (Conexión con Clase 3)
try:
    df = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\ventas_consolidadas.csv', sep=';', encoding='latin1')
    print("✅ Dataset cargado para limpieza.")
except FileNotFoundError:
    print("❌ Error: Ejecuta primero la Clase 3.")
    exit()

# --- SIMULACIÓN DE PROBLEMAS (Para poder limpiar) ---
# Inyectamos algunos valores nulos (NaN)
df.loc[0:5, 'Monto'] = np.nan
df.loc[10:12, 'Cantidad'] = np.nan

# Inyectamos Outliers (Valores atípicos)
df.loc[50, 'Monto'] = 15000  # Una venta imposiblemente alta
df.loc[51, 'Monto'] = -500   # Un monto negativo erróneo

# 2. IDENTIFICACIÓN DE VALORES PERDIDOS
print("\n--- Conteo de Valores Nulos ---")
print(df.isnull().sum())

# 3. IMPUTACIÓN (Tratamiento de nulos)
# Imputamos 'Monto' con la mediana (más robusta ante outliers que la media)
mediana_monto = df['Monto'].median()
df['Monto'] = df['Monto'].fillna(mediana_monto)

# Imputamos 'Cantidad' con la moda (el valor más frecuente)
moda_cantidad = df['Cantidad'].mode()[0]
df['Cantidad'] = df['Cantidad'].fillna(moda_cantidad)
print(f"\n✅ Nulos imputados (Monto con {mediana_monto} y Cantidad con {moda_cantidad}).")

# 4. DETECCIÓN Y FILTRADO DE OUTLIERS
Q1 = df['Monto'].quantile(0.25)
Q3 = df['Monto'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtramos el DataFrame para mantener solo datos dentro del rango
df_clean = df[(df['Monto'] >= limite_inferior) & (df['Monto'] <= limite_superior)]

outliers_detectados = len(df) - len(df_clean)
print(f"✅ Outliers eliminados: {outliers_detectados}")

# 5. GUARDAR DATASET LIMPIO PARA LA SIGUIENTE CLASE
df_clean.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_limpio.csv', index=False, sep=';', encoding='latin1')
print("\n Dataset limpio guardado en 'data/dataset_limpio.csv'.")