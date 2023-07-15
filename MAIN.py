
#Snapshot 1.1.1

#Importacion de funciones:
import numpy as np
import matplotlib.pylab as plt
from PyAstronomy import pyasl

#Funcion principal:
def puntos_lagrange(masa1,masa2,distancia):
  #De momento la distancia no tiene utilizad, pero se utilizará en un futuro

  #Parametros:
  m1= masa1 #Objeto más pesado [Kg](central)
  m2= masa2 #Objeto más liviano [Kg]](el que orbite alrededor del objeto más pesado)
  d= distancia # distancia entre los 2 objetos [km]

  #Variables:
  m=  m2/m1 #Mass ratio

  #Puntos l1/l2/l3:
  '''
  La función get_lagrange, propia de PyAstronomy, ya calcúla los puntos de lagrange, lo que es un problema menos, 
  ya que así nos podemos enfocar más a fondo en la personalizacion de la visualización de estos datos y el potencial
  de roche, y no en su obtención como tal.
  '''
  l1 = pyasl.get_lagrange_1(m, getdlrp=False)
  l2 = pyasl.get_lagrange_2(m, getdlrp=False)
  l3 = pyasl.get_lagrange_3(m, getdlrp=False)
  #Puntos l4/l5
  l4, l5 = pyasl.get_lagrange_4(), pyasl.get_lagrange_5()

  ##Grafica de los puntos:
  plt.scatter(0,0,s=300, color='yellow',label='Masa 1')
  plt.scatter(1,0,s=130,color='black', label='Masa 2')
  plt.scatter(l1, 0, label='L1')
  plt.scatter(l2, 0, label='L2')
  plt.scatter(l3, 0, label='L3')
  plt.scatter(l4[0], l4[1], label='L4')
  plt.scatter(l5[0], l5[1], label='L5')
  plt.legend()
  plt.grid()
  plt.show()
  
  #Output de la función:
  return {l1,l2,l3,l4,l5}

#Datos de ejemplo: (en un futuro debería ser el usuario el que ingrese estos valores)
#PD: Establecer en el input que m1 != m2 y m1 > m2
moon = 1.898e27#7.3477e22 #[Kg]
earth = 1.989e30#5.97219e24 #[Kg]
distance = 384399 #[Km]

#Output con llamado a función:
print(puntos_lagrange(earth,moon,distance))
