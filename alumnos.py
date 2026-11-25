from archivos import guardar_alumnos
from validaciones import pedir_dni, pedir_edad, pedir_nota


#  PUNTO 1: CARGAR ALUMNOS 
def registrar_alumno(alumnos):
    """Registra un alumno nuevo validando DNI, edad y nota."""
    print("\n--- Registrar alumno ---")

    dni = pedir_dni()                          
    if dni in alumnos:                         
        print("Error: ya existe un alumno con ese DNI.")
        return                                 

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = pedir_edad()                        
    nota = pedir_nota()                         

    alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    guardar_alumnos(alumnos)
    print("Alumno registrado correctamente.")



def mostrar_alumno(dni, datos):
    """Muestra el formato de la consigna.
    Está separada para reutilizarla también en buscar, modificar y eliminar."""
    print(f"DNI: {dni}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Apellido: {datos['apellido']}")
    print(f"Edad: {datos['edad']}")
    print(f"Nota: {datos['nota']}")          
    print("-" * 25)                             


def listar_alumnos(alumnos):
    """Muestra TODOS los alumnos registrados."""
    print("\n--- Listado de alumnos ---")
    
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    for dni, datos in alumnos.items():
        mostrar_alumno(dni, datos)

#  PUNTO 3: BUSCAR ALUMNO 
def buscar_alumno(alumnos):
    """Busca un alumno por su DNI y muestra sus datos."""
    print("\n--- Buscar alumno ---")
    dni = input("Ingrese el DNI a buscar: ")

    if dni in alumnos:
        mostrar_alumno(dni, alumnos[dni])      
    else:
        print("No se encontró un alumno con ese DNI.")

#  PUNTO 4: MODIFICAR ALUMNO 
def modificar_alumno(alumnos):
    """Permite modificar nombre, apellido, edad o nota de un alumno."""
    print("\n--- Modificar alumno ---")
    dni = input("Ingrese el DNI del alumno a modificar: ")

    if dni not in alumnos:
        print("No se encontró un alumno con ese DNI.")
        return

    print("Datos actuales:")
    mostrar_alumno(dni, alumnos[dni])

    print("¿Qué desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Nota")
    opcion = input("Opción: ")

    if opcion == "1":
        alumnos[dni]["nombre"] = input("Nuevo nombre: ")
    elif opcion == "2":
        alumnos[dni]["apellido"] = input("Nuevo apellido: ")
    elif opcion == "3":
        alumnos[dni]["edad"] = pedir_edad()
    elif opcion == "4":
        alumnos[dni]["nota"] = pedir_nota()
    else:
        print("Opción inválida. No se modificó ningún dato.")
        return                                

    guardar_alumnos(alumnos)
    print("Alumno modificado correctamente.")


#  PUNTO 5: ELIMINAR ALUMNO 
def eliminar_alumno(alumnos):
    """Elimina un alumno por su DNI, pidiendo confirmación antes."""
    print("\n--- Eliminar alumno ---")
    dni = input("Ingrese el DNI del alumno a eliminar: ")

    if dni not in alumnos:
        print("No se encontró un alumno con ese DNI.")
        return

    mostrar_alumno(dni, alumnos[dni])

    confirmacion = input("¿Seguro que desea eliminarlo? (s/n): ")

    if confirmacion == "s":
        del alumnos[dni]                      
        guardar_alumnos(alumnos)              
        print("Alumno eliminado correctamente.")
    else:
        print("Operación cancelada. No se eliminó nada.")






















































