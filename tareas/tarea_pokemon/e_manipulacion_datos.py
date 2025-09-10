from tareas.tarea_pokemon.a_cargar import datos

"""
5. Manipulación de datos
------------------------
- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
- Ordena el DataFrame por "Poder Total" de mayor a menor.
"""

lista_columnas_para_poder_total = ['Ataque', 'Defensa', 'Velocidad', 'PS']
for columna_actual in lista_columnas_para_poder_total:
    if columna_actual not in datos.columns:
        raise KeyError(f'Columna faltante: {columna_actual}')

datos['Poder Total'] = datos['Ataque'] + datos['Defensa'] + datos['Velocidad'] + datos['PS']

datos_ordenados_por_poder_total = datos.sort_values('Poder Total', ascending=False).reset_index(drop=True)

print('Top 10 Pokémon por Poder Total (Ataque+Defensa+Velocidad+PS):')
print()
print(datos_ordenados_por_poder_total[['Nombre','Ataque','Defensa','Velocidad','PS','Poder Total']].head(10).to_string(index=False))

# Pregunta si se desea ver más
respuesta_usuario_ver_mas = input('\n¿Desea ver más Pokémon? (s/n): ').strip().lower()
if respuesta_usuario_ver_mas == 's':
    try:
        cantidad_adicional_a_mostrar = int(input('¿Cuántos más desea ver? Ingrese un número: ').strip())
        if cantidad_adicional_a_mostrar > 0:
            print(datos_ordenados_por_poder_total[['Nombre','Ataque','Defensa','Velocidad','PS','Poder Total']].head(10 + cantidad_adicional_a_mostrar).to_string(index=False))
        else:
            print('Número no válido, se mostrarán solo los 10 primeros.')
    except ValueError:
        print('Entrada no válida, se mostrarán solo los 10 primeros.')
from tareas.tarea_pokemon.a_cargar import datos

"""
5. Manipulación de datos
------------------------
- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
- Ordena el DataFrame por "Poder Total" de mayor a menor.
"""

lista_columnas_para_poder_total = ['Ataque', 'Defensa', 'Velocidad', 'PS']
for columna_actual in lista_columnas_para_poder_total:
    if columna_actual not in datos.columns:
        raise KeyError(f'Columna faltante: {columna_actual}')

datos['Poder Total'] = datos['Ataque'] + datos['Defensa'] + datos['Velocidad'] + datos['PS']

datos_ordenados_por_poder_total = datos.sort_values('Poder Total', ascending=False).reset_index(drop=True)

print('Top 10 Pokémon por Poder Total (Ataque+Defensa+Velocidad+PS):')
print()
print(datos_ordenados_por_poder_total[['Nombre','Ataque','Defensa','Velocidad','PS','Poder Total']].head(10).to_string(index=False))

# Pregunta si se desea ver más
respuesta_usuario_ver_mas = input('\n¿Desea ver más Pokémon? (s/n): ').strip().lower()
if respuesta_usuario_ver_mas == 's':
    try:
        cantidad_adicional_a_mostrar = int(input('¿Cuántos más desea ver? Ingrese un número: ').strip())
        if cantidad_adicional_a_mostrar > 0:
            print(datos_ordenados_por_poder_total[['Nombre','Ataque','Defensa','Velocidad','PS','Poder Total']].head(10 + cantidad_adicional_a_mostrar).to_string(index=False))
        else:
            print('Número no válido, se mostrarán solo los 10 primeros.')
    except ValueError:
        print('Entrada no válida, se mostrarán solo los 10 primeros.')
