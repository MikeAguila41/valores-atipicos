import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Cargar archivo csv desde equipo
#from google.colab import files
#files.upload()

df= pd.read_csv('Ventas_totales_sinnulos.csv', index_col=0)
#df.head()

#Estoy utilizando el archivo de ventas totales ya limpios y sin 
#valores nulos. Ya que esto fue realizo anteriormente en otra actividad. 
#Por lo que ahora ya no hago limpieza del archivo ya que este ya se encuentra sin nulos

valores_nulos = df.isnull().sum()
#print(valores_nulos)

# columna 'ventas_precios_corrientes'
#histograma
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes con outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

#gráfica de caja
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["ventas_precios_corrientes"]
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
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corrientes (método cuartiles)")
#plt.show() #dibujamos el diagrama

#histograma con datos limpios
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes sin outliers (método de cuartiles)')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

#Método aplicando desviación estandar. Encuentro los valores extremos
y = df["ventas_precios_corrientes"]
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
plt.hist(x = data_clean_iqr_desv_std["ventas_precios_corrientes"], color='green', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes con desviación estándar')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()

#Realizamos diagrama de caja o bigote con datos limpios con desv_std
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_desv_std["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corrientes (método cuartiles)")
#plt.show() #dibujamos el diagrama

data_clean_iqr["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes.csv')
# se utiliza el método de quartiles para la columna 'ventas_precios_corrientes' ya que no elimina los nulos con las desv-std

