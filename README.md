# Proyecto cierre módulo 3: Análisis de E-commerce
Repositorio dedicado al análisis exploratorio, limpieza y transformación de datos de un entorno e-commerce utilizando Python.

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de un flujo de trabajo automatizado para la obtención, limpieza y estructuración de datos de una empresa de e-commerce. El objetivo es transformar datos crudos provenientes de múltiples fuentes (CSV, Excel, Web) en un dataset confiable listo para modelos de Machine Learning y reportes estratégicos.

## 📁 Instrucciones para Ejecutar el Proyecto

Para reproducir este flujo de trabajo, ejecute los scripts en el siguiente orden:
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

1. Justificación de Herramientas

NumPy: Se eligió por su rapidez para crear y manejar grandes conjuntos de números, lo que facilita generar datos sintéticos (simulados) de forma eficiente.
Pandas: Se utilizó para leer, limpiar y organizar los datos en tablas fáciles de trabajar. Permite cargar archivos (CSV, Excel, HTML) y transformar la información para análisis posteriores.

2. Descripción de Datos y Fuentes

    Se creó un conjunto de datos de ventas (DataSet) mediante simulaciones aleatorias para representar transacciones históricas.

    Fuentes externas
        - Archivo Excel: catálogo de categorías de productos que enriquece cada venta.
        - Extracción de Indicadores: Uso de APIs (mindicador.cl) y Web Scraping para integrar el valor del dólar en tiempo real, contextualizando el análisis financiero.

3. Técnicas de Limpieza y Transformación

    Manejo de Valores faltantes: Se aplicó identificación mediante isnull() e imputación con estadísticas de tendencia central (media/mediana para numéricos y moda para categóricos).

    Outliers: Se identificaron y filtraron valores extremos usando el rango intercuartil (IQR), evitando que montos atípicos afecten los análisis.

    Data Wrangling:

        Binning: Segmentación o agrupación de ventas por niveles de gasto.

        Lambdas: Cálculo de impuestos y totales de forma eficiente.

        Agregación: Resumen de métricas mediante groupby() y pivot_table.

4. Decisiones y Desafíos

    Decisión: Se prefirió la mediana para imputar montos porque es menos sensible a valores extremos que la media.

    Desafío: Resolver dependencias opcionales para la extracción web (por ejemplo librerías adicionales) y asegurar que el proceso de carga fuera robusto. Manejo de Bloqueos Web: Se superaron errores de acceso (HTTP 403/429) mediante la implementación de planes de contingencia (datos de respaldo) para asegurar la continuidad del pipeline, se tenía presente usar User_agent también.

    Integración: Al unir ventas con el catálogo se aplicó un left join para conservar todas las transacciones aunque falte información del catálogo.

5. Resultados y Estado Final

    El dataset quedó normalizado, sin valores nulos y sin outliers extremos. Se exportaron reportes en Excel y CSV listos para usar en herramientas de visualización o en modelos predictivos.

## Avance por Clases
### Clase 1: Cimentación con NumPy
- Generación de un conjunto de datos ficticios de clientes y transacciones.
- Implementación de operaciones estadísticas básicas para análisis preliminar.
- Exportación de datos en formato (`.npy`).

### Clase 2: Estructuración con Pandas
- Transformación de arreglos a **DataFrames**.
- Exploración de datos usando `.describe()`, `.info()` y `.value_counts()`.
- Aplicación de **filtros condicionales** para segmentar transacciones.
- Exportación a formato **CSV** para estandarización de procesos.

### Clase 3: Extracción Multi-fuente
- Implementación de `read_csv` con optimización de tipos de datos (`dtype`).
- Manejo de archivos Excel mediante `read_excel` y  `openpyxl`.
- **Web Scraping** básico: Consumo de APIs y manejo de peticiones mediante requests y urllib para capturar indicadores económicos.
- Se aplicó `utf-8` y `latin1` para evitar errores de lectura

### Clase 4: Manejo de Valores Perdidos y Outliers
- Uso de `isnull().sum()` para dimensionar la falta de datos.
- Aplicación de la **Mediana** para montos mitigando el sesgo de valores extremos.
- Aplicación de la **Moda** para cantidad.
- Detección y filtrado de outliers con **Rango Intercuartílico (IQR)**.
- Reducción de ruido en el dataset y creación de `dataset_limpio.csv`.

### Clase 5: Data Wrangling y Enriquecimiento
- Segmentación de transacciones en categorías de clientes por Segmento Etario (Joven, Adulto, Sénior) y nivel de gasto (Bronce, Plata, Oro).
- Uso de funciones **Lambda**: Creación de un Score de Actividad normalizado (0-1) para identificar el compromiso del cliente.
- Renombramiento de columnas y reordenamiento estratégico de filas para mejorar el reporte final.
- Conversión de tipos de datos (`astype`) para asegurar la eficiencia en el procesamiento de grandes volúmenes.

### Clase 6: Agrupamiento, Pivoteo e Integración Final
- Consolidación con `pd.merge()` con el catálogo de productos (leftjoin).
- Implementación de `groupby()` con funciones estadísticas (`agg`) para extraer métricas clave.
- Creación de **Tablas Pivot** para análisis cruzado de categorías de productos con segmentos de precio.
- Generación de reportes finales en formatos CSV y Excel para la toma de decisiones gerenciales.

---

## Conclusión del Proyecto
Se ha implementado un flujo de datos (Pipeline) completo que:
1. **Obtiene** datos de fuentes heterogéneas (NumPy, CSV, Excel, Web).
2. **Limpia** errores, nulos y outliers (IQR).
3. **Transforma** y enriquece la información (Lambda, Binning).
4. **Analiza** y reporta resultados mediante agrupaciones complejas.

**El dataset final es confiable, estructurado y está listo para ser consumido por modelos de Machine Learning o herramientas de visualización.**
