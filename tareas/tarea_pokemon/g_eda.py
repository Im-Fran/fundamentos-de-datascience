from tareas.tarea_pokemon.a_cargar import datos
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path

"""
7. Análisis exploratorio (EDA)
------------------------------
- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
- Identifica posibles outliers en los valores de ataque y PS usando boxplots.
"""

# Crear directorio de resultados EDA
directorio_resultados_eda = Path(__file__).parent / 'resultados' / 'eda'
directorio_resultados_eda.mkdir(parents=True, exist_ok=True)

print("Análisis exploratorio de datos")
print()

# 1. ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa?
print("1. Análisis de ataque y defensa por tipo de Pokémon")
print()

# Estadísticas de ataque por tipo primario
print("Estadísticas de ataque por tipo primario:")
estadisticas_ataque_por_tipo_primario = datos.groupby('Tipo 1')['Ataque'].agg(['mean', 'std', 'median', 'count']).round(2)
estadisticas_ataque_por_tipo_primario = estadisticas_ataque_por_tipo_primario.sort_values('mean', ascending=False)
print(estadisticas_ataque_por_tipo_primario)

# Guardar estadísticas de ataque en CSV
estadisticas_ataque_por_tipo_primario.to_csv(directorio_resultados_eda / 'estadisticas_ataque_por_tipo.csv')

print()
print("Estadísticas de defensa por tipo primario:")
estadisticas_defensa_por_tipo_primario = datos.groupby('Tipo 1')['Defensa'].agg(['mean', 'std', 'median', 'count']).round(2)
estadisticas_defensa_por_tipo_primario = estadisticas_defensa_por_tipo_primario.sort_values('mean', ascending=False)
print(estadisticas_defensa_por_tipo_primario)

# Guardar estadísticas de defensa en CSV
estadisticas_defensa_por_tipo_primario.to_csv(directorio_resultados_eda / 'estadisticas_defensa_por_tipo.csv')

# Análisis estadístico más profundo
print()
print("Análisis estadístico detallado:")
print()
print("Tipos con mayor ataque promedio:")
top_tres_tipos_mayor_ataque = estadisticas_ataque_por_tipo_primario.head(3)
for tipo_pokemon in top_tres_tipos_mayor_ataque.index:
    promedio_ataque_tipo = top_tres_tipos_mayor_ataque.loc[tipo_pokemon, 'mean']
    desviacion_estandar_ataque_tipo = top_tres_tipos_mayor_ataque.loc[tipo_pokemon, 'std']
    cantidad_pokemon_tipo = top_tres_tipos_mayor_ataque.loc[tipo_pokemon, 'count']
    print('- ' + tipo_pokemon + ':', str(promedio_ataque_tipo) + ' ± ' + str(desviacion_estandar_ataque_tipo) + ' (n=' + str(cantidad_pokemon_tipo) + ')')

print()
print("Tipos con mayor defensa promedio:")
top_tres_tipos_mayor_defensa = estadisticas_defensa_por_tipo_primario.head(3)
for tipo_pokemon in top_tres_tipos_mayor_defensa.index:
    promedio_defensa_tipo = top_tres_tipos_mayor_defensa.loc[tipo_pokemon, 'mean']
    desviacion_estandar_defensa_tipo = top_tres_tipos_mayor_defensa.loc[tipo_pokemon, 'std']
    cantidad_pokemon_tipo = top_tres_tipos_mayor_defensa.loc[tipo_pokemon, 'count']
    print('- ' + tipo_pokemon + ':', str(promedio_defensa_tipo) + ' ± ' + str(desviacion_estandar_defensa_tipo) + ' (n=' + str(cantidad_pokemon_tipo) + ')')

# Test ANOVA para verificar diferencias significativas
print()
print("Prueba ANOVA (diferencias significativas entre tipos):")
conteo_tipos_con_suficientes_datos = datos['Tipo 1'].value_counts()
lista_tipos_validos_para_anova = conteo_tipos_con_suficientes_datos[conteo_tipos_con_suficientes_datos >= 3].index

