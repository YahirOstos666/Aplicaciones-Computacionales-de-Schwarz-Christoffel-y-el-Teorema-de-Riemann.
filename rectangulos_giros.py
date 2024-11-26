import numpy as np
import matplotlib.pyplot as plt

# Solicitar los vértices del rectángulo al usuario
print("Introduce las coordenadas de los vértices del rectángulo en el plano complejo:")
print("Formato: número complejo (ejemplo: -2-2j, 1-2j, 1+1j, -2+1j)")
vertices = input("Vértices del rectángulo separados por comas: ").strip()
vertices = [complex(v) for v in vertices.split(",")]

# Asegurarse de que el rectángulo esté cerrado (agregar el primer vértice al final si es necesario)
if vertices[0] != vertices[-1]:
    vertices.append(vertices[0])

# Solicitar la función de transformación al usuario
print("\nDefine la función de transformación \( w(z) \). Por ejemplo:")
print("- Para \( w(z) = z + 1 \), escribe: z + 1")
print("- Para \( w(z) = (1 + 1j)*z + (1 - 1j) \), escribe: (1 + 1j)*z + (1 - 1j)")
func_str = input("Función \( w(z) \): ").strip()

# Convertir la función a un objeto ejecutable
def transform(z):
    return eval(func_str)

# Aplicar la transformación a los vértices
transformed_vertices = [transform(v) for v in vertices]

# Crear los gráficos
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Graficar el rectángulo original
ax[0].plot([v.real for v in vertices], [v.imag for v in vertices], 'b-o', label="Original")
ax[0].set_title("Rectángulo Original (z-plane)")
ax[0].set_xlabel("Re(z)")
ax[0].set_ylabel("Im(z)")
ax[0].grid()
ax[0].axhline(0, color='black', linewidth=0.5)
ax[0].axvline(0, color='black', linewidth=0.5)
ax[0].legend()

# Graficar el rectángulo transformado
ax[1].plot([v.real for v in transformed_vertices], [v.imag for v in transformed_vertices], 'r-o', label="Transformado")
ax[1].set_title("Rectángulo Transformado (w-plane)")
ax[1].set_xlabel("Re(w)")
ax[1].set_ylabel("Im(w)")
ax[1].grid()
ax[1].axhline(0, color='black', linewidth=0.5)
ax[1].axvline(0, color='black', linewidth=0.5)
ax[1].legend()

plt.tight_layout()
plt.show()
