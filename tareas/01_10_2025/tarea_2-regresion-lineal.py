import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

datos = {'Superficie_m2': [50, 70, 65, 90, 45], 'Num_Habitaciones': [1, 2, 2, 3, 1], 'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0], 'Precio_UF': [2500, 3800, 3500, 5200, 2100]}

df_datos = pd.DataFrame(datos)


# Variables independientes (X)
X = df_datos[['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km']]


# Variables dependientes (Y)
y = df_datos['Precio_UF']

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Calcular Predicciones
y_pred = modelo.predict(X)

# Evaluación Modelo
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print("Intercepto:", modelo.intercept_)
print("Coeficientes:", dict(zip(X.columns, modelo.coef_)))
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)

# Comparar reales vs predicciones
resultado = pd.DataFrame({
    "Precio_Real": y,
    "Precio_Predicho": y_pred
})

print("\nComparación:")
print(resultado)