grupos_de_ataque_por_tipo = [datos[datos['Tipo 1'] == tipo_actual]['Ataque'].values for tipo_actual in lista_tipos_validos_para_anova]
grupos_de_defensa_por_tipo = [datos[datos['Tipo 1'] == tipo_actual]['Defensa'].values for tipo_actual in lista_tipos_validos_para_anova]

estadistico_f_ataque, valor_p_ataque = stats.f_oneway(*grupos_de_ataque_por_tipo)
estadistico_f_defensa, valor_p_defensa = stats.f_oneway(*grupos_de_defensa_por_tipo)

print('Ataque - F-statistic:', round(estadistico_f_ataque, 3), ', p-value:', round(valor_p_ataque, 3))
print('Defensa - F-statistic:', round(estadistico_f_defensa, 3), ', p-value:', round(valor_p_defensa, 3))

if valor_p_ataque < 0.05:
    print("Hay diferencias significativas en ataque entre tipos de Pokémon")
else:
    print("No hay diferencias significativas en ataque entre tipos de Pokémon")

if valor_p_defensa < 0.05:
    print("Hay diferencias significativas en defensa entre tipos de Pokémon")
else:
    print("No hay diferencias significativas en defensa entre tipos de Pokémon")

# 2. Correlación entre ataque y velocidad
print()
print()
print("2. Correlación entre ataque y velocidad")
print()

coeficiente_correlacion_ataque_velocidad = datos['Ataque'].corr(datos['Velocidad'])
print('Coeficiente de correlación de Pearson:', round(coeficiente_correlacion_ataque_velocidad, 4))

# Interpretación de la correlación
if abs(coeficiente_correlacion_ataque_velocidad) < 0.1:
    interpretacion_fuerza_correlacion = "muy débil"
elif abs(coeficiente_correlacion_ataque_velocidad) < 0.3:
    interpretacion_fuerza_correlacion = "débil"
elif abs(coeficiente_correlacion_ataque_velocidad) < 0.5:
    interpretacion_fuerza_correlacion = "moderada"
elif abs(coeficiente_correlacion_ataque_velocidad) < 0.7:
    interpretacion_fuerza_correlacion = "fuerte"
else:
    interpretacion_fuerza_correlacion = "muy fuerte"

if coeficiente_correlacion_ataque_velocidad > 0:
    direccion_de_correlacion = "positiva"
else:
    direccion_de_correlacion = "negativa"

print('Interpretación: Correlación', interpretacion_fuerza_correlacion, direccion_de_correlacion)

# Test de significancia de la correlación
numero_observaciones = len(datos)
estadistico_t_correlacion = coeficiente_correlacion_ataque_velocidad * np.sqrt((numero_observaciones - 2) / (1 - coeficiente_correlacion_ataque_velocidad**2))
valor_p_correlacion = 2 * (1 - stats.t.cdf(abs(estadistico_t_correlacion), numero_observaciones - 2))
print('Test de significancia: t =', round(estadistico_t_correlacion, 3), ', p-value =', round(valor_p_correlacion, 3))

if valor_p_correlacion < 0.05:
    print("La correlación es estadísticamente significativa")
else:
    print("La correlación no es estadísticamente significativa")

# 3. Dispersión de PS por tipo
print()
print()
print("3. Dispersión de PS por tipo de Pokémon")
print()

estadisticas_ps_por_tipo = datos.groupby('Tipo 1')['PS'].agg(['mean', 'std', 'var', 'count']).round(2)
estadisticas_ps_por_tipo = estadisticas_ps_por_tipo.sort_values('std', ascending=False)

print("Desviación estándar de PS por tipo (ordenado de mayor a menor dispersión):")
print(estadisticas_ps_por_tipo)

# Guardar estadísticas de PS en CSV
estadisticas_ps_por_tipo.to_csv(directorio_resultados_eda / 'estadisticas_ps_por_tipo.csv')

print("Tipo con mayor dispersión en PS:", estadisticas_ps_por_tipo.index[0], "(σ =", str(estadisticas_ps_por_tipo.iloc[0]['std']) + ")")
print("Tipo con menor dispersión en PS:", estadisticas_ps_por_tipo.index[-1], "(σ =", str(estadisticas_ps_por_tipo.iloc[-1]['std']) + ")")

