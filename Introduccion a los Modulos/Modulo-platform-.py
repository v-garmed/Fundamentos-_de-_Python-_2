import platform

print(platform.platform())  # Muestra la plataforma en la que se está ejecutando el código
print(platform.platform(1))    # Muestra el sistema operativo
print(platform.platform(0,1))  # Muestra el nombre del sistema operativo

print(platform.machine())  # Muestra el tipo de máquina (arquitectura)
print(platform.processor())  # Muestra el procesador
print(platform.system())  # Muestra el sistema operativo

print(platform.version())   # Muestra la versión del sistema operativo

print(platform.python_implementation)
for atr in platform.python_version_tuple():
    print(atr, end="\t")  # Muestra la versión de Python en forma de tupla