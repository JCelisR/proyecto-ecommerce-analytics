import numpy as np
import pandas as pd
import os

# Configuración del generador de números aleatorios
rng = np.random.default_rng(seed=42)
n_clientes = 500

# 1. GENERACIÓN DE DATOS BASE CON ARRAYS
ids = np.arange(1, n_clientes + 1)

nombres_base = np.array([
    "Ana", "Sofía", "Camila", "Valentina", "Isidora", "Martina",
    "Mateo", "Benjamín", "Tomás", "Vicente", "Lucas", "Joaquín",
    "Daniela", "Fernanda", "Ignacio", "Gabriel", "Antonia", "Catalina"
])

apellidos_base = np.array([
    "González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto",
    "Contreras", "Silva", "Martínez", "Sepúlveda", "Torres", "Flores"
])

# Creamos los nombres completos combinando aleatoriamente
nombres = rng.choice(nombres_base, size=n_clientes) + " " + rng.choice(apellidos_base, size=n_clientes)

# Ciudades con probabilidades específicas (Chile)
ciudades = np.array(["Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta", "Temuco", "Rancagua"])
ciudad = rng.choice(ciudades, size=n_clientes, p=[0.45, 0.12, 0.14, 0.08, 0.08, 0.08, 0.05])

# 2. CÁLCULOS ESTADÍSTICOS VECTORIZADOS
# Edad: Distribución normal (promedio 35 años)
edad = np.clip(rng.normal(loc=35, scale=12, size=n_clientes), 18, 70).round(0).astype(int)

# Total_Compras: Distribución de Poisson (promedio 4.5 compras)
total_compras = rng.poisson(lam=4.5, size=n_clientes)
total_compras = np.clip(total_compras, 0, 35)

# Ticket promedio y Monto Total con ruido aleatorio
ticket_promedio = rng.lognormal(mean=np.log(25000), sigma=0.55, size=n_clientes)
monto_total = (total_compras * ticket_promedio) + rng.normal(0, 5000, size=n_clientes)
monto_total = np.clip(monto_total, 0, None).round(0).astype(int)

# 3. OPERACIONES MATEMÁTICAS BÁSICAS (NumPy)
print(f"--- Estadísticas Iniciales (NumPy) ---")
print(f"Monto Total de Ventas: ${np.sum(monto_total)}")
print(f"Promedio de Edad de Clientes: {np.mean(edad):.1f} años")
print(f"Máximo de compras por un cliente: {np.max(total_compras)}")

# 4. ESTRUCTURACIÓN Y GUARDADO
# Creamos la carpeta 'data' si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Creamos un DataFrame para visualización y exportación
clientes = pd.DataFrame({
    "ID": ids,
    "Nombre": nombres,
    "Edad": edad,
    "Ciudad": ciudad,
    "Total_Compras": total_compras,
    "Monto_Total": monto_total
})

# 5. GUARDAR Y PREPARAR PARA LA SIGUIENTE CLASE
# Guardamos en formato binario .npy para la siguiente clase
np.save(r'C:\Users\jceli\Bootcamp\proyecto-ecommerce-analytics\data\transacciones_iniciales.npy', monto_total)

# También exportamos el CSV inicial para la siguiente clase
clientes.to_csv(r'C:\Users\jceli\Bootcamp\proyecto-ecommerce-analytics\data\dataset_transacciones.csv', index=False)

print("\n✅ Proceso completado: Archivo 'data\transacciones_iniciales.npy' guardado.")
print("\n--- Primeros 5 registros del DataFrame ---")
print(clientes.head())