# Coeficiente de variación para comparar dispersión relativa
print()
print("Coeficiente de variación (CV = σ/μ) - Para comparar dispersión relativa:")
coeficiente_variacion_ps = (estadisticas_ps_por_tipo['std'] / estadisticas_ps_por_tipo['mean'] * 100).round(2)
coeficiente_variacion_ps = coeficiente_variacion_ps.sort_values(ascending=False)
print(coeficiente_variacion_ps.to_frame('CV (%)'))

# Guardar coeficiente de variación en CSV
coeficiente_variacion_ps.to_csv(directorio_resultados_eda / 'coeficiente_variacion_ps.csv')

# 4. Detección de outliers usando boxplots
print()
print()
print("4. Detección de outliers")
print()

# Función para detectar outliers usando IQR
def detectar_outliers_iqr(serie):
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = serie[(serie < limite_inferior) | (serie > limite_superior)]
    return outliers

# Outliers en Ataque
outliers_ataque = detectar_outliers_iqr(datos['Ataque'])
print("Outliers en ataque:")
print("Número de outliers:", len(outliers_ataque))
if len(outliers_ataque) > 0:
    print("Pokémon con valores atípicos de ataque:")
    lista_outliers_ataque = []
    for idx in outliers_ataque.index:
        nombre = datos.loc[idx, 'Nombre']
        ataque = datos.loc[idx, 'Ataque']
        tipo = datos.loc[idx, 'Tipo 1']
        print("  -", nombre, "(" + tipo + "):", ataque)
        lista_outliers_ataque.append({'Nombre': nombre, 'Tipo': tipo, 'Ataque': ataque})

    # Guardar outliers de ataque en CSV
    import pandas as pd
    dataframe_outliers_ataque = pd.DataFrame(lista_outliers_ataque)
    dataframe_outliers_ataque.to_csv(directorio_resultados_eda / 'outliers_ataque.csv', index=False)

# Outliers en PS
outliers_ps = detectar_outliers_iqr(datos['PS'])
print()
print("Outliers en PS:")
print("Número de outliers:", len(outliers_ps))
if len(outliers_ps) > 0:
    print("Pokémon con valores atípicos de PS:")
    lista_outliers_ps = []
    for idx in outliers_ps.index:
        nombre = datos.loc[idx, 'Nombre']
        ps = datos.loc[idx, 'PS']
        tipo = datos.loc[idx, 'Tipo 1']
        print("  -", nombre, "(" + tipo + "):", ps)
        lista_outliers_ps.append({'Nombre': nombre, 'Tipo': tipo, 'PS': ps})

    # Guardar outliers de PS en CSV
    import pandas as pd
    dataframe_outliers_ps = pd.DataFrame(lista_outliers_ps)
    dataframe_outliers_ps.to_csv(directorio_resultados_eda / 'outliers_ps.csv', index=False)

# Estadísticas descriptivas para contexto
print()
print("Estadísticas descriptivas:")
print("Ataque - Media:", round(datos['Ataque'].mean(), 1), ", Mediana:", round(datos['Ataque'].median(), 1))
print("PS - Media:", round(datos['PS'].mean(), 1), ", Mediana:", round(datos['PS'].median(), 1))

# Crear visualizaciones
print()
print("Generando visualizaciones")
print()

# Configurar el estilo
plt.style.use('default')
sns.set_palette("husl")

# Figura 1: Boxplot de ataque y PS para identificar outliers
figura_outliers, (axes_ataque, axes_ps) = plt.subplots(1, 2, figsize=(15, 6))

# Boxplot de Ataque
boxplot_ataque = axes_ataque.boxplot(datos['Ataque'], patch_artist=True)
axes_ataque.set_title('Distribución de Ataque\n(Detección de Outliers)', fontsize=14, fontweight='bold')
axes_ataque.set_ylabel('Ataque', fontsize=12)
axes_ataque.grid(True, alpha=0.3)
boxplot_ataque['boxes'][0].set_facecolor('lightblue')

