import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
#? Generar un array con las edades de todos los estudiantes de segundo año:
edades = [21, 20, 20, 19, 28, 21, 18, 21, 25, 19, 20, 20, 21, 19, 19, 21, 19, 25, 25, 19, 19, 20, 21, 20, 19, 24, 22, 19, 34, 20, 26, 27, 20, 20, 25, 25, 19, 19, 24, 19, 23, 19, 19, 19, 30, 20, 22]
#? Mostrar las edades por pantalla.
print("Edades de 2do ano: ", *edades)
#? ¿Qué tipo de variable representan las edades de los estudiantes?
#* Las edades de los estudiantes se representan con variables cuantitativas discretas
#? 2) Medidas estadísticas
#? Calcular:
#? Mostrar todos los resultados.

#? ● Media 
media = np.mean(edades)
print("Media: ",media)

#? ● Mediana
mediana = np.median(edades)
print("Mediana: ",mediana)

#? ● Moda 
# !(se calcula con panda)
moda = pd.Series(edades).mode()[0]
print("Moda: ", moda)

#? ● Varianza
varianza = np.var(edades)
print('Varianza:', varianza)

#? ● Desviación estándar
desviacion_estandar = np.std(edades)
print('Desviacion:', desviacion_estandar)

#? ● Rango
rango = np.max(edades) - np.min(edades)
print('Rango:', rango)

#Punto 3: Q1: El 25% de los alumnos tiene 19 años o menos.
#Q2: El 50% de la clase tiene 20 años o menos.
#Q3: El 75% de la clase tiene hasta 23.5 años.


#Percentiles, utilizamos Numpy
Q1 = np.percentile(edades, 25)
Q2 = np.percentile(edades, 50)
Q3 = np.percentile(edades, 75)

print("Percientil 25 ", Q1)
print("Percientil 50 ", Q2)
print("Percientil 75 ", Q3)

#Histograma de Frecuencia
#Configuraciones
#.hist es para hacer este tipo de graficos, luego agregarmos las configuraciones basicas como color,borde, cant_datos y array
plt.hist(edades, bins=10, color="red", edgecolor="black")
plt.title("Distribucion de edades", fontsize=14)  # Titulo
#Determinamos Eje X e Y
plt.xlabel("edades", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.show()  # Mostrar grafico determinado