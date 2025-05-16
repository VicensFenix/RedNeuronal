# Importa Librerias
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Creando arrays para entrada y salida
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheir = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Diseñando el modelo neuronal (capas entrada y salida)
# capa = tf.keras.layers.Dense(units=1, input_shape=[1])
# modelo = tf.keras.Sequential([capa])
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

# Optimizando
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Entrenando el modelo
print("Comenzando entrenamiento ...")
historial = modelo.fit(celsius, fahrenheir, epochs=1000, verbose=False)
print("Modelo entranado!")

# Gráfica de pérdida durante el entrenamiento
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

# Creando una predicción
print("Hagamos una predicción")
resultado = modelo.predict(np.array([[100.0]]))  # Cambio en la entrada
print("El resultado es " + str(resultado[0][0]) + " Fahrenheit!")

# Mostrando los pesos del modelo después del entrenamiento
print("Variables internas del modelo:")
print("Pesos de la capa oculta 1:", oculta1.get_weights())
print("Pesos de la capa oculta 2:", oculta2.get_weights())
print("Pesos de la capa de salida:", salida.get_weights())