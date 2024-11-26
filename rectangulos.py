import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definir la función para verificar si f(z) es conforme
def es_conforme(funcion, z):
    """
    Verifica si una función es analítica y su derivada es diferente de cero.
    """
    # Separar z en partes reales e imaginarias
    x, y = sp.symbols('x y', real=True)
    z_complex = x + sp.I * y  # Representación en términos de x + i*y

    # Expresar f(z) en términos de x + i*y
    f = sp.sympify(funcion).subs({'z': z_complex})

    # Separar parte real e imaginaria de f(z)
    u, v = sp.re(f), sp.im(f)

    # Calcular derivadas parciales para ecuaciones de Cauchy-Riemann
    du_dx, du_dy = sp.diff(u, x), sp.diff(u, y)
    dv_dx, dv_dy = sp.diff(v, x), sp.diff(v, y)

    # Verificar las ecuaciones de Cauchy-Riemann
    cauchy_riemann = (du_dx - dv_dy, du_dy + dv_dx)
    analitica = all(sp.simplify(eq) == 0 for eq in cauchy_riemann)

    # Verificar si la derivada f'(z) es diferente de cero
    df_dz = sp.diff(funcion, z)
    derivada_no_cero = sp.simplify(df_dz) != 0

    return analitica and derivada_no_cero

# Graficar el dominio y su imagen
def graficar_dom_imagen(funcion, limites):
    """
    Graficar dominio en z y su imagen en w bajo f(z).
    """
    x_min, x_max, y_min, y_max = limites

    # Crear una rejilla en el dominio
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y  # Dominio en el plano complejo

    # Evaluar la función en el dominio
    f = lambda z: eval(funcion)
    W = f(Z)

    # Graficar el dominio
    plt.figure(figsize=(12, 6))

    # Gráfica del dominio
    plt.subplot(1, 2, 1)
    plt.plot(Z.real.flatten(), Z.imag.flatten(), 'b.', markersize=1)
    plt.title("Dominio (z)")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.grid()

    # Gráfica de la imagen
    plt.subplot(1, 2, 2)
    plt.plot(W.real.flatten(), W.imag.flatten(), 'r.', markersize=1)
    plt.title("Imagen (w = f(z))")
    plt.xlabel("Re(w)")
    plt.ylabel("Im(w)")
    plt.grid()

    plt.show()

# Programa principal
if __name__ == "__main__":
    # Solicitar la función compleja y los límites del dominio
    funcion = input("Introduce la función compleja f(z): ")
    x_min = float(input("Límite inferior de Re(z): "))
    x_max = float(input("Límite superior de Re(z): "))
    y_min = float(input("Límite inferior de Im(z): "))
    y_max = float(input("Límite superior de Im(z): "))
    limites = (x_min, x_max, y_min, y_max)

    # Verificar si la función es conforme
    z = sp.symbols('z')
    if es_conforme(funcion, z):
        print("La función es conforme en el dominio dado.")
        graficar_dom_imagen(funcion, limites)
    else:
        print("La función no es conforme en el dominio dado.")
