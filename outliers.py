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

#histograma
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes con outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()

#gráfica de caja
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["ventas_precios_corrientes"]

percentile25 = y.quantile(0.25) #Q1
percentile75 = y.quantile(0.75) #Q3
iqr = percentile75 - percentile25

Limite_Superior_iqr = percentile75 + 1.5*iqr
Limite_Inferior_iqr = percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

#Encontramos Ouliers
outliers_iqr= df[(y>Limite_Superior_iqr)|(y<Limite_Inferior_iqr)]
outliers_iqr

#Obtenemos datos limpios
data_clean_iqr = df[(y < Limite_Superior_iqr)&(y > Limite_Inferior_iqr)]
print(data_clean_iqr)

#Realizamos diagrama de caja o bigote con datos limpios
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corrientes")
plt.show() #dibujamos el diagrama

#histograma con datos limpios
fig = plt.figure(figsize =(7, 3))
plt.hist(x = data_clean_iqr["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes sin outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()

data_clean_iqr["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes.csv')