# Lagrange_points
Project of software development

#Descripción del proyecto:

Herramienta gráfica para visualizar los puntos de Lagrange y potencial de Roche de objetos celestes con parámetros ingresados por el usuario, con una interfáz interactiva donde el usuario podrá observar como gracias a un slider con el cúal irán variando los parametrós, y en consecuencia la visualizacion de los puntos y el potencial.


#Dependencias para su funcionamiento:

* Numpy(Version: >= 1.7)
* Matpllotlib(Version >= 3.0.0)
* PyAstronomy(Version = 0.20.0)

#Como usar:(Example ejecution)

NombredeFuncion(Masa1,Masa2,Distancia, opcional)

*Parametros:
  *Masa1 (Float)= Masa del objeto más masivo, al tratarse de numeros grandes,en kilogramos. Se puede expresar como potencia de 10 con Numpy(Ej: 1e10)
  *Masa2 (Float)= Masa del objeto menos másivo en comparacion al primero, en kilogramos. Se puede expresar como potencia de 10 con Numpy(Ej: 1e10)
  *Distancia (Float)= Distancia entre los dos objetos, en kilometros. Se puede expresar como potencia de 10 con Numpy(Ej: 1e10)
