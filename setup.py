import setuptools

#Si tienes un readme
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='lagrange_points',  #nombre del paquete
    version='1.1.2', #versión
    license = 'MIT',
    author="Thomas Salazar; Esteban Sanchez; Sebastian Lopez; Andres Rumillanca", #autor
    author_email="thomas.salazar@usach.cl", #email
    description="un paquete para encontrar y graficar los puntos de Lagrange y potenciales de Roche de dos cuerpos", #Breve descripción
    long_description=long_description,
    install_requires = ['numpy','matplotlib', 'PyAstronomy']
    
    
) #aquí añadimos información sobre el lenguaje usado, el tipo de licencia, etc.
