# Predicción de temperaturas con Redes Neuronales en TensorFlow

Este proyecto utiliza TensorFlow para entrenar una red neuronal que predice temperaturas en grados Fahrenheit a partir de temperaturas en grados Celsius. Utiliza una red con dos capas ocultas para mejorar la precisión de la predicción.

## Requisitos

- Python 3.x
- TensorFlow
- Numpy
- Matplotlib

## Instalación

Para instalar las librerías necesarias, ejecuta el siguiente comando:


## Descripción del Código

1. **Importación de librerías:** Se utilizan TensorFlow, Numpy y Matplotlib.
2. **Creación de datos:** Se definen dos arrays con temperaturas en grados Celsius y Fahrenheit.
3. **Definición del modelo:** Se crea una red neuronal con dos capas ocultas de 3 unidades cada una y una capa de salida con 1 unidad.
4. **Compilación:** Se utiliza el optimizador Adam con un valor de pérdida de error cuadrático medio.
5. **Entrenamiento:** El modelo se entrena durante 1000 épocas.
6. **Visualización de pérdida:** Se grafica la pérdida para evaluar el rendimiento.
7. **Predicción:** Se realiza una predicción de la temperatura en Fahrenheit dada una entrada en Celsius.
8. **Pesos del modelo:** Se muestran los pesos de las capas después del entrenamiento.

## Ejemplo de Predicción

El modelo predice la temperatura en Fahrenheit dada una entrada en Celsius. Por ejemplo:


## Visualización

El entrenamiento genera una gráfica de la pérdida en función del número de épocas para evaluar el rendimiento del modelo.

## Contribuciones

Si deseas contribuir, realiza un fork del repositorio y envía un pull request con tus mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT.

## Recomendaciones

- Es recomendable crear un entorno virtual para este proyecto para evitar conflictos con otras librerías instaladas globalmente.  
- Este proyecto fue desarrollado usando Python 3.11, se recomienda usar esta versión para evitar problemas de compatibilidad.

### Crear y activar un entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate


### Clonar o tener el Proyecto

1. **Clonar**: Clona el proyecto.

``bash
https://github.com/VicensFenix/RedNeuronal.git

2. **Descarga el ZIP: Si no descarguen el .zip del proyecto.