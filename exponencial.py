import numpy as np
import matplotlib.pyplot as plt

# Definir la región en el plano z
x = np.linspace(-1, 1, 100)  # Valores de x en [-1, 1]
y = np.linspace(0, np.pi, 100)  # Valores de y en [0, π]
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  # Crear la región rectangular como números complejos

# Aplicar la transformación w = e^z
W = np.exp(Z)

# Definir puntos clave en el plano z
puntos_z = {
    "A": -1 + 1j * np.pi,
    "B": 1 + 1j * np.pi,
    "D": -1 + 0j,
    "C": 1 + 0j
}
puntos_w = {k: np.exp(v) for k, v in puntos_z.items()}  # Imagen de los puntos en el plano w

# Graficar la región en el plano z
plt.figure(figsize=(14, 7))

# Plano z
plt.subplot(1, 2, 1)
plt.title("Plano - z")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.fill_between(x, 0, np.pi, color="orange", alpha=0.3, label="Región original")
plt.plot(np.real(Z), np.imag(Z), color="blue", alpha=0.6)  # Líneas horizontales
plt.plot(np.real(Z.T), np.imag(Z.T), color="blue", alpha=0.6)  # Líneas verticales
for k, v in puntos_z.items():
    plt.scatter(np.real(v), np.imag(v), color="red")
    plt.text(np.real(v), np.imag(v) + 0.1, f"{k}", color="red")
plt.legend()
plt.grid()

# Plano w
plt.subplot(1, 2, 2)
plt.title("Plano - w (Transformado)")
plt.xlabel("Re(w)")
plt.ylabel("Im(w)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.fill_between(np.real(W[0, :]), 0, np.imag(W[:, 0]), color="orange", alpha=0.3, label="Región transformada")
plt.plot(np.real(W), np.imag(W), color="red", alpha=0.6)  # Líneas horizontales transformadas
plt.plot(np.real(W.T), np.imag(W.T), color="red", alpha=0.6)  # Líneas verticales transformadas
for k, v in puntos_w.items():
    plt.scatter(np.real(v), np.imag(v), color="blue")
    plt.text(np.real(v), np.imag(v) + 0.1, f"f({k})", color="blue")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
