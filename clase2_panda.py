import pandas as pd
import numpy as np

# 1. CARGA DE DATOS (Conexión Clase 1 -> Clase 2)
try:
    data_numpy = np.load('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\transacciones_iniciales.npy')
    print("✅ Datos cargados exitosamente desde NumPy.\n")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo .npy. Asegúrate de ejecutar la Clase 1 primero.")

# 2. CREACIÓN DEL DATAFRAME
# Convertimos la matriz en un DataFrame con nombres de columnas claros
df = pd.DataFrame(data_numpy, columns=['ID_Cliente', 'Monto', 'Cantidad'])

# Convertimos ID_Cliente a entero (NumPy lo guardó como float por la matriz)
df['ID_Cliente'] = df['ID_Cliente'].astype(int)

# 3. EXPLORACIÓN BÁSICA
print("--- PRIMEROS 5 REGISTROS (head) ---")
print(df.head(), "\n")

print("--- INFORMACIÓN ESTRUCTURAL (info) ---")
df.info()
print("\n")

print("--- ESTADÍSTICAS DESCRIPTIVAS (describe) ---")
print(df.describe(), "\n")

# 4. SELECCIÓN Y FILTRADO
# Ejemplo: Filtrar transacciones mayores a $700
ventas_altas = df[df['Monto'] > 700]

# Ejemplo: Clientes que compraron más de 4 productos
clientes_mayoristas = df[df['Cantidad'] > 4]

print(f"Cantidad de ventas mayores a $700: {len(ventas_altas)}")
print(f"Monto promedio de ventas con +4 productos: ${clientes_mayoristas['Monto'].mean():.2f}\n")

# 5. SUMARIZACIÓN Y VALORES ÚNICOS
print(f"Total de clientes únicos: {df['ID_Cliente'].nunique()}")
print("Conteo de transacciones por cantidad de productos:")
print(df['Cantidad'].value_counts())

# 6. GUARDAR PARA LA SIGUIENTE CLASE (Limpieza)
df.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_transacciones.csv', index=False)
print("\n✅ Dataset estructurado guardado como 'data/dataset_transacciones.csv'.")