import numpy as np
import matplotlib.pyplot as plt

# Crear puntos para regiones entre rectas
def generar_region_entre_rectas(recta1, recta2, x_min, x_max, pasos=500):
    """
    Genera los límites superior e inferior entre dos rectas.
    :param recta1: Ecuación de la primera recta (como una cadena, e.g., "7", "7*x + 1").
    :param recta2: Ecuación de la segunda recta (como una cadena).
    :param x_min: Límite inferior de x.
    :param x_max: Límite superior de x.
    :param pasos: Número de divisiones entre x_min y x_max.
    :return: Arreglos de puntos x, y_min, y_max.
    """
    x = np.linspace(x_min, x_max, pasos)
    y1 = eval(recta1)
    y2 = eval(recta2)

    # Calcular los límites de la región
    y_min, y_max = np.minimum(y1, y2), np.maximum(y1, y2)
    return x, y_min, y_max

# Transformación conforme
def transformar_region(x, y_min, y_max, funcion):
    """
    Transforma los límites de la región con una función conforme.
    :param x: Valores de x en la región original.
    :param y_min: Límites inferiores de y.
    :param y_max: Límites superiores de y.
    :param funcion: Función conforme (cadena, e.g., "z**2", "(z + 1)/(z - 1)").
    :return: Límites transformados w_min y w_max.
    """
    z_min = x + 1j * y_min
    z_max = x + 1j * y_max
    z_func = lambda z: eval(funcion)

    w_min = np.vectorize(z_func)(z_min)
    w_max = np.vectorize(z_func)(z_max)
    return w_min, w_max

# Visualización de región original y transformada
def visualizar_transformacion(x, y_min, y_max, w_min, w_max):
    """
    Visualiza las regiones original y transformada.
    :param x: Valores de x en la región original.
    :param y_min: Límites inferiores de y en la región original.
    :param y_max: Límites superiores de y en la región original.
    :param w_min: Límites inferiores de la región transformada.
    :param w_max: Límites superiores de la región transformada.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Región original
    axes[0].fill_between(x, y_min, y_max, color="blue", alpha=0.5)
    axes[0].set_title("Región Original")
    axes[0].set_xlabel("Re(z)")
    axes[0].set_ylabel("Im(z)")
    axes[0].grid(True)

    # Región transformada
    axes[1].fill_between(np.real(w_min), np.imag(w_min), np.imag(w_max), color="red", alpha=0.5)
    axes[1].set_title("Región Transformada")
    axes[1].set_xlabel("Re(w)")
    axes[1].set_ylabel("Im(w)")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

# Interfaz principal
def main():
    print("Definir límites de las regiones entre rectas:")
    x_min = float(input("Límite inferior de x: "))
    x_max = float(input("Límite superior de x: "))

    print("\nIntroduce las ecuaciones de las rectas (por ejemplo, '7', '7*x + 1'):")
    recta1 = input("Ecuación de la primera recta (y1): ")
    recta2 = input("Ecuación de la segunda recta (y2): ")

    pasos = int(input("Número de pasos en la cuadrícula (mayor = más detalle): "))

    print("\nIntroduce una función conforme para transformar (e.g., 'z**2', '(z + 1)/(z - 1)'):")
    funcion = input("Función w(z): ")

    # Generar región entre las rectas
    x, y_min, y_max = generar_region_entre_rectas(recta1, recta2, x_min, x_max, pasos)

    # Transformar la región
    w_min, w_max = transformar_region(x, y_min, y_max, funcion)

    # Visualizar resultados
    visualizar_transformacion(x, y_min, y_max, w_min, w_max)

# Ejecutar programa
if __name__ == "__main__":
    main()
