from archivos import cargar_alumnos
from alumnos import registrar_alumno, listar_alumnos, buscar_alumno, modificar_alumno, eliminar_alumno
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print("\n======== GESTIÓN DE ALUMNOS ========")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadísticas")
    print("7. Salir")


def main():
    alumnos = cargar_alumnos()

    while True:                                 
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alumno(alumnos)
        elif opcion == "2":
            listar_alumnos(alumnos)
        elif opcion == "3":
            buscar_alumno(alumnos)
        elif opcion == "4":
            modificar_alumno(alumnos)
        elif opcion == "5":
            eliminar_alumno(alumnos)
        elif opcion == "6":
            mostrar_estadisticas(alumnos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break                               
        else:
            print("Opcion inválida. Vuelva a intentar.")


if __name__ == "__main__":
    main()