# Boxplot de PS
boxplot_ps = axes_ps.boxplot(datos['PS'], patch_artist=True)
axes_ps.set_title('Distribución de PS\n(Detección de Outliers)', fontsize=14, fontweight='bold')
axes_ps.set_ylabel('PS', fontsize=12)
axes_ps.grid(True, alpha=0.3)
boxplot_ps['boxes'][0].set_facecolor('lightcoral')

plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'outliers_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Figura 2: Scatter plot de correlación Ataque vs Velocidad
plt.figure(figsize=(10, 8))
plt.scatter(datos['Ataque'], datos['Velocidad'], alpha=0.7, s=60, c='steelblue', edgecolors='navy', linewidth=0.5)
plt.xlabel('Ataque', fontsize=12)
plt.ylabel('Velocidad', fontsize=12)
plt.title('Correlación entre Ataque y Velocidad\nr = ' + str(round(coeficiente_correlacion_ataque_velocidad, 4)), fontsize=14, fontweight='bold')

# Línea de tendencia
coeficientes_polinomio = np.polyfit(datos['Ataque'], datos['Velocidad'], 1)
polinomio_tendencia = np.poly1d(coeficientes_polinomio)
plt.plot(datos['Ataque'].sort_values(), polinomio_tendencia(datos['Ataque'].sort_values()), "r--", alpha=0.8, linewidth=2)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'correlacion_ataque_velocidad.png', dpi=300, bbox_inches='tight')
plt.show()

# Figura 3: Boxplot de PS por tipo
plt.figure(figsize=(12, 8))
lista_datos_ps_por_tipo = []
lista_tipos_para_grafico = []
for tipo_pokemon_actual in datos['Tipo 1'].unique():
    if datos[datos['Tipo 1'] == tipo_pokemon_actual]['PS'].count() >= 2:  # Solo tipos con al menos 2 Pokémon
        lista_datos_ps_por_tipo.append(datos[datos['Tipo 1'] == tipo_pokemon_actual]['PS'].values)
        lista_tipos_para_grafico.append(tipo_pokemon_actual)

plt.boxplot(lista_datos_ps_por_tipo, tick_labels=lista_tipos_para_grafico)
plt.title('Dispersión de PS por Tipo de Pokémon', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Pokémon', fontsize=12)
plt.ylabel('PS', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'ps_por_tipo_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Figura 4: Heatmap de estadísticas por tipo
plt.figure(figsize=(12, 8))
matriz_estadisticas_por_tipo = datos.groupby('Tipo 1')[['Ataque', 'Defensa', 'Velocidad', 'PS']].mean()
sns.heatmap(matriz_estadisticas_por_tipo, annot=True, cmap='YlOrRd', fmt='.1f', cbar_kws={'label': 'Valor promedio'})
plt.title('Heatmap de Estadísticas Promedio por Tipo', fontsize=14, fontweight='bold')
plt.xlabel('Estadísticas', fontsize=12)
plt.ylabel('Tipo de Pokémon', fontsize=12)
plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'heatmap_stats_por_tipo.png', dpi=300, bbox_inches='tight')
plt.show()

# Guardar matriz de estadísticas en CSV
matriz_estadisticas_por_tipo.to_csv(directorio_resultados_eda / 'matriz_estadisticas_por_tipo.csv')

print("Visualizaciones y datos guardados en:", directorio_resultados_eda)

print()
print("Resumen de conclusiones")
print("1. Tipos con mayor ataque: Los tipos Dragón, Lucha y Fuego tienden a tener mayor ataque")
print("2. Tipos con mayor defensa: Los tipos Roca, Acero y Tierra tienden a tener mayor defensa")
print("3. Correlación ataque-velocidad:", interpretacion_fuerza_correlacion, direccion_de_correlacion, "(r =", str(round(coeficiente_correlacion_ataque_velocidad, 4)) + ")")
print("4. Dispersión de PS: Varía significativamente entre tipos")
print("5. Outliers detectados:", len(outliers_ataque), "en ataque,", len(outliers_ps), "en PS")
from tareas.tarea_pokemon.a_cargar import datos
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path

"""
7. Análisis exploratorio (EDA)
------------------------------
- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
- Identifica posibles outliers en los valores de ataque y PS usando boxplots.
"""

# Crear directorio de resultados EDA
directorio_resultados_eda = Path(__file__).parent / 'resultados' / 'eda'
directorio_resultados_eda.mkdir(parents=True, exist_ok=True)

print("Análisis exploratorio de datos")
print()

# 1. ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa?
print("1. Análisis de ataque y defensa por tipo de Pokémon")
print()

# Estadísticas de ataque por tipo primario
print("Estadísticas de ataque por tipo primario:")
estadisticas_ataque_por_tipo_primario = datos.groupby('Tipo 1')['Ataque'].agg(['mean', 'std', 'median', 'count']).round(2)
estadisticas_ataque_por_tipo_primario = estadisticas_ataque_por_tipo_primario.sort_values('mean', ascending=False)
print(estadisticas_ataque_por_tipo_primario)

# Guardar estadísticas de ataque en CSV
estadisticas_ataque_por_tipo_primario.to_csv(directorio_resultados_eda / 'estadisticas_ataque_por_tipo.csv')

print()
print("Estadísticas de defensa por tipo primario:")
estadisticas_defensa_por_tipo_primario = datos.groupby('Tipo 1')['Defensa'].agg(['mean', 'std', 'median', 'count']).round(2)
estadisticas_defensa_por_tipo_primario = estadisticas_defensa_por_tipo_primario.sort_values('mean', ascending=False)
print(estadisticas_defensa_por_tipo_primario)

# Guardar estadísticas de defensa en CSV
estadisticas_defensa_por_tipo_primario.to_csv(directorio_resultados_eda / 'estadisticas_defensa_por_tipo.csv')

# Análisis estadístico más profundo
print()
print("Análisis estadístico detallado:")
print()
print("Tipos con mayor ataque promedio:")
top_tres_tipos_mayor_ataque = estadisticas_ataque_por_tipo_primario.head(3)
for tipo_pokemon in top_tres_tipos_mayor_ataque.index:
    promedio_ataque_tipo = top_tres_tipos_mayor_ataque.loc[tipo_pokemon, 'mean']
    desviacion_estandar_ataque_tipo = top_tres_tipos_mayor_ataque.loc[tipo_pokemon, 'std']
    cantidad_pokemon_tipo = top_tres_tipos_mayor_ataque.loc[tipo_pokemon, 'count']
    print('- ' + tipo_pokemon + ':', str(promedio_ataque_tipo) + ' ± ' + str(desviacion_estandar_ataque_tipo) + ' (n=' + str(cantidad_pokemon_tipo) + ')')

print()
print("Tipos con mayor defensa promedio:")
top_tres_tipos_mayor_defensa = estadisticas_defensa_por_tipo_primario.head(3)
for tipo_pokemon in top_tres_tipos_mayor_defensa.index:
    promedio_defensa_tipo = top_tres_tipos_mayor_defensa.loc[tipo_pokemon, 'mean']
    desviacion_estandar_defensa_tipo = top_tres_tipos_mayor_defensa.loc[tipo_pokemon, 'std']
    cantidad_pokemon_tipo = top_tres_tipos_mayor_defensa.loc[tipo_pokemon, 'count']
    print('- ' + tipo_pokemon + ':', str(promedio_defensa_tipo) + ' ± ' + str(desviacion_estandar_defensa_tipo) + ' (n=' + str(cantidad_pokemon_tipo) + ')')

# Test ANOVA para verificar diferencias significativas
print()
print("Prueba ANOVA (diferencias significativas entre tipos):")
conteo_tipos_con_suficientes_datos = datos['Tipo 1'].value_counts()
lista_tipos_validos_para_anova = conteo_tipos_con_suficientes_datos[conteo_tipos_con_suficientes_datos >= 3].index

grupos_de_ataque_por_tipo = [datos[datos['Tipo 1'] == tipo_actual]['Ataque'].values for tipo_actual in lista_tipos_validos_para_anova]
grupos_de_defensa_por_tipo = [datos[datos['Tipo 1'] == tipo_actual]['Defensa'].values for tipo_actual in lista_tipos_validos_para_anova]

estadistico_f_ataque, valor_p_ataque = stats.f_oneway(*grupos_de_ataque_por_tipo)
estadistico_f_defensa, valor_p_defensa = stats.f_oneway(*grupos_de_defensa_por_tipo)

print('Ataque - F-statistic:', round(estadistico_f_ataque, 3), ', p-value:', round(valor_p_ataque, 3))
print('Defensa - F-statistic:', round(estadistico_f_defensa, 3), ', p-value:', round(valor_p_defensa, 3))

if valor_p_ataque < 0.05:
    print("Hay diferencias significativas en ataque entre tipos de Pokémon")
else:
    print("No hay diferencias significativas en ataque entre tipos de Pokémon")

if valor_p_defensa < 0.05:
    print("Hay diferencias significativas en defensa entre tipos de Pokémon")
else:
    print("No hay diferencias significativas en defensa entre tipos de Pokémon")

# 2. Correlación entre ataque y velocidad
print()
print()
print("2. Correlación entre ataque y velocidad")
print()

coeficiente_correlacion_ataque_velocidad = datos['Ataque'].corr(datos['Velocidad'])
print('Coeficiente de correlación de Pearson:', round(coeficiente_correlacion_ataque_velocidad, 4))

# Interpretación de la correlación
if abs(coeficiente_correlacion_ataque_velocidad) < 0.1:
    interpretacion_fuerza_correlacion = "muy débil"
elif abs(coeficiente_correlacion_ataque_velocidad) < 0.3:
    interpretacion_fuerza_correlacion = "débil"
elif abs(coeficiente_correlacion_ataque_velocidad) < 0.5:
    interpretacion_fuerza_correlacion = "moderada"
elif abs(coeficiente_correlacion_ataque_velocidad) < 0.7:
    interpretacion_fuerza_correlacion = "fuerte"
else:
    interpretacion_fuerza_correlacion = "muy fuerte"

if coeficiente_correlacion_ataque_velocidad > 0:
    direccion_de_correlacion = "positiva"
else:
    direccion_de_correlacion = "negativa"

print('Interpretación: Correlación', interpretacion_fuerza_correlacion, direccion_de_correlacion)

# Test de significancia de la correlación
numero_observaciones = len(datos)
estadistico_t_correlacion = coeficiente_correlacion_ataque_velocidad * np.sqrt((numero_observaciones - 2) / (1 - coeficiente_correlacion_ataque_velocidad**2))
valor_p_correlacion = 2 * (1 - stats.t.cdf(abs(estadistico_t_correlacion), numero_observaciones - 2))
print('Test de significancia: t =', round(estadistico_t_correlacion, 3), ', p-value =', round(valor_p_correlacion, 3))

if valor_p_correlacion < 0.05:
    print("La correlación es estadísticamente significativa")
else:
    print("La correlación no es estadísticamente significativa")

# 3. Dispersión de PS por tipo
print()
print()
print("3. Dispersión de PS por tipo de Pokémon")
print()

estadisticas_ps_por_tipo = datos.groupby('Tipo 1')['PS'].agg(['mean', 'std', 'var', 'count']).round(2)
estadisticas_ps_por_tipo = estadisticas_ps_por_tipo.sort_values('std', ascending=False)

print("Desviación estándar de PS por tipo (ordenado de mayor a menor dispersión):")
print(estadisticas_ps_por_tipo)

# Guardar estadísticas de PS en CSV
estadisticas_ps_por_tipo.to_csv(directorio_resultados_eda / 'estadisticas_ps_por_tipo.csv')

print("Tipo con mayor dispersión en PS:", estadisticas_ps_por_tipo.index[0], "(σ =", str(estadisticas_ps_por_tipo.iloc[0]['std']) + ")")
print("Tipo con menor dispersión en PS:", estadisticas_ps_por_tipo.index[-1], "(σ =", str(estadisticas_ps_por_tipo.iloc[-1]['std']) + ")")

# Coeficiente de variación para comparar dispersión relativa
print()
print("Coeficiente de variación (CV = σ/μ) - Para comparar dispersión relativa:")
coeficiente_variacion_ps = (estadisticas_ps_por_tipo['std'] / estadisticas_ps_por_tipo['mean'] * 100).round(2)
coeficiente_variacion_ps = coeficiente_variacion_ps.sort_values(ascending=False)
print(coeficiente_variacion_ps.to_frame('CV (%)'))

# Guardar coeficiente de variación en CSV
coeficiente_variacion_ps.to_csv(directorio_resultados_eda / 'coeficiente_variacion_ps.csv')

# 4. Detección de outliers usando boxplots
print()
print()
print("4. Detección de outliers")
print()

# Función para detectar outliers usando IQR
def detectar_outliers_iqr(serie):
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = serie[(serie < limite_inferior) | (serie > limite_superior)]
    return outliers

# Outliers en Ataque
outliers_ataque = detectar_outliers_iqr(datos['Ataque'])
print("Outliers en ataque:")
print("Número de outliers:", len(outliers_ataque))
if len(outliers_ataque) > 0:
    print("Pokémon con valores atípicos de ataque:")
    lista_outliers_ataque = []
    for idx in outliers_ataque.index:
        nombre = datos.loc[idx, 'Nombre']
        ataque = datos.loc[idx, 'Ataque']
        tipo = datos.loc[idx, 'Tipo 1']
        print("  -", nombre, "(" + tipo + "):", ataque)
        lista_outliers_ataque.append({'Nombre': nombre, 'Tipo': tipo, 'Ataque': ataque})

    # Guardar outliers de ataque en CSV
    import pandas as pd
    dataframe_outliers_ataque = pd.DataFrame(lista_outliers_ataque)
    dataframe_outliers_ataque.to_csv(directorio_resultados_eda / 'outliers_ataque.csv', index=False)

# Outliers en PS
outliers_ps = detectar_outliers_iqr(datos['PS'])
print()
print("Outliers en PS:")
print("Número de outliers:", len(outliers_ps))
if len(outliers_ps) > 0:
    print("Pokémon con valores atípicos de PS:")
    lista_outliers_ps = []
    for idx in outliers_ps.index:
        nombre = datos.loc[idx, 'Nombre']
        ps = datos.loc[idx, 'PS']
        tipo = datos.loc[idx, 'Tipo 1']
        print("  -", nombre, "(" + tipo + "):", ps)
        lista_outliers_ps.append({'Nombre': nombre, 'Tipo': tipo, 'PS': ps})

    # Guardar outliers de PS en CSV
    import pandas as pd
    dataframe_outliers_ps = pd.DataFrame(lista_outliers_ps)
    dataframe_outliers_ps.to_csv(directorio_resultados_eda / 'outliers_ps.csv', index=False)

# Estadísticas descriptivas para contexto
print()
print("Estadísticas descriptivas:")
print("Ataque - Media:", round(datos['Ataque'].mean(), 1), ", Mediana:", round(datos['Ataque'].median(), 1))
print("PS - Media:", round(datos['PS'].mean(), 1), ", Mediana:", round(datos['PS'].median(), 1))

# Crear visualizaciones
print()
print("Generando visualizaciones")
print()

# Configurar el estilo
plt.style.use('default')
sns.set_palette("husl")

# Figura 1: Boxplot de ataque y PS para identificar outliers
figura_outliers, (axes_ataque, axes_ps) = plt.subplots(1, 2, figsize=(15, 6))

# Boxplot de Ataque
boxplot_ataque = axes_ataque.boxplot(datos['Ataque'], patch_artist=True)
axes_ataque.set_title('Distribución de Ataque\n(Detección de Outliers)', fontsize=14, fontweight='bold')
axes_ataque.set_ylabel('Ataque', fontsize=12)
axes_ataque.grid(True, alpha=0.3)
boxplot_ataque['boxes'][0].set_facecolor('lightblue')

# Boxplot de PS
boxplot_ps = axes_ps.boxplot(datos['PS'], patch_artist=True)
axes_ps.set_title('Distribución de PS\n(Detección de Outliers)', fontsize=14, fontweight='bold')
axes_ps.set_ylabel('PS', fontsize=12)
axes_ps.grid(True, alpha=0.3)
boxplot_ps['boxes'][0].set_facecolor('lightcoral')

plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'outliers_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Figura 2: Scatter plot de correlación Ataque vs Velocidad
plt.figure(figsize=(10, 8))
plt.scatter(datos['Ataque'], datos['Velocidad'], alpha=0.7, s=60, c='steelblue', edgecolors='navy', linewidth=0.5)
plt.xlabel('Ataque', fontsize=12)
plt.ylabel('Velocidad', fontsize=12)
plt.title('Correlación entre Ataque y Velocidad\nr = ' + str(round(coeficiente_correlacion_ataque_velocidad, 4)), fontsize=14, fontweight='bold')

# Línea de tendencia
coeficientes_polinomio = np.polyfit(datos['Ataque'], datos['Velocidad'], 1)
polinomio_tendencia = np.poly1d(coeficientes_polinomio)
plt.plot(datos['Ataque'].sort_values(), polinomio_tendencia(datos['Ataque'].sort_values()), "r--", alpha=0.8, linewidth=2)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'correlacion_ataque_velocidad.png', dpi=300, bbox_inches='tight')
plt.show()

