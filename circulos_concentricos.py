import numpy as np
import matplotlib.pyplot as plt

# Definir la función conforme
def w(z):
    return z**2 + 10  # Función conforme que cambia la forma de la región

def plot_circular_regions():
    # Definir parámetros de los círculos
    num_points = 100
    theta = np.linspace(0, 2*np.pi, num_points)  # ángulos de 0 a 2pi
    radii = [1, 2, 3]  # Radios para círculos concéntricos
    centers = [(0, 0), (5, 5)]  # Centros para círculos concéntricos y no concéntricos

    # Crear la figura
    plt.figure(figsize=(12, 6))

    # Subplot para la región original (círculos)
    plt.subplot(1, 2, 1)

    for r in radii:
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        plt.fill(x, y, alpha=0.5, label=f'Radio {r}')

    for center in centers:
        for r in radii:
            x = center[0] + r * np.cos(theta)
            y = center[1] + r * np.sin(theta)
            plt.plot(x, y, label=f'Centro {center} y Radio {r}', linestyle='--')

    plt.title('Regiones Circulares Originales')
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.legend()
    plt.grid()

    # Subplot para la región transformada
    plt.subplot(1, 2, 2)

    for r in radii:
        # Convertir las coordenadas originales en complejas
        circle_points = [r * np.exp(1j * t) for t in theta]
        # Transformar la región con la función conforme
        transformed_points = [w(z) for z in circle_points]
        transformed_x = [p.real for p in transformed_points]
        transformed_y = [p.imag for p in transformed_points]
        plt.fill(transformed_x, transformed_y, alpha=0.5, label=f'Radio {r}')

    for center in centers:
        for r in radii:
            # Crear círculo no concéntrico y transformarlo
            circle_points = [r * np.exp(1j * t) + center[0] + 1j * center[1] for t in theta]
            transformed_points = [w(z) for z in circle_points]
            transformed_x = [p.real for p in transformed_points]
            transformed_y = [p.imag for p in transformed_points]
            plt.plot(transformed_x, transformed_y, label=f'Centro {center} y Radio {r}', linestyle='--')

    plt.title('Regiones Circulares Transformadas')
    plt.xlabel('Re(w)')
    plt.ylabel('Im(w)')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

plot_circular_regions()
