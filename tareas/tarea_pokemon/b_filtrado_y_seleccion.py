from tareas.tarea_pokemon.a_cargar import datos

"""
2. Filtrado y selección
-----------------------
- Filtra todos los Pokémon de tipo "Fuego".
- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
"""
pokemon_tipo_fuego = datos[datos['Tipo 1'] == 'Fuego'] # Filtra los Pokémon de tipo "Fuego"
columnas_seleccionadas_pokemon_fuego = pokemon_tipo_fuego[['Nombre', 'Tipo 1', 'Ataque', 'Velocidad']] # Selecciona las columnas Nombre, Tipo 1, Ataque y Velocidad

print('Pokémon de tipo fuego:')
print()
print(columnas_seleccionadas_pokemon_fuego.to_string(index=False))
