# 8. Interpretación y Conclusiones

Este documento resume hallazgos clave de los análisis (estadística básica, agrupamientos, visualizaciones y EDA) sobre los Pokémon de la primera generación.

## 1. Tendencias de Ataque y Defensa
Los promedios por tipo muestran que algunos tipos sobresalen ofensivamente mientras otros son más balanceados defensivamente. (Ver `resultados/eda/estadisticas_ataque_por_tipo.csv` y `resultados/eda/estadisticas_defensa_por_tipo.csv`).
- Tipos con ataque más alto: suelen incluir combinaciones con Lucha, Fuego o Tierra (dependiendo de los registros presentes). 
- Tipos con defensa más alta: tienden a incluir variantes como Roca/Acero en datasets más amplios; en esta muestra parcial destacan aquellos con mayor mediana de Defensa (consultar archivos generados).

Conclusión: Hay especialización parcial: no todos los tipos que atacan fuerte son igual de rápidos ni resistentes.

## 2. Correlación Ataque vs Velocidad
La correlación Pearson calculada en `g_eda.py` es moderada-baja (ver consola y `resultados/eda/correlacion_ataque_velocidad.png`), indicando que un mayor ataque no garantiza mayor velocidad. Se justifica analizar cada tipo por separado si se buscara construir equipos balanceados.

## 3. Dispersión de PS
La desviación estándar de PS por tipo (archivo `resultados/eda/estadisticas_ps_por_tipo.csv`) evidencia que algunos tipos son más homogéneos (baja dispersión) mientras otros mezclan tanques y frágiles. Tipos con alta dispersión permiten roles variados dentro del mismo arquetipo. El coeficiente de variación se encuentra en `resultados/eda/coeficiente_variacion_ps.csv`.

## 4. Outliers
Se identificaron outliers usando IQR en Ataque y PS (`resultados/eda/outliers_ps.csv`). Estos valores extremos pueden distorsionar promedios; al diseñar estrategias conviene revisar si representan evoluciones avanzadas o excepciones. Las visualizaciones se encuentran en `resultados/eda/outliers_boxplot.png`.

## 5. Balance vs Especialización
- Más balanceados: tipos cuyos promedios de Ataque, Defensa, Velocidad y PS están cercanos a la mediana global del dataset y además con baja desviación. (Puede aproximarse consultando `resultados/eda/matriz_estadisticas_por_tipo.csv` con desviaciones estándar.)
- Más especializados: aquellos con un atributo claramente superior (p.ej. muy alto Ataque o Velocidad) y otros por debajo del promedio.

## 6. Visualizaciones Clave
- Histograma de Ataque: distribución relativamente sesgada hacia valores medios, con cola en superiores (`figuras/hist_ataque.png`).
- Scatter Ataque vs Velocidad: nube dispersa sin patrón lineal fuerte (`resultados/eda/correlacion_ataque_velocidad.png`).
- Boxplot PS por tipo: permite detectar qué tipos tienen mediana más alta y rango intercuartílico amplio (`resultados/eda/ps_por_tipo_boxplot.png`).
- Violines de Defensa: muestran forma de la distribución (multimodalidad potencial o concentración) (`figuras/violin_defensa_global.png` y `figuras/violin_defensa_por_tipo.png`).
- Heatmap de estadísticas: visualización completa de todas las estadísticas promedio por tipo (`resultados/eda/heatmap_stats_por_tipo.png`).

## 7. Recomendaciones Analíticas
1. Para equipos equilibrados: priorizar tipos con varianza moderada en PS y ataque medio (evita dependencia de un solo rol).
2. Para ofensiva rápida: seleccionar tipos con alta mediana de Velocidad aun sacrificando Defensa.
3. Outliers deben analizarse individualmente: pueden definir estrategia (sweeper, tanque) pero incrementan vulnerabilidad si caen.
4. Incluir mezcla de perfiles: uno con PS alto y defensa sólida, otro veloz con ataque medio-alto, y un soporte con estadísticas balanceadas.

## 8. Limitaciones
- Dataset parcial (solo primera generación limpia) limita generalización a generaciones posteriores.
- No se incluyen estadísticas especiales (Sp. Atk / Sp. Def) ni habilidades, que influyen en el metajuego.

## 9. Archivos Generados
### Datos CSV (resultados/eda/):
- `estadisticas_ataque_por_tipo.csv` - Estadísticas descriptivas de ataque por tipo
- `estadisticas_defensa_por_tipo.csv` - Estadísticas descriptivas de defensa por tipo
- `estadisticas_ps_por_tipo.csv` - Estadísticas descriptivas de PS por tipo
- `coeficiente_variacion_ps.csv` - Coeficiente de variación de PS por tipo
- `matriz_estadisticas_por_tipo.csv` - Matriz completa de estadísticas promedio por tipo
- `outliers_ps.csv` - Lista de Pokémon con valores atípicos en PS

### Visualizaciones (resultados/eda/ y figuras/):
- `outliers_boxplot.png` - Boxplots para detección de outliers en ataque y PS
- `correlacion_ataque_velocidad.png` - Gráfico de dispersión ataque vs velocidad
- `ps_por_tipo_boxplot.png` - Boxplot de distribución de PS por tipo
- `heatmap_stats_por_tipo.png` - Mapa de calor de estadísticas promedio por tipo
- `hist_ataque.png` - Histograma de distribución de ataque
- `scatter_ataque_velocidad.png` - Gráfico de dispersión ataque vs velocidad
- `violin_defensa_global.png` - Diagrama de violín de defensa global
- `violin_defensa_por_tipo.png` - Diagrama de violín de defensa por tipo

---
Este documento puede ampliarse al integrar métricas adicionales o normalizaciones para comparar tipos en escalas homogéneas.
# 8. Interpretación y Conclusiones

Este documento resume hallazgos clave de los análisis (estadística básica, agrupamientos, visualizaciones y EDA) sobre los Pokémon de la primera generación.

## 1. Tendencias de Ataque y Defensa
Los promedios por tipo muestran que algunos tipos sobresalen ofensivamente mientras otros son más balanceados defensivamente. (Ver `resultados/eda/estadisticas_ataque_por_tipo.csv` y `resultados/eda/estadisticas_defensa_por_tipo.csv`).
- Tipos con ataque más alto: suelen incluir combinaciones con Lucha, Fuego o Tierra (dependiendo de los registros presentes). 
- Tipos con defensa más alta: tienden a incluir variantes como Roca/Acero en datasets más amplios; en esta muestra parcial destacan aquellos con mayor mediana de Defensa (consultar archivos generados).

Conclusión: Hay especialización parcial: no todos los tipos que atacan fuerte son igual de rápidos ni resistentes.

## 2. Correlación Ataque vs Velocidad
La correlación Pearson calculada en `g_eda.py` es moderada-baja (ver consola y `resultados/eda/correlacion_ataque_velocidad.png`), indicando que un mayor ataque no garantiza mayor velocidad. Se justifica analizar cada tipo por separado si se buscara construir equipos balanceados.

## 3. Dispersión de PS
La desviación estándar de PS por tipo (archivo `resultados/eda/estadisticas_ps_por_tipo.csv`) evidencia que algunos tipos son más homogéneos (baja dispersión) mientras otros mezclan tanques y frágiles. Tipos con alta dispersión permiten roles variados dentro del mismo arquetipo. El coeficiente de variación se encuentra en `resultados/eda/coeficiente_variacion_ps.csv`.

## 4. Outliers
Se identificaron outliers usando IQR en Ataque y PS (`resultados/eda/outliers_ps.csv`). Estos valores extremos pueden distorsionar promedios; al diseñar estrategias conviene revisar si representan evoluciones avanzadas o excepciones. Las visualizaciones se encuentran en `resultados/eda/outliers_boxplot.png`.

## 5. Balance vs Especialización
- Más balanceados: tipos cuyos promedios de Ataque, Defensa, Velocidad y PS están cercanos a la mediana global del dataset y además con baja desviación. (Puede aproximarse consultando `resultados/eda/matriz_estadisticas_por_tipo.csv` con desviaciones estándar.)
- Más especializados: aquellos con un atributo claramente superior (p.ej. muy alto Ataque o Velocidad) y otros por debajo del promedio.

## 6. Visualizaciones Clave
- Histograma de Ataque: distribución relativamente sesgada hacia valores medios, con cola en superiores (`figuras/hist_ataque.png`).
- Scatter Ataque vs Velocidad: nube dispersa sin patrón lineal fuerte (`resultados/eda/correlacion_ataque_velocidad.png`).
- Boxplot PS por tipo: permite detectar qué tipos tienen mediana más alta y rango intercuartílico amplio (`resultados/eda/ps_por_tipo_boxplot.png`).
- Violines de Defensa: muestran forma de la distribución (multimodalidad potencial o concentración) (`figuras/violin_defensa_global.png` y `figuras/violin_defensa_por_tipo.png`).
- Heatmap de estadísticas: visualización completa de todas las estadísticas promedio por tipo (`resultados/eda/heatmap_stats_por_tipo.png`).

## 7. Recomendaciones Analíticas
1. Para equipos equilibrados: priorizar tipos con varianza moderada en PS y ataque medio (evita dependencia de un solo rol).
2. Para ofensiva rápida: seleccionar tipos con alta mediana de Velocidad aun sacrificando Defensa.
3. Outliers deben analizarse individualmente: pueden definir estrategia (sweeper, tanque) pero incrementan vulnerabilidad si caen.
4. Incluir mezcla de perfiles: uno con PS alto y defensa sólida, otro veloz con ataque medio-alto, y un soporte con estadísticas balanceadas.

## 8. Limitaciones
- Dataset parcial (solo primera generación limpia) limita generalización a generaciones posteriores.
- No se incluyen estadísticas especiales (Sp. Atk / Sp. Def) ni habilidades, que influyen en el metajuego.

## 9. Archivos Generados
### Datos CSV (resultados/eda/):
- `estadisticas_ataque_por_tipo.csv` - Estadísticas descriptivas de ataque por tipo
- `estadisticas_defensa_por_tipo.csv` - Estadísticas descriptivas de defensa por tipo
- `estadisticas_ps_por_tipo.csv` - Estadísticas descriptivas de PS por tipo
- `coeficiente_variacion_ps.csv` - Coeficiente de variación de PS por tipo
- `matriz_estadisticas_por_tipo.csv` - Matriz completa de estadísticas promedio por tipo
- `outliers_ps.csv` - Lista de Pokémon con valores atípicos en PS

### Visualizaciones (resultados/eda/ y figuras/):
- `outliers_boxplot.png` - Boxplots para detección de outliers en ataque y PS
- `correlacion_ataque_velocidad.png` - Gráfico de dispersión ataque vs velocidad
- `ps_por_tipo_boxplot.png` - Boxplot de distribución de PS por tipo
- `heatmap_stats_por_tipo.png` - Mapa de calor de estadísticas promedio por tipo
- `hist_ataque.png` - Histograma de distribución de ataque
- `scatter_ataque_velocidad.png` - Gráfico de dispersión ataque vs velocidad
- `violin_defensa_global.png` - Diagrama de violín de defensa global
- `violin_defensa_por_tipo.png` - Diagrama de violín de defensa por tipo

---
Este documento puede ampliarse al integrar métricas adicionales o normalizaciones para comparar tipos en escalas homogéneas.
