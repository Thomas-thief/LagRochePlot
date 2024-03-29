# Lagrange_points
Project of software development


## Descripción del proyecto:

Herramienta gráfica para visualizar los puntos de Lagrange y potencial de Roche de objetos celestes con parámetros ingresados por el usuario, con una interfáz interactiva donde el usuario podrá observar como gracias a un slider con el cúal irán variando los parametrós, y en consecuencia la visualizacion de los puntos y el potencial.


## Dependencias para su funcionamiento:

* Numpy(Version: >= 1.7)
* Matpllotlib(Version >= 3.0.0)
* PyAstronomy(Version = 0.20.0)
* SciPy(Version = 1.11.1)


## Como usar:

* Parametros:
  * Masa1 (Float) = Masa del objeto más masivo, al tratarse de numeros grandes,en kilogramos. Se puede expresar como potencia de 10 con Numpy(Ej: 1e10)
  * Masa2 (Float) = Masa del objeto menos másivo en comparacion al primero, en kilogramos. Se puede expresar como potencia de 10 con Numpy(Ej: 1e10)
  * Distancia (Float) = Distancia entre los dos objetos, en kilometros. Se puede expresar como potencia de 10 con Numpy(Ej: 1e10)

```
# Importación del módulo:
from LagRochePlot import LagRoche

# Variables a utilizar:
# Se escogen m1, m2 y distancia(por defecto en 100, 20 y 1 respectivamente):
    
m1 = 5.97219e24      # Masa tierra [kg]
m2 = 7.3477e22       # Masa luna [kg]
dist = 0.00256955529 # Distancia tierra-luna [UA]

# Restricción: m1 >= m2
# Ejecución del módulo:
LagRoche.Plot(m1,m2,dist)
```

## Funciones dentro le la clase principal

**__init__(m1 = 100, m2 = 20, dis = 1):**
  **Parámetros de entrada:** 
   * self: Asignado a elementos propios de la clase.	
   * m1 [Kg] (Float): Masa del cuerpo más masivo. Por defecto = 100.
   * m2 [kg] (Float): Masa del segundo cuerpo. Por defecto = 20.
   * dis [UA] (Float): Distancia entre los dos cuerpos. Por defecto =1.

  **Funcionalidad:**
   * Asigna los parámetros iniciales de masas, distancias, posición y un contador k. Crea variables vacías para el potencial de roche y los puntos lagrangianos.
   * Define los parámetros estéticos del gráfico.
   * Crea los Sliders de masa 1, masa 2 y distancia.
   * Crea dos botones:
     * save: Activa la variable de evento que llama a la función save_plot().
     * lag: Activa la variable de evento que llama a función lag_plt().
   * Utiliza la función self.plot() para hacer el primer gráfico.


**calculo(self):**
  **Parámetros de entrada:** 
   * self: Asignado a elementos propios de la clase.	

  **Funcionalidad:**
   * Calcula las coordenadas de los 5 puntos de Lagrange junto con el potencial de Roche


**update_plot(self, val):**
  **Parámetros de entrada:**
   * self: Asignado a elementos propios de la clase.	
   * val: Variable de valor de los datos cambiados por los Sliders.

  **Funcionalidad:**
   * Actualiza los valores de las masas y las distancias según la variable de valor cambiada por los Sliders de las masas y de la distancia.
   * Utiliza la función self.calculo() para calcular los parámetros necesarios
   * Borra el gráfico antiguo para crear uno nuevo con los nuevos parámetros.


**save_plot(self, event):**
  **Parámetros de entrada:**
   * self: Asignado a elementos propios de la clase.	
   * event: Variable de evento que se activa desde el botón save

  **Funcionalidad:**
   * Es activada a través de la variabilidad de evento accionada desde el botón save, dentro de la interfaz interactiva.
   * Revisa si es que existe una carpeta llamada ‘gráficos’ dentro del escritorio, si no, crea una
   * Guarda una imagen del gráfico dentro de la carpeta ‘gráficos’.

**lag_plt(self, event):**
  **Parámetros de entrada:**
   * self: Asignado a elementos propios de la clase.	
   * event: Variable de evento que se activa desde el botón lag
  **Funcionalidad:**
   * Es activada a través de la variabilidad de evento accionada desde el botón save, dentro de la interfaz interactiva.
   * Imprime las coordenadas de los puntos de lagrange en unidades astronómicas con respecto a la masa 1.

**plot(self):**
  **Parámetros de entrada:**
   * self: Asignado a elementos propios de la clase.	
  **Funcionalidad:**
   * Utiliza las funciones self.calculo() y self.update_plot() para obtener los parámetros iniciales
   * Plotea el gráfico.

