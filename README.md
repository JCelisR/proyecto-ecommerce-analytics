# proyecto-ecommerce-analytics
# Proyecto cierre módulo 3: Análisis de E-commerce

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de un flujo de trabajo automatizado para la obtención, limpieza y estructuración de datos de una empresa de e-commerce. El objetivo es transformar datos crudos provenientes de múltiples fuentes (CSV, Excel, Web) en un dataset confiable listo para modelos de Machine Learning y reportes estratégicos.

## ¿Qué utilizar?
- **Lenguaje:** Python 3.x
- **Librerías Principales:** 
        - `NumPy`: Para manipulación de datos numéricos y generación de datos sintéticos.
        - `Pandas`: Para limpieza, transformación y análisis estructural.
- **Entorno:** Google Colab / VS Code.
- **Control de Versiones:** GitHub.

## Estructura del Repositorio
- `notebooks/`: Cuadernos de experimentación (Google Colab).
- `data/`: Archivos generados y datasets procesados.
- `scripts/`: Código fuente en formato `.py` para procesos automatizados.

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
