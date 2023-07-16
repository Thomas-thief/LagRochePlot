
#Snapshot 1.1.2

#Importacion de funciones:

import numpy as np
import matplotlib.pylab as plt
from PyAstronomy import pyasl

#Funcion
def puntos_lagrange(masa1,masa2,distancia):
  '''
  La función get_lagrange, propia de PyAstronomy, ya calcúla los puntos de lagrange, lo que es un problema menos, 
  ya que así nos podemos enfocar más a fondo en la personalizacion de la visualización de estos datos y el potencial
  de roche, y no en su obtención como tal.
  '''
  #De momento la distancia no tiene utilizad, pero se utilizará en un futuro
  
  #Parametros:
  m1= masa1 #Objeto más pesado [Kg](central)
  m2= masa2 #Objeto más liviano [Kg]](el que orbite alrededor del objeto más pesado)
  d= distancia # distancia entre los 2 objetos [?]

  #Variables:
  m= m2/m1# m2/m1 #Mass ratio
  x, y = np.linspace(-2, 3, 300), np.linspace(-2, 2, 300) #Posición
  X, Y = np.meshgrid(x, y)
  p = pyasl.rochepot_dl(X, Y, 0, m) #potencial

  #Puntos l1/l2/l3 y sus potenciales:
  l1, l1pot = pyasl.get_lagrange_1(m)
  l2, l2pot = pyasl.get_lagrange_2(m)
  l3, l3pot = pyasl.get_lagrange_3(m)
  #Puntos l4/l5 y sus potenciales
  l4, l5 = pyasl.get_lagrange_4(), pyasl.get_lagrange_5()
  l4pot = pyasl.rochepot_dl(l4[0], l4[1], l4[2], m)
  l5pot = pyasl.rochepot_dl(l5[0], l5[1], l5[2], m)

  #grafico
  level= l4pot*1.005, l3pot, l2pot, l1pot
  levels = sorted(level)

  plt.contourf(p, levels, extent=[-2, 3, -2, 2])
  plt.scatter(0,0,s=300, color='yellow',label='Masa 1', edgecolor='black')
  plt.scatter(1,0,s=130,color='cyan', label='Masa 2', edgecolor='black')
  plt.scatter(l1, 0, label='L1', edgecolor='black')
  plt.scatter(l2, 0, label='L2', edgecolor='black')
  plt.scatter(l3, 0, label='L3', edgecolor='black')
  plt.scatter(l4[0], l4[1], label='L4', edgecolor='black')
  plt.scatter(l5[0], l5[1], label='L5', edgecolor='black')
  plt.legend()
  plt.grid()
  plt.title('Roche lobe')
  plt.show()
  print(m)
  
  #Output:
  return {l1,l2,l3,l4,l5}

#Datos de ejemplo: (en un futuro debería ser el usuario el que ingrese estos valores)
#Establecer en el input que m1 => m2
moon = 7.3477e22 #[Kg]1.898e27#
earth = 5.97219e24 #[Kg]1.989e30#
distance = 384399 #[Km]

print(puntos_lagrange(earth,moon,distance))
