from tareas.tarea_pokemon.a_cargar import datos # DataFrame con los datos de los Pokémon
"""
3. Estadística descriptiva básica
---------------------------------
- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
- ¿Cuántos Pokémon tienen dos tipos?
- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
"""

import numpy as np

print('Estadísticas básicas del ataque de los Pokémon')
print()

# Promedio, mediana y moda del ataque de todos los Pokémon
promedio_de_ataque_todos_pokemon = round(datos['Ataque'].mean(), 2)
mediana_de_ataque_todos_pokemon = round(datos['Ataque'].median(), 2)
moda_de_ataque_todos_pokemon = round(datos['Ataque'].mode()[0], 2)

print('Promedio de ataque:', promedio_de_ataque_todos_pokemon)
print('Mediana de ataque:', mediana_de_ataque_todos_pokemon)
print('Moda de ataque:', moda_de_ataque_todos_pokemon)
print()

# Pokémon con mayor defensa y menor velocidad
nombre_pokemon_con_mayor_defensa = datos.loc[datos['Defensa'].idxmax()]['Nombre']
nombre_pokemon_con_menor_velocidad = datos.loc[datos['Velocidad'].idxmin()]['Nombre']
valor_mayor_defensa = datos["Defensa"].max()
valor_menor_velocidad = datos["Velocidad"].min()

print('Pokémon con mayor defensa:', nombre_pokemon_con_mayor_defensa, 'con defensa', valor_mayor_defensa)
print('Pokémon con menor velocidad:', nombre_pokemon_con_menor_velocidad, 'con velocidad', valor_menor_velocidad)
print()

# Cantidad de Pokémon con dos tipos
cantidad_pokemon_con_dos_tipos = datos[datos['Tipo 2'].notnull()].shape[0]
print('Cantidad de Pokémon con dos tipos:', cantidad_pokemon_con_dos_tipos)
print()

# Rango y desviación estándar de los PS (Puntos de Salud)
rango_puntos_de_salud = np.ptp(datos['PS'])
desviacion_estandar_puntos_de_salud = round(datos['PS'].std(), 2)

print('Rango de PS:', rango_puntos_de_salud)
print('Desviación estándar de PS:', desviacion_estandar_puntos_de_salud)
print()
from tareas.tarea_pokemon.a_cargar import datos # DataFrame con los datos de los Pokémon
"""
3. Estadística descriptiva básica
---------------------------------
- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
- ¿Cuántos Pokémon tienen dos tipos?
- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
"""

import numpy as np

print('Estadísticas básicas del ataque de los Pokémon')
print()

# Promedio, mediana y moda del ataque de todos los Pokémon
promedio_de_ataque_todos_pokemon = round(datos['Ataque'].mean(), 2)
mediana_de_ataque_todos_pokemon = round(datos['Ataque'].median(), 2)
moda_de_ataque_todos_pokemon = round(datos['Ataque'].mode()[0], 2)

print('Promedio de ataque:', promedio_de_ataque_todos_pokemon)
print('Mediana de ataque:', mediana_de_ataque_todos_pokemon)
print('Moda de ataque:', moda_de_ataque_todos_pokemon)
print()

# Pokémon con mayor defensa y menor velocidad
nombre_pokemon_con_mayor_defensa = datos.loc[datos['Defensa'].idxmax()]['Nombre']
nombre_pokemon_con_menor_velocidad = datos.loc[datos['Velocidad'].idxmin()]['Nombre']
valor_mayor_defensa = datos["Defensa"].max()
valor_menor_velocidad = datos["Velocidad"].min()

print('Pokémon con mayor defensa:', nombre_pokemon_con_mayor_defensa, 'con defensa', valor_mayor_defensa)
print('Pokémon con menor velocidad:', nombre_pokemon_con_menor_velocidad, 'con velocidad', valor_menor_velocidad)
print()

# Cantidad de Pokémon con dos tipos
cantidad_pokemon_con_dos_tipos = datos[datos['Tipo 2'].notnull()].shape[0]
print('Cantidad de Pokémon con dos tipos:', cantidad_pokemon_con_dos_tipos)
print()

# Rango y desviación estándar de los PS (Puntos de Salud)
rango_puntos_de_salud = np.ptp(datos['PS'])
desviacion_estandar_puntos_de_salud = round(datos['PS'].std(), 2)

print('Rango de PS:', rango_puntos_de_salud)
print('Desviación estándar de PS:', desviacion_estandar_puntos_de_salud)
print()
