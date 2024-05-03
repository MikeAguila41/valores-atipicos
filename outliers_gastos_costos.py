import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Cargar archivo csv desde equipo
#from google.colab import files
#files.upload()

df= pd.read_excel('gastos_costos_20_23.xlsx')
#df.head()

#Estoy utilizando el archivo de ventas totales ya limpios y sin 
#valores nulos. Ya que esto fue realizo anteriormente en otra actividad. 
#Por lo que ahora ya no hago limpieza del archivo ya que este ya se encuentra sin nulos

valores_nulos = df.isnull().sum()
#print(valores_nulos)

# columna 'IMPORTE'
#histograma
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IMPORTE"], color='red', rwidth=0.50)
plt.title('IMPORTE')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

#gráfica de caja
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["IMPORTE"]) 
plt.title("Outliers de IMPORTE")
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["IMPORTE"]
#print(y)
percentile25 = y.quantile(0.25) #Q1
percentile75 = y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr = percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr = percentile75 + 1.5*iqr
Limite_Inferior_iqr = percentile25 - 1.5*iqr
print("Limite superior permitido usando cuartiles ", Limite_Superior_iqr)
print("Limite inferior permitido usando cuartiles ", Limite_Inferior_iqr)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior_iqr)|(y<Limite_Inferior_iqr)]
outliers_iqr

#Obtenemos datos limpios
data_clean_iqr = df[(y < Limite_Superior_iqr)&(y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

#Realizamos diagrama de caja o bigote con datos limpios
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IMPORTE"]) 
plt.title("Outliers de IMPORTE (método cuartiles)")
#plt.show() #dibujamos el diagrama

#histograma con datos limpios
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr["IMPORTE"], color='blue', rwidth=0.50)
plt.title('Histograma de IMPORTE sin outliers (método de cuartiles)')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

#Método aplicando desviación estandar. Encuentro los valores extremos
y = df["IMPORTE"]
#print(y)
Limite_Superior_desv_std = y.mean() + 3*y.std() #La fòrumla es 3 veces
Limite_Inferior_desv_std = y.mean() - 3*y.std()
print("Limite superior permitido utilizando desviación estándar ", Limite_Superior_desv_std)
print("Limite inferior permitido utilizando desviación estándar ", Limite_Inferior_desv_std)

#Obtenemos datos limpios
data_clean_iqr_desv_std = df[(y < Limite_Superior_desv_std)&(y > Limite_Inferior_desv_std)]
print(data_clean_iqr)

#histograma con desviación estándar
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr_desv_std["IMPORTE"], color='green', rwidth=0.50)
plt.title('Histograma de IMPORTE con desviación estándar')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
plt.show()

#Realizamos diagrama de caja o bigote con datos limpios con desv_std
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_desv_std["IMPORTE"]) 
plt.title("Outliers de ventas_precios_corrientes (desv_std)")
#plt.show() #dibujamos el diagrama

data_clean_iqr["IMPORTE"].to_csv('IMPORTE.csv')
# se utiliza el método de quartiles para la columna 'IMPORTE' ya que no elimina los nulos con las desv-std

# columna 'TOTAL MX'
#histograma
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL MX con outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

#gráfica de caja
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX")
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["TOTAL MX"]
#print(y)
percentile25 = y.quantile(0.25) #Q1
percentile75 = y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr = percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr = percentile75 + 1.5*iqr
Limite_Inferior_iqr = percentile25 - 1.5*iqr
print("Limite superior permitido usando cuartiles ", Limite_Superior_iqr)
print("Limite inferior permitido usando cuartiles ", Limite_Inferior_iqr)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior_iqr)|(y<Limite_Inferior_iqr)]
outliers_iqr

