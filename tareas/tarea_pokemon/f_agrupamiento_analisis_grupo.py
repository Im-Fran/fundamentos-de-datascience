"""
6. Agrupamiento y análisis por grupo
-------------------------------------
- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
- ¿Qué tipo tiene el mayor promedio de velocidad?
- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
"""
import pandas as pd
from tareas.tarea_pokemon.a_cargar import datos

print('Análisis por grupo (Tipo 1)')
print()

estadisticas_ataque_por_tipo = datos.groupby('Tipo 1')['Ataque'].agg(['mean','median','std']).round(2).rename(columns={'mean':'Promedio','median':'Mediana','std':'Desv.Std'})
print('Ataque por tipo (promedio, mediana, desviación estándar):')
print(estadisticas_ataque_por_tipo.sort_values('Promedio', ascending=False).to_string())
print()

promedio_velocidad_por_tipo = datos.groupby('Tipo 1')['Velocidad'].mean().round(2)
tipo_con_mayor_promedio_velocidad = promedio_velocidad_por_tipo.idxmax()
valor_mayor_promedio_velocidad = promedio_velocidad_por_tipo.max()
print('Tipo con mayor promedio de velocidad:', tipo_con_mayor_promedio_velocidad, f'({valor_mayor_promedio_velocidad})')
print()

# Pokémon con mayor y menor PS por tipo
lista_pokemon_extremos_ps = []
for tipo_actual, dataframe_del_tipo in datos.groupby('Tipo 1'):
    fila_pokemon_mayor_ps = dataframe_del_tipo.loc[dataframe_del_tipo['PS'].idxmax()]
    fila_pokemon_menor_ps = dataframe_del_tipo.loc[dataframe_del_tipo['PS'].idxmin()]
    lista_pokemon_extremos_ps.append({
        'Tipo 1': tipo_actual,
        'Max PS Nombre': fila_pokemon_mayor_ps['Nombre'],
        'Max PS': int(fila_pokemon_mayor_ps['PS']),
        'Min PS Nombre': fila_pokemon_menor_ps['Nombre'],
        'Min PS': int(fila_pokemon_menor_ps['PS'])
    })

dataframe_pokemon_extremos_ps = pd.DataFrame(lista_pokemon_extremos_ps).sort_values('Tipo 1')
print('Pokémon con mayor y menor PS por tipo:')
print(dataframe_pokemon_extremos_ps.to_string(index=False))
"""
6. Agrupamiento y análisis por grupo
-------------------------------------
- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
- ¿Qué tipo tiene el mayor promedio de velocidad?
- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
"""
import pandas as pd
from tareas.tarea_pokemon.a_cargar import datos

print('Análisis por grupo (Tipo 1)')
print()

estadisticas_ataque_por_tipo = datos.groupby('Tipo 1')['Ataque'].agg(['mean','median','std']).round(2).rename(columns={'mean':'Promedio','median':'Mediana','std':'Desv.Std'})
print('Ataque por tipo (promedio, mediana, desviación estándar):')
print(estadisticas_ataque_por_tipo.sort_values('Promedio', ascending=False).to_string())
print()

promedio_velocidad_por_tipo = datos.groupby('Tipo 1')['Velocidad'].mean().round(2)
tipo_con_mayor_promedio_velocidad = promedio_velocidad_por_tipo.idxmax()
valor_mayor_promedio_velocidad = promedio_velocidad_por_tipo.max()
print('Tipo con mayor promedio de velocidad:', tipo_con_mayor_promedio_velocidad, f'({valor_mayor_promedio_velocidad})')
print()

# Pokémon con mayor y menor PS por tipo
lista_pokemon_extremos_ps = []
for tipo_actual, dataframe_del_tipo in datos.groupby('Tipo 1'):
    fila_pokemon_mayor_ps = dataframe_del_tipo.loc[dataframe_del_tipo['PS'].idxmax()]
    fila_pokemon_menor_ps = dataframe_del_tipo.loc[dataframe_del_tipo['PS'].idxmin()]
    lista_pokemon_extremos_ps.append({
        'Tipo 1': tipo_actual,
        'Max PS Nombre': fila_pokemon_mayor_ps['Nombre'],
        'Max PS': int(fila_pokemon_mayor_ps['PS']),
        'Min PS Nombre': fila_pokemon_menor_ps['Nombre'],
        'Min PS': int(fila_pokemon_menor_ps['PS'])
    })

dataframe_pokemon_extremos_ps = pd.DataFrame(lista_pokemon_extremos_ps).sort_values('Tipo 1')
print('Pokémon con mayor y menor PS por tipo:')
print(dataframe_pokemon_extremos_ps.to_string(index=False))
