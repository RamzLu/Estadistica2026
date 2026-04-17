import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#? Generar un array con las edades de todos los estudiantes de segundo año:
edades = [21, 20, 20, 19, 28, 21, 18, 21, 25, 19, 20, 20, 21, 19, 19, 21, 19, 25, 25, 19, 19, 20, 21, 20, 19, 24, 22, 19, 34, 20, 26, 27, 20, 20, 25, 25, 19, 19, 24, 19, 23, 19, 19, 19, 30, 20, 22]
#? Mostrar las edades por pantalla.
print("Edades de 2do ano: ", *edades)
#? ¿Qué tipo de variable representan las edades de los estudiantes?
#* Las edades de los estudiantes se representan con variables cuantitativas discretas
#? 2) Medidas estadísticas
#? Calcular:
#? ● Desviación estándar
#? ● Rango
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
