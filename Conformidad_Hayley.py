import numpy as np
import matplotlib.pyplot as plt

# Definimos la función conforme w(z) = (z - i) / (z + i)
def w(z):
    return (z - 1j) / (z + 1j)

# Crear el semiplano superior con líneas verticales y horizontales
x = np.linspace(-2, 2, 500)
y = np.linspace(0.1, 3, 500)  # y > 0 para el semiplano superior
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Generar líneas verticales y horizontales en el semiplano superior
vertical_lines_x = np.linspace(-2, 2, 10)
horizontal_lines_y = np.linspace(0.2, 3, 10)

# Graficar las líneas en el semiplano superior y su imagen bajo w(z)
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Subplot del semiplano superior
ax[0].set_title("Semiplano Superior (z)")
for x_val in vertical_lines_x:
    ax[0].plot(np.full_like(y, x_val), y, 'b', alpha=0.7)  # Líneas verticales
for y_val in horizontal_lines_y:
    ax[0].plot(x, np.full_like(x, y_val), 'r', alpha=0.7)  # Líneas horizontales
ax[0].set_xlim(-2, 2)
ax[0].set_ylim(0, 3)
ax[0].set_xlabel("Re(z)")
ax[0].set_ylabel("Im(z)")
ax[0].grid()

# Subplot de la imagen conforme
ax[1].set_title("Imagen Conforme w(z)")
for x_val in vertical_lines_x:
    z_line = x_val + 1j * y  # Línea vertical en el semiplano superior
    w_line = w(z_line)  # Imagen conforme
    ax[1].plot(w_line.real, w_line.imag, 'b', alpha=0.7)  # Mapeo de líneas verticales
for y_val in horizontal_lines_y:
    z_line = x + 1j * y_val  # Línea horizontal en el semiplano superior
    w_line = w(z_line)  # Imagen conforme
    ax[1].plot(w_line.real, w_line.imag, 'r', alpha=0.7)  # Mapeo de líneas horizontales
ax[1].set_xlim(-1.5, 1.5)
ax[1].set_ylim(-1.5, 1.5)
ax[1].set_xlabel("Re(w)")
ax[1].set_ylabel("Im(w)")
ax[1].grid()

plt.tight_layout()
plt.show()
