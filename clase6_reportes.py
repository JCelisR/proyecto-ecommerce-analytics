import pandas as pd
import numpy as np

# 1. CARGA DE DATOS
try:
    df_ventas = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_final_wrangled.csv', sep=';', encoding='latin1')
    df_productos = pd.read_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\categorias_productos.xlsx')
    print("✅ Datasets cargados exitosamente.")
except Exception as e:
    print(f"❌ Error al cargar archivos. Vuelve a ejecutar clase 5 y 3: {e}")
    exit()

# 2. COMBINACIÓN DE DATOS (Merge - Tarea 6)
# Nota: Como nuestro dataset sintético no tenía ID_Producto, lo asignaremos aleatoriamente para el ejemplo
np.random.seed(42)
df_ventas['ID_Producto'] = np.random.randint(1, 4, size=len(df_ventas))

df_consolidado = pd.merge(df_ventas, df_productos, on='ID_Producto', how='left')

# 3. AGRUPAMIENTO
reporte_categorias = df_consolidado.groupby('Categoria').agg({
    'Total_Con_Impuesto': 'sum',
    'Cliente_ID': 'count',
    'Subtotal': 'mean'
}).rename(columns={'Cliente_ID': 'Cantidad_Ventas', 'Subtotal': 'Ticket_Promedio'})

print("\n--- REPORTE POR CATEGORÍA ---")
print(reporte_categorias)

# 4. PIVOTEO
# Creamos una tabla dinámica para ver el Total de Ventas por Categoría y Segmento (Binning)
tabla_pivot = df_consolidado.pivot_table(
    values='Total_Con_Impuesto', 
    index='Categoria', 
    columns='Categoria_Venta', 
    aggfunc='sum',
    fill_value=0
)

print("\n--- TABLA PIVOT: VENTAS POR CATEGORÍA Y SEGMENTO ---")
print(tabla_pivot)

# 5. EXPORTACIÓN FINAL DEL PROYECTO
reporte_categorias.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\reporte_final_categorias.csv', sep=';')
tabla_pivot.to_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\reporte_final_pivot.xlsx')

print("\n PROYECTO FINALIZADO.")
print("Archivos generados: 'data/reporte_final_categorias.csv' y 'data/reporte_final_pivot.xlsx'")