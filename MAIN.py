
#Snapshot 1.0.2

#Importacion de funciones:

import numpy as np
import matplotlib.pylab as plt
from PyAstronomy import pyasl
from matplotlib.widgets import Slider

#Funcion
def puntos_lagrange(masa1,masa2,distancia):
  '''
  La función get_lagrange, propia de PyAstronomy, ya calcúla los puntos de lagrange, lo que es un problema menos, 
  ya que así nos podemos enfocar más a fondo en la personalizacion de la visualización de estos datos y el potencial
  de roche, y no en su obtención como tal.
  '''
  #De momento la distancia no tiene utilizad, pero se utilizará en un futuro
  def update(val):
    '''
    Actualiza los parámetros del grafico en funcion del cambio en el Slider interactivo de la variable m: (m2/m1)
    '''
    global m, l1, l2, l3, l4, l5

    m = slider_m.val
    if m == 1:
      # Establece un valor pequeño cercano a 1 para evitar errores en la función rochepot_dl
      m = 0.99999999
    
    # Obtener valores dimensionales del potencial de Roche
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

    ax.clear()
    ax.contourf(p, levels, extent=[-2, 3, -2, 2])
    ax.scatter(0,0,s=300, color='yellow',label='Masa 1', edgecolor='black')
    ax.scatter(1,0,s=130,color='cyan', label='Masa 2', edgecolor='black')
    ax.scatter(l1, 0, label='L1', edgecolor='black')
    ax.scatter(l2, 0, label='L2', edgecolor='black')
    ax.scatter(l3, 0, label='L3', edgecolor='black')
    ax.scatter(l4[0], l4[1], label='L4', edgecolor='black')
    ax.scatter(l5[0], l5[1], label='L5', edgecolor='black')
    ax.legend()
    ax.grid()
    ax.set_title('Roche lobe  \n  Interactive menu')
    
    
  #Parametros:
  m1= masa1 #Objeto más pesado [Kg](central)
  m2= masa2 #Objeto más liviano [Kg]](el que orbite alrededor del objeto más pesado)
  d= distancia # distancia entre los 2 objetos [?]

  #Variables:
  m= m2/m1# m2/m1 #Mass ratio
  M = m
  x, y = np.linspace(-2, 3, 300), np.linspace(-2, 2, 300) #Posición
  X, Y = np.meshgrid(x, y)

  #Parametros del gráfico
  fig, ax = plt.subplots()
  plt.subplots_adjust(left=0.1, right=0.8, bottom=0.1)

  #Slider
  slider_ax = plt.axes([0.85, 0.1, 0.155, 0.7775])  # [left, bottom, width, height]
  slider_m = Slider(slider_ax, 'm2/m1', M, 1.0, valinit=m, valstep=0.0001, orientation="vertical")

  # Actualizar el gráfico cuando se cambia el valor del slider
  slider_m.on_changed(update)

  # Graficar los datos iniciales
  update(m)

  # Mostrar el gráfico
  plt.show()

  #Output:
  return {l1,l2,l3,l4,l5}

#MAIN
#Datos de ejemplo: (en un futuro debería ser el usuario el que ingrese estos valores)
#Establecer en el input que m1 => m2
moon = 7.3477e22 #[Kg]1.898e27#
earth = 5.97219e24 #[Kg]1.989e30#
distance = 384399 #[Km]

print(puntos_lagrange(earth,moon,distance))
