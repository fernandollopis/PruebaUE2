# Fernando Llopis
# 2019_09_01
# Creando un dataset
import pandas as pd
# Definicion variables.
nombre = ['Sara','Carmen','Pablo', 'Balmore']
genero =['Mujer','Mujer','Hombre', 'Hombre' ]
edad = [20, 21, 19, 22]
#create a dataframe
class2020 = pd.DataFrame ({'nombre': nombre, 'genero': genero, 'edad': edad})
class2020.shape
class2020.head()

#Borrado
del (nombre , genero , edad)
# Export dataframe to Excel
class2020.to_excel("class2020.xlsx")
