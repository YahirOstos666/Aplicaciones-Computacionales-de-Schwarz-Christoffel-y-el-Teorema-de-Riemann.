import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones de mapeo
def z_squared(z):
    return z**2

def reciprocal(z):
    return 1/z

def sqrt_z(z):
    return np.sqrt(z)

def exp_z(z):
    return np.exp(z)

def log_z(z):
    return np.log(z)

def sin_z(z):
    return np.sin(z)

def joukowsky(z):
    return z + 1/z

# Lista de funciones y sus nombres
functions = [
    (z_squared, r"$z^2$"),
    (reciprocal, r"$1/z$"),
    (sqrt_z, r"$z^{1/2}$"),
    (exp_z, r"$e^z$"),
    (log_z, r"$\log(z)$"),
    (sin_z, r"$\sin(z)$"),
    (joukowsky, r"Joukowsky"),
]

# Crear una cuadrícula en el plano z
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
x, y = np.meshgrid(x, y)
z = x + 1j * y

# Eliminar el origen para funciones como 1/z y log(z)
z[np.isclose(z, 0)] = np.nan

# Generar los gráficos
fig, axes = plt.subplots(len(functions), 2, figsize=(12, 4 * len(functions)))

for i, (func, name) in enumerate(functions):
    # Calcular el mapeo
    w = func(z)

    # Plano z
    axes[i, 0].set_title(f"Plano z: Región original ({name})")
    axes[i, 0].set_xlabel("Re")
    axes[i, 0].set_ylabel("Im")
    axes[i, 0].plot(np.real(z), np.imag(z), 'b-', alpha=0.5)
    axes[i, 0].plot(np.real(z.T), np.imag(z.T), 'r-', alpha=0.5)
    axes[i, 0].grid(True)
    axes[i, 0].set_aspect('equal', adjustable='box')

    # Plano w (transformado)
    axes[i, 1].set_title(f"Plano w: Transformado ({name})")
    axes[i, 1].set_xlabel("Re")
    axes[i, 1].set_ylabel("Im")
    axes[i, 1].plot(np.real(w), np.imag(w), 'b-', alpha=0.5)
    axes[i, 1].plot(np.real(w.T), np.imag(w.T), 'r-', alpha=0.5)
    axes[i, 1].grid(True)
    axes[i, 1].set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()
