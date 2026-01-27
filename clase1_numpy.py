import numpy as np
import os

# 1. GENERACIÓN DE DATOS FICTICIOS
# Configuramos la semilla para que los datos sean siempre los mismos al ejecutar
np.random.seed(42)

# Simulamos 500 transacciones
n_registros = 500

# IDs de Clientes: Generamos 500 IDs aleatorios entre el 1000 y el 1050 (algunos repetirán)
ids_clientes = np.random.randint(1000, 1051, size=n_registros)

# Montos: Distribución normal (Media $500, Desviación $150)
montos = np.random.normal(500, 150, size=n_registros).round(2)

# Cantidades: Números enteros entre 1 y 5 productos por compra
cantidades = np.random.randint(1, 6, size=n_registros)

# 2. OPERACIONES MATEMÁTICAS BÁSICAS
print("--- RESUMEN ESTADÍSTICO INICIAL (NumPy) ---")
print(f"Total de Ventas: ${np.sum(montos):,.2f}")
print(f"Ticket Promedio: ${np.mean(montos):,.2f}")
print(f"Venta Máxima: ${np.max(montos)}")
print(f"Desviación Estándar de Ventas: ${np.std(montos):,.2f}")
print(f"Total de productos vendidos: {np.sum(cantidades)}")
print("-" * 40)

# 3. ESTRUCTURACIÓN Y GUARDADO
# Creamos una carpeta 'data' si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Combinamos los arrays en una sola matriz para transporte de datos
# Columna 0: ID, Columna 1: Monto, Columna 2: Cantidad
dataset_final = np.column_stack((ids_clientes, montos, cantidades))

# Guardamos en formato .npy (binario de NumPy)
np.save(r'C:\Users\jceli\Bootcamp\proyecto-ecommerce-analytics\data\transacciones_iniciales.npy', dataset_final)

print("✅ Proceso completado: Archivo 'data/transacciones_iniciales.npy' guardado.")
