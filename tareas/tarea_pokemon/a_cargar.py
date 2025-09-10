import pandas as pd

"""
1. Lectura de datos
-------------------
- Carga el archivo csv en un DataFrame de Pandas.
"""
# datos = pd.read_csv('data/pokemon_primera_gen.csv') # Este es el archivo antiguo con posibles errores
datos = pd.read_csv('data/pokemon_revisado.csv') # Este es el archivo

""" Debajo se muestra el código que se ejecutó por primera vez para validat y reparar los datos entregados."""
"""
1.1 Validación de datos
---------------------
- Filtra los datos de pokemon_primera_gen y los verifica con el archivo 'control.csv'.

Fuente del archivo 'pokemon_gen_1_to_8.csv': https://github.com/shahinrostami/pokemon_dataset/blob/master/pokemon_gen_1_to_8.csv
"""
# control = pd.read_csv('./pokemon_gen_1_to_8.csv') # Lee el archivo CSV y lo almacena en la variable control
# nombres_pokemon_generacion_1 = set(control[control['generation'] == 1]['name'])
# pokemon = datos[datos['Nombre'].isin(nombres_pokemon_generacion_1)]


""" 
1.2 Reparación de datos
---------------------
- Repara inconsistencias en los tipos de pokémon
- Obtiene el tipo de pokémon desde el D.F. de control (usando el nombre del pokémon como llave)
- Reemplaza 'Tipo 1' y 'Tipo 2' con el contenido de type_1 y type_2 del D.F. de control
"""
# pokemon = pokemon.drop(columns=['Tipo 1', 'Tipo 2']) # Elimina las columnas 'Tipo 1' y 'Tipo 2' del DataFrame pokemon
# pokemon = pokemon.merge(control[['name', 'type_1', 'type_2']], left_on='Nombre', right_on='name', how='left') # Realiza un merge entre los DataFrames pokemon y control
# pokemon = pokemon.drop(columns=['name']) # Elimina la columna 'name' del DataFrame pokemon
# pokemon = pokemon.rename(columns={'type_1': 'Tipo 1', 'type_2': 'Tipo 2'}) # Renombra las columnas 'type_1' y 'type_2' a 'Tipo 1' y 'Tipo 2'
# pokemon = pokemon[['Nombre', 'Tipo 1', 'Tipo 2', 'Ataque', 'Defensa', 'Velocidad', 'PS']] # Reordena las columnas del DataFrame pokemon
# pokemon.to_csv('data/pokemon_revisado.csv', index=False) # Guarda el DataFrame pokemon en un archivo CSV