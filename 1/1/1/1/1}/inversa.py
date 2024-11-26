# Importar las bibliotecas necesarias nuevamente debido al reinicio
import numpy as np
import matplotlib.pyplot as plt

# Redefinir los parámetros necesarios
a = 1  # Límite izquierdo en el plano z
b = 3  # Límite derecho en el plano z

# Coordenadas para las circunferencias en el plano w
center_outer = (1/(2*a), 0)  # Centro de la circunferencia exterior
radius_outer = 1/(2*a)       # Radio de la circunferencia exterior (roja)
center_inner = (1/(2*b), 0)  # Centro de la circunferencia interior
radius_inner = 1/(2*b)       # Radio de la circunferencia interior (azul)

# Crear figura y subgráficos
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plano z
ax[0].set_title("Plano - z")
ax[0].set_xlabel("Re")
ax[0].set_ylabel("Im")
ax[0].axhline(0, color="black", linewidth=0.5)
ax[0].axvline(0, color="black", linewidth=0.5)
ax[0].plot([a, a], [-2, 2], "r-", label="a")
ax[0].plot([b, b], [-2, 2], "b-", label="b")
ax[0].fill_betweenx([-2, 2], a, b, color="peachpuff", alpha=0.6)
ax[0].legend()
ax[0].set_xlim(-0.5, 4)
ax[0].set_ylim(-2.5, 2.5)
ax[0].grid(True)

# Plano w
ax[1].set_title("Plano - w")
ax[1].set_xlabel("Re")
ax[1].set_ylabel("Im")
ax[1].axhline(0, color="black", linewidth=0.5)
ax[1].axvline(0, color="black", linewidth=0.5)

# Circunferencia exterior (roja)
outer_circle = plt.Circle(center_outer, radius_outer, color="red", fill=False, linewidth=2, label="1/a")
ax[1].add_artist(outer_circle)

# Circunferencia interior (azul)
inner_circle = plt.Circle(center_inner, radius_inner, color="blue", fill=False, linewidth=2, label="1/b")
ax[1].add_artist(inner_circle)

# Colorear las regiones
theta = np.linspace(0, 2 * np.pi, 500)
x_outer = center_outer[0] + radius_outer * np.cos(theta)
y_outer = center_outer[1] + radius_outer * np.sin(theta)
x_inner = center_inner[0] + radius_inner * np.cos(theta)
y_inner = center_inner[1] + radius_inner * np.sin(theta)

# Color rojo dentro del círculo rojo
ax[1].fill_betweenx(y_outer, -radius_outer, x_outer, color="lightcoral", alpha=0.6)

# Color azul dentro del círculo azul
ax[1].fill_betweenx(y_inner, -radius_inner, x_inner, color="lightblue", alpha=0.6)

# Etiquetas de las circunferencias
ax[1].text(center_outer[0] + radius_outer + 0.02, 0, "1/a", color="red", fontsize=10)
ax[1].text(center_inner[0] - radius_inner - 0.04, 0, "1/b", color="blue", fontsize=10)

ax[1].set_xlim(-0.1, 0.6)
ax[1].set_ylim(-0.4, 0.4)
ax[1].grid(True)
ax[1].set_aspect("equal", adjustable="box")

plt.tight_layout()
plt.show()