#Obtenemos datos limpios
data_clean_iqr = df[(y < Limite_Superior_iqr)&(y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

#Realizamos diagrama de caja o bigote con datos limpios
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX (método cuartiles)")
#plt.show() #dibujamos el diagrama

#histograma con datos limpios
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr["TOTAL MX"], color='blue', rwidth=0.50)
plt.title('Histograma de TOTAL MX sin outliers (método de cuartiles)')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

#Método aplicando desviación estandar. Encuentro los valores extremos
y = df["TOTAL MX"]
#print(y)
Limite_Superior_desv_std = y.mean() + 3*y.std() #La fòrumla es 3 veces
Limite_Inferior_desv_std = y.mean() - 3*y.std()
print("Limite superior permitido utilizando desviación estándar ", Limite_Superior_desv_std)
print("Limite inferior permitido utilizando desviación estándar ", Limite_Inferior_desv_std)

#Obtenemos datos limpios
data_clean_iqr_desv_std = df[(y < Limite_Superior_desv_std)&(y > Limite_Inferior_desv_std)]
print(data_clean_iqr)

#histograma con desviación estándar
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr_desv_std["TOTAL MX"], color='green', rwidth=0.50)
plt.title('Histograma de TOTAL MX con desviación estándar')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
plt.show()

#Realizamos diagrama de caja o bigote con datos limpios con desv_std
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_desv_std["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX (desv_std)")
#plt.show() #dibujamos el diagrama

data_clean_iqr["TOTAL MX"].to_csv('TOTAL MX.csv')
# se utiliza el método de quartiles para la columna 'TOTAL MX' ya que no elimina los nulos con las desv-std

# columna 'TOTAL SAT'
#histograma
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["TOTAL SAT"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL SAT con outliers')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

#gráfica de caja
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["TOTAL SAT"]) 
plt.title("Outliers de TOTAL SAT")
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["TOTAL SAT"]
#print(y)
percentile25 = y.quantile(0.25) #Q1
percentile75 = y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr = percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr = percentile75 + 1.5*iqr
Limite_Inferior_iqr = percentile25 - 1.5*iqr
print("Limite superior permitido usando cuartiles ", Limite_Superior_iqr)
print("Limite inferior permitido usando cuartiles ", Limite_Inferior_iqr)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior_iqr)|(y<Limite_Inferior_iqr)]
outliers_iqr

#Obtenemos datos limpios
data_clean_iqr = df[(y < Limite_Superior_iqr)&(y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

#Realizamos diagrama de caja o bigote con datos limpios
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["TOTAL SAT"]) 
plt.title("Outliers de TOTAL SAT (método cuartiles)")
#plt.show() #dibujamos el diagrama

#histograma con datos limpios
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr["TOTAL SAT"], color='blue', rwidth=0.50)
plt.title('Histograma de TOTAL SAT sin outliers (método de cuartiles)')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

#Método aplicando desviación estandar. Encuentro los valores extremos
y = df["TOTAL SAT"]
#print(y)
Limite_Superior_desv_std = y.mean() + 3*y.std() #La fòrumla es 3 veces
Limite_Inferior_desv_std = y.mean() - 3*y.std()
print("Limite superior permitido utilizando desviación estándar ", Limite_Superior_desv_std)
print("Limite inferior permitido utilizando desviación estándar ", Limite_Inferior_desv_std)

#Obtenemos datos limpios
data_clean_iqr_desv_std = df[(y < Limite_Superior_desv_std)&(y > Limite_Inferior_desv_std)]
print(data_clean_iqr)

#histograma con desviación estándar
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr_desv_std["TOTAL SAT"], color='green', rwidth=0.50)
plt.title('Histograma de TOTAL SAT con desviación estándar')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
plt.show()

#Realizamos diagrama de caja o bigote con datos limpios con desv_std
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_desv_std["TOTAL SAT"]) 
plt.title("Outliers de TOTAL SAT (método desv_std)")
#plt.show() #dibujamos el diagrama

data_clean_iqr["TOTAL SAT"].to_csv('TOTAL SAT.csv')
# se utiliza el método de quartiles para la columna 'TOTAL SAT' ya que no elimina los nulos con las desv-std