def cantidad_alumnos(alumnos):
    """Devuelve la cantidad total de alumnos."""
    return len(alumnos)                        

def promedio_notas(alumnos):
    """Devuelve el promedio de todas las notas."""
    suma = 0
    for datos in alumnos.values():             
        suma += datos["nota"]
    return suma / len(alumnos)                 


def alumno_mayor_nota(alumnos):
    """Devuelve el DNI del alumno con la nota más alta."""
    dni_mejor = None
    nota_mejor = -1                            

    for dni, datos in alumnos.items():
        if datos["nota"] > nota_mejor:          
            nota_mejor = datos["nota"]          
            dni_mejor = dni
    return dni_mejor


def cantidad_aprobados(alumnos):
    """Devuelve cuántos alumnos tienen nota mayor o igual a 6."""
    contador = 0
    for datos in alumnos.values():
        if datos["nota"] >= 6:
            contador += 1
    return contador


def cantidad_desaprobados(alumnos):
    """Devuelve cuántos alumnos tienen nota menor a 6."""
    return cantidad_alumnos(alumnos) - cantidad_aprobados(alumnos)


def mostrar_estadisticas(alumnos):
    """Muestra todas las estadísticas juntas (la llama el menú)."""
    print("\n--- Estadísticas ---")

    if not alumnos:
        print("No hay alumnos registrados.")
        return

    dni_mejor = alumno_mayor_nota(alumnos)
    mejor = alumnos[dni_mejor]

    print(f"Cantidad total de alumnos: {cantidad_alumnos(alumnos)}")
    print(f"Promedio de notas: {promedio_notas(alumnos):.2f}")  
    print(f"Alumno con mayor nota: {mejor['nombre']} {mejor['apellido']} "
          f"(DNI {dni_mejor}) con {mejor['nota']:g}")
    print(f"Aprobados (nota >= 6): {cantidad_aprobados(alumnos)}")
    print(f"Desaprobados (nota < 6): {cantidad_desaprobados(alumnos)}")