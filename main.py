# main.py

from Conversor import Conversor


def main():
    print("Conversor de ángulos:")
    print("1. Grados a Radianes")
    print("2. Radianes a Grados")

    # Obtener la opción del usuario
    opcion = input("Elige una opción (1 o 2): ").strip()

    if opcion == "1":
        # Conversión de Grados a Radianes
        grados = float(input("Introduce el valor en grados: "))
        radianes = Conversor.degrees_to_radians(grados)
        print(f"{grados} grados son {radianes:.4f} radianes.")

    elif opcion == "2":
        # Conversión de Radianes a Grados
        radianes = float(input("Introduce el valor en radianes: "))
        grados = Conversor.radians_to_degrees(radianes)
        print(f"{radianes:.4f} radianes son {grados:.2f} grados.")

    else:
        print("Opción no válida. Por favor, elige 1 o 2.")


if __name__ == "__main__":
    main()