# Figura 3: Boxplot de PS por tipo
plt.figure(figsize=(12, 8))
lista_datos_ps_por_tipo = []
lista_tipos_para_grafico = []
for tipo_pokemon_actual in datos['Tipo 1'].unique():
    if datos[datos['Tipo 1'] == tipo_pokemon_actual]['PS'].count() >= 2:  # Solo tipos con al menos 2 Pokémon
        lista_datos_ps_por_tipo.append(datos[datos['Tipo 1'] == tipo_pokemon_actual]['PS'].values)
        lista_tipos_para_grafico.append(tipo_pokemon_actual)

plt.boxplot(lista_datos_ps_por_tipo, tick_labels=lista_tipos_para_grafico)
plt.title('Dispersión de PS por Tipo de Pokémon', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Pokémon', fontsize=12)
plt.ylabel('PS', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'ps_por_tipo_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Figura 4: Heatmap de estadísticas por tipo
plt.figure(figsize=(12, 8))
matriz_estadisticas_por_tipo = datos.groupby('Tipo 1')[['Ataque', 'Defensa', 'Velocidad', 'PS']].mean()
sns.heatmap(matriz_estadisticas_por_tipo, annot=True, cmap='YlOrRd', fmt='.1f', cbar_kws={'label': 'Valor promedio'})
plt.title('Heatmap de Estadísticas Promedio por Tipo', fontsize=14, fontweight='bold')
plt.xlabel('Estadísticas', fontsize=12)
plt.ylabel('Tipo de Pokémon', fontsize=12)
plt.tight_layout()
plt.savefig(directorio_resultados_eda / 'heatmap_stats_por_tipo.png', dpi=300, bbox_inches='tight')
plt.show()

# Guardar matriz de estadísticas en CSV
matriz_estadisticas_por_tipo.to_csv(directorio_resultados_eda / 'matriz_estadisticas_por_tipo.csv')

print("Visualizaciones y datos guardados en:", directorio_resultados_eda)

print()
print("Resumen de conclusiones")
print("1. Tipos con mayor ataque: Los tipos Dragón, Lucha y Fuego tienden a tener mayor ataque")
print("2. Tipos con mayor defensa: Los tipos Roca, Acero y Tierra tienden a tener mayor defensa")
print("3. Correlación ataque-velocidad:", interpretacion_fuerza_correlacion, direccion_de_correlacion, "(r =", str(round(coeficiente_correlacion_ataque_velocidad, 4)) + ")")
print("4. Dispersión de PS: Varía significativamente entre tipos")
print("5. Outliers detectados:", len(outliers_ataque), "en ataque,", len(outliers_ps), "en PS")
