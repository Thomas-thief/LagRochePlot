
#Snapshot 1.1.2

#Importacion de funciones:

import numpy as np
import matplotlib.pylab as plt
from PyAstronomy import pyasl
from matplotlib.widgets import Slider, Button

#Clase
class LagRochePlot:
    '''
  La función get_lagrange, propia de PyAstronomy, ya calcúla los puntos de lagrange, lo que es un problema menos, 
  ya que así nos podemos enfocar más a fondo en la personalizacion de la visualización de estos datos y el potencial
  de roche, y no en su obtención como tal.
  '''
    def __init__(self,m1=100,m2=20,dis=1):
        '''
        Configura todos los parametros iniciales junto a los intercatuables.
        '''

        self.m1 = m1
        self.m2= m2
        self.m = m2/m1  # Valor inicial de q
        self.dis = dis

        plt.style.use(['dark_background'])
        self.fig, self.ax = plt.subplots()  # Crea la figura y los ejes
        plt.subplots_adjust(left=0.14, right=0.78, bottom=0.2)  # Ajusta los márgenes
        
        self.slider_m1_ax = plt.axes([0.80, 0.07, 0.03, 0.7575])  # Posición y tamaño del slider
        self.slider_m1 = Slider(self.slider_m1_ax, 'Masa\n1', self.m1/2, 1.5*self.m1, valinit=self.m1, valstep=0.1, orientation="vertical")  # Crea el slider

        self.slider_m2_ax = plt.axes([0.86, 0.07, 0.03, 0.7575])  # Posición y tamaño del slider
        self.slider_m2 = Slider(self.slider_m2_ax, 'Masa\n2', self.m2/2, self.m1/2, valinit=self.m2, valstep=0.1, orientation="vertical")  # Crea el slider

        self.slider_dis_ax = plt.axes([0.93, 0.07, 0.03, 0.7575])  # Posición y tamaño del slider
        self.slider_dis = Slider(self.slider_dis_ax, 'Distancia', self.dis, 100.0, valinit=self.dis, valstep=0.1, orientation="vertical")  # Crea el slider

        self.button_save_ax = plt.axes([0.02, 0.02, 0.11, 0.065])  # Posición y tamaño del botón
        self.button_save = Button(self.button_save_ax, 'Guardar',  color='black')  # Crea el botón

        self.button_lag_ax = plt.axes([0.14, 0.02, 0.43, 0.065])  # Posición y tamaño del botón
        self.button_lag = Button(self.button_lag_ax, 'Coordenadas de Puntos de Lagrange',  color='black')  # Crea el botón

        self.k = 1  # Contador para nombres de archivos

        self.x, self.y = np.linspace(-2, 3, 300), np.linspace(-2, 2, 300)  # Valores para la malla
        self.xx, self.yy = np.meshgrid(self.x, self.y)  # Crea la malla   
        self.p = None  # Variable para almacenar el potencial
        self.l1, self.l2, self.l3, self.l4, self.l5 = None, None, None, None, None  # Variables para almacenar los puntos de Lagrange
        self.l1pot, self.l2pot, self.l3pot, self.l4pot, self.l5pot = None, None, None, None, None  # Variables para almacenar los potenciales de Lagrange

        self.slider_m1.on_changed(self.update_plot)  # Conecta el evento del slider a la función de actualización del gráfico
        self.slider_m2.on_changed(self.update_plot)  # Conecta el evento del slider a la función de actualización del gráfico
        self.slider_dis.on_changed(self.update_plot)  # Conecta el evento del slider a la función de actualización del gráfico
        self.button_save.on_clicked(self.save_plot)  # Conecta el evento del botón a la función de guardar el gráfico
        self.button_lag.on_clicked(self.lag_pts)


        self.plot()  # Llama a la función para trazar el gráfico inicial

    def calculo(self):
        '''
        Calcula los valores de los puntos de Lagrange y los potenciales asociados.
        '''
        self.p = pyasl.rochepot_dl(self.xx, self.yy, 0, self.m)  # Calcula el potencial de Roche self.m1, self.m2, self.a
        self.l1, self.l1pot = pyasl.get_lagrange_1(self.m)  # Calcula el punto de Lagrange L1
        self.l2, self.l2pot = pyasl.get_lagrange_2(self.m)  # Calcula el punto de Lagrange L2
        self.l3, self.l3pot = pyasl.get_lagrange_3(self.m)  # Calcula el punto de Lagrange L3
        self.l4, self.l5 = pyasl.get_lagrange_4(), pyasl.get_lagrange_5()  # Calcula los puntos de Lagrange L4 y L5
        self.l4pot = pyasl.rochepot_dl(self.l4[0], self.l4[1], self.l4[2], self.m)  # Calcula el potencial de Roche para L4
        self.l5pot = pyasl.rochepot_dl(self.l5[0], self.l5[1], self.l5[2], self.m)  # Calcula el potencial de Roche para L5

    def update_plot(self, val):
        '''
        Actualiza el gráfico cuando se cambia el valor del slider.
        '''
        self.m1 = self.slider_m1.val # Obtiene el valor actual del slider
        self.m2 = self.slider_m2.val # Obtiene el valor actual del slider
        self.m = self.m2/self.m1  
        self.dis = self.slider_dis.val # Obtiene el valor actual del slider

        if self.m == 1:
            self.m = 0.99999999  # Evita errores al usar el potencial de Roche
             

        self.calculo()  # Calcula los valores necesarios para el trazado del gráfico

        level = sorted([self.l5pot, self.l4pot, self.l3pot, self.l2pot, self.l1pot])
        levels = np.linspace(level[0],level[-1], 20)

        self.ax.clear()  # Limpia los ejes antes de actualizar el gráfico
        self.ax.contour(self.p,levels, alpha=0.8, extent=[-2*self.dis, 3*self.dis, -2*self.dis, 2*self.dis], cmap='Greys')  # Rellena los contornos 
        self.ax.scatter(0, 0, marker='o', color='yellow', edgecolor='white', s=300,label='Masa 1')  # Dibuja el punto central
        self.ax.scatter(1*self.dis, 0, marker='o', color='cyan', edgecolor='white', s=100,label='Masa 2')  # Dibuja el segundo punto
        self.ax.scatter(self.l1*self.dis, 0, label='L1', edgecolor='white',s=60)  # Dibuja el punto L1
        self.ax.scatter(self.l2*self.dis, 0, label='L2', edgecolor='white',s=60)  # Dibuja el punto L2
        self.ax.scatter(self.l3*self.dis, 0, label='L3', edgecolor='white',s=60)  # Dibuja el punto L3
        self.ax.scatter(self.l4[0]*self.dis, self.l4[1]*self.dis, label='L4', edgecolor='white',s=60)  # Dibuja el punto L4
        self.ax.scatter(self.l5[0]*self.dis, self.l5[1]*self.dis, label='L5', edgecolor='white',s=60)  # Dibuja el punto L5
        self.ax.set_title("LagRochePlot", fontname='Georgia',fontsize=30)  # Establece el título del gráfico
        self.ax.set_xlabel("Distancia en el eje x [AU]", fontname='Georgia', fontsize=12)  # Etiqueta del eje x
        self.ax.set_ylabel("Distancia en el eje y [AU]", fontname='Georgia', fontsize=12)  # Etiqueta del eje y
        self.ax.legend()
        self.ax.grid(alpha=0.3)

    def save_plot(self, event):
        '''
        Guarda el gráfico con un nombre único.
        '''
        plt.savefig(f'LagRochePlot N°{self.k}')
        print(f'LagRochePlot N°{self.k}, guardado')
        self.k += 1
        plt.show()
    
    def lag_pts(self,event):
        print(f'puntos de Lagrange con origen en la masa 1: \n L1=[{self.l1*self.dis},0]\n L2=[{self.l2*self.dis},0]\n L3=[{self.l3*self.dis},0]\n L4=[{self.l4[0]*self.dis}, {self.l4[1]*self.dis}]\n L5=[{self.l5[0]*self.dis}, {self.l5[1]*self.dis}]\n')


    def plot(self):
        '''
        Realiza el trazado inicial del gráfico.
        '''
        self.calculo()  # Calcula los valores iniciales para el trazado del gráfico
        self.update_plot(0)  # Actualiza el gráfico inicial
        plt.show()


#Datos de ejemplo: (en un futuro debería ser el usuario el que ingrese estos valores)
#Establecer en el input que m1 => m2
#moon = 7.3477e22 #[Kg]
#earth = 5.97219e24 #[Kg]
#distance = 384399000/149597870700 #[AU]

#LagRochePlot(earth,moon,distance)