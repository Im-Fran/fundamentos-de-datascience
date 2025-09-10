from pathlib import Path
import seaborn as sns
from tareas.tarea_pokemon.a_cargar import datos

"""
4. Visualización de datos
-------------------------
- Haz un histograma de los valores de ataque.
- Realiza un gráfico de dispersión entre ataque y velocidad.
- Haz un boxplot de los PS por tipo principal (Tipo 1).
- Grafica la distribución de la defensa usando un diagrama de violín.

Las figuras se guardan en tareas/tarea_pokemon/figuras
"""

directorio_de_figuras = Path(__file__).parent / 'figuras'
directorio_de_figuras.mkdir(exist_ok=True)

# Histograma de ataque
grafico_histograma_ataque = sns.histplot(datos['Ataque'])
grafico_histograma_ataque.figure.savefig(directorio_de_figuras / 'hist_ataque.png')
grafico_histograma_ataque.figure.clear()

# Dispersión ataque vs velocidad
grafico_dispersion_ataque_velocidad = sns.scatterplot(data=datos, x='Ataque', y='Velocidad')
grafico_dispersion_ataque_velocidad.figure.savefig(directorio_de_figuras / 'scatter_ataque_velocidad.png')
grafico_dispersion_ataque_velocidad.figure.clear()

# Boxplot PS por tipo principal
grafico_boxplot_ps_por_tipo = sns.boxplot(data=datos, x='Tipo 1', y='PS')
grafico_boxplot_ps_por_tipo.figure.savefig(directorio_de_figuras / 'box_ps_por_tipo.png')
grafico_boxplot_ps_por_tipo.figure.clear()

# Violín defensa (global)
grafico_violin_defensa_global = sns.violinplot(data=datos, y='Defensa')
grafico_violin_defensa_global.figure.savefig(directorio_de_figuras / 'violin_defensa_global.png')
grafico_violin_defensa_global.figure.clear()

# Violín defensa por tipo
grafico_violin_defensa_por_tipo = sns.violinplot(data=datos, x='Tipo 1', y='Defensa')
grafico_violin_defensa_por_tipo.figure.savefig(directorio_de_figuras / 'violin_defensa_por_tipo.png')
grafico_violin_defensa_por_tipo.figure.clear()

print('Figuras generadas en:', directorio_de_figuras)
from pathlib import Path
import seaborn as sns
from tareas.tarea_pokemon.a_cargar import datos

"""
4. Visualización de datos
-------------------------
- Haz un histograma de los valores de ataque.
- Realiza un gráfico de dispersión entre ataque y velocidad.
- Haz un boxplot de los PS por tipo principal (Tipo 1).
- Grafica la distribución de la defensa usando un diagrama de violín.

Las figuras se guardan en tareas/tarea_pokemon/figuras
"""

directorio_de_figuras = Path(__file__).parent / 'figuras'
directorio_de_figuras.mkdir(exist_ok=True)

# Histograma de ataque
grafico_histograma_ataque = sns.histplot(datos['Ataque'])
grafico_histograma_ataque.figure.savefig(directorio_de_figuras / 'hist_ataque.png')
grafico_histograma_ataque.figure.clear()

# Dispersión ataque vs velocidad
grafico_dispersion_ataque_velocidad = sns.scatterplot(data=datos, x='Ataque', y='Velocidad')
grafico_dispersion_ataque_velocidad.figure.savefig(directorio_de_figuras / 'scatter_ataque_velocidad.png')
grafico_dispersion_ataque_velocidad.figure.clear()

# Boxplot PS por tipo principal
grafico_boxplot_ps_por_tipo = sns.boxplot(data=datos, x='Tipo 1', y='PS')
grafico_boxplot_ps_por_tipo.figure.savefig(directorio_de_figuras / 'box_ps_por_tipo.png')
grafico_boxplot_ps_por_tipo.figure.clear()

# Violín defensa (global)
grafico_violin_defensa_global = sns.violinplot(data=datos, y='Defensa')
grafico_violin_defensa_global.figure.savefig(directorio_de_figuras / 'violin_defensa_global.png')
grafico_violin_defensa_global.figure.clear()

# Violín defensa por tipo
grafico_violin_defensa_por_tipo = sns.violinplot(data=datos, x='Tipo 1', y='Defensa')
grafico_violin_defensa_por_tipo.figure.savefig(directorio_de_figuras / 'violin_defensa_por_tipo.png')
grafico_violin_defensa_por_tipo.figure.clear()

print('Figuras generadas en:', directorio_de_figuras)
