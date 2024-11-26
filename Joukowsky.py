import numpy as np
import matplotlib.pyplot as plt

# Función de Joukowsky
def joukowsky(z):
    return z + 1 / z

# Crear los círculos en el plano z
theta = np.linspace(0, 2 * np.pi, 500)  # Ángulo de 0 a 2π
radii = [1.2, 1.5, 2.0, 3.0]  # Radios de los círculos
circles = [r * np.exp(1j * theta) for r in radii]

# Mapear los círculos al plano w usando la transformación de Joukowsky
ellipses = [joukowsky(z) for z in circles]

# Crear la figura
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Gráfica en el plano z
axes[0].set_title("Círculos en el Plano Z")
for circle in circles:
    axes[0].plot(circle.real, circle.imag, 'b')  # Círculos en azul
axes[0].axhline(0, color='black', linewidth=0.5)
axes[0].axvline(0, color='black', linewidth=0.5)
axes[0].set_xlabel("Re(z)")
axes[0].set_ylabel("Im(z)")
axes[0].grid(True)
axes[0].axis("equal")

# Gráfica en el plano w
axes[1].set_title("Elipses en el Plano W")
for ellipse in ellipses:
    axes[1].plot(ellipse.real, ellipse.imag, 'r')  # Elipses en rojo
axes[1].axhline(0, color='black', linewidth=0.5)
axes[1].axvline(0, color='black', linewidth=0.5)
axes[1].set_xlabel("Re(w)")
axes[1].set_ylabel("Im(w)")
axes[1].grid(True)
axes[1].axis("equal")

plt.tight_layout()
plt.show()
