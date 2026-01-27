# Proyecto cierre módulo 3: Análisis de E-commerce
Repositorio dedicado al análisis exploratorio, limpieza y transformación de datos de un entorno e-commerce utilizando Python.

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de un flujo de trabajo automatizado para la obtención, limpieza y estructuración de datos de una empresa de e-commerce. El objetivo es transformar datos crudos provenientes de múltiples fuentes (CSV, Excel, Web) en un dataset confiable listo para modelos de Machine Learning y reportes estratégicos.

## 📁 Estructura del Proyecto
- `clase1_numpy.py`: Generación y fundamentos de arrays.
- `clase2_panda.py`: Estructuras de datos (Series y DataFrames).
- `clase3_extraccion.py`: Lectura de fuentes externas (CSV, Excel, Web).
- `clase4_limpieza.py`: Tratamiento de nulos y Outliers (IQR).
- `clase5_wrangling.py`: Transformación avanzada y enriquecimiento.
- `clase6_reportes.py`: Agrupamiento y tablas dinámicas finales.

## Datos
Los datasets procesados se encuentran en la carpeta `/data`.

## Tecnologías
- Python 3.13+
- Pandas / NumPy
- Openpyxl / Lxml

## Avance por Clases
### Clase 1: Cimentación con NumPy
- Generación de un conjunto de datos ficticio de clientes y transacciones.
- Implementación de operaciones estadísticas básicas para análisis preliminar.
- Exportación de datos en formato binario (`.npy`) para asegurar la integridad de los tipos de datos.

### Clase 2: Estructuración con Pandas
- Transformación de arreglos NumPy a **DataFrames**.
- Exploración de datos usando `.describe()`, `.info()` y `.value_counts()`.
- Aplicación de **filtros condicionales** para segmentar transacciones de alto valor.
- Exportación a formato **CSV** para estandarización de procesos.

### Clase 3: Extracción Multi-fuente
- Implementación de `read_csv` con optimización de tipos de datos (`dtype`).
- Manejo de archivos Excel mediante `read_excel` y la librería `openpyxl`.
- **Web Scraping** básico: Uso de `read_html` para capturar datos financieros en tiempo real.
- Aplicación de técnicas de ahorro de memoria (`usecols`) y manejo de codificaciones (`encoding`).

### Clase 4: Manejo de Valores Perdidos y Outliers
- Uso de `isnull().sum()` para dimensionar la falta de datos.
- Aplicación de la **Mediana** para valores numéricos (Monto) para mitigar el sesgo de valores extremos.
- Aplicación de la **Moda** para variables discretas (Cantidad).
- **Tratamiento de Outliers:** Implementación del método del **Rango Intercuartílico (IQR)** para filtrar registros que distorsionan el análisis estadístico.
- Reducción de ruido en el dataset y creación de `dataset_limpio.csv`.

### Clase 5: Data Wrangling y Enriquecimiento
- Segmentación de transacciones en categorías ('Económica', 'Estándar', 'Premium') para facilitar el análisis de marketing.
- Uso de funciones **Lambda** y `.apply()` para cálculos dinámicos de impuestos y totales.
- Renombramiento de columnas y reordenamiento estratégico de filas para mejorar la legibilidad del reporte final.
- Conversión de tipos de datos (`astype`) para asegurar la eficiencia en el procesamiento de grandes volúmenes.

### Clase 6: Agrupamiento, Pivoteo e Integración Final
- Uso de `pd.merge()` para consolidar datos de ventas con el catálogo de productos (similares a JOINs en SQL).
- Implementación de `groupby()` con múltiples funciones estadísticas (`agg`) para extraer métricas de negocio.
- Creación de **Tablas Pivot** para cruzar categorías de productos con segmentos de precio.
- Generación de reportes finales en formatos CSV y Excel para la toma de decisiones gerenciales.

---

## Conclusión del Proyecto
Se ha implementado un flujo de datos (Pipeline) completo que:
1. **Obtiene** datos de fuentes heterogéneas (NumPy, CSV, Excel, Web).
2. **Limpia** errores, nulos y outliers (IQR).
3. **Transforma** y enriquece la información (Lambda, Binning).
4. **Analiza** y reporta resultados mediante agrupaciones complejas.

**El dataset final es confiable, estructurado y está listo para ser consumido por modelos de Machine Learning o herramientas de visualización como Power BI.**
