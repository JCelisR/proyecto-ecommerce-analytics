import pandas as pd
import numpy as np

# 1. CARGA DE DATOS 
# Conexión con Clases anteriores (1 a 5)
try:
    df = pd.read_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\dataset_final_wrangled.csv', sep=';', encoding='latin1')
    # Cargamos también el catálogo de Excel creado en la Clase 3
    df_cat = pd.read_excel('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\categorias_productos.xlsx')
    print("✅ Datasets cargados exitosamente.")
except Exception as e:
    print(f"❌ Error al cargar archivos. Vuelve a ejecutar clase 5 y 3: {e}")
    exit()

# 2. COMBINACIÓN DE DATOS (Merge)
# Generamos IDs de productos aleatorios para cruzar con el catálogo
df['ID_Producto'] = np.random.randint(1, 6, size=len(df))

# Unimos las tablas (Data Wrangling avanzado)
df_final = pd.merge(df, df_cat, on='ID_Producto', how='left')

# 3. AGRUPAMIENTO
# Obtenemos métricas resumidas por Ciudad y Categoría
resumen_ventas = df_final.groupby(['Ciudad', 'Categoria'])['Monto_Total'].agg(['sum', 'mean', 'count']).reset_index()
resumen_ventas.columns = ['Ciudad', 'Categoria', 'Venta_Total', 'Promedio_Venta', 'Num_Transacciones']

# 4. REESTRUCTURACIÓN (pivot_table)
# Creamos una tabla dinámica para ver el Total de Ventas por Categoría y Segmento (Binning)
# Creamos una matriz para comparar ventas de categorías entre ciudades
matriz_ventas = df_final.pivot_table(
    index='Ciudad', 
    columns='Categoria', 
    values='Monto_Total', 
    aggfunc='sum',
    fill_value=0
)

print("\n--- TABLA PIVOT: VENTAS POR CATEGORÍA Y SEGMENTO ---")
print(matriz_ventas)

# 5. EXPORTACIÓN FINAL DEL PROYECTO
# CSV para sistemas de datos y Excel para reportes gerenciales
df_final.to_csv('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\entrega_final_ventas.csv', index=False)
with pd.ExcelWriter('C:\\Users\\jceli\\Bootcamp\\proyecto-ecommerce-analytics\\data\\reporte_final_analisis.xlsx') as writer:
    df_final.to_excel(writer, sheet_name='Datos_Detallados', index=False)
    resumen_ventas.to_excel(writer, sheet_name='Resumen_KPIs', index=False)
    matriz_ventas.to_excel(writer, sheet_name='Matriz_Ciudades')

print("\n🏆 ¡Proyecto Finalizado! Archivos generados en la carpeta /data:")
print("- entrega_final_ventas.csv")
print("- reporte_final_analisis.xlsx (Con múltiples pestañas)")