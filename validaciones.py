def pedir_dni(mensaje="DNI: "):
    """Pide un DNI. Solo permite números, de 7 u 8 dígitos."""
    while True:
        dni = input(mensaje)
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return dni                         
        print("Error: numero DNI no permitido.")


def pedir_edad():
    """Pide la edad. No permite edades negativas ni letras."""
    while True:                              
        try:
            edad = int(input("Edad: "))       
            if edad >= 0:
                return edad                    
            print("Error: la edad no puede ser negativa.")
        except ValueError:
            print("Error: ingrese un número entero.")


def pedir_nota():
    """Pide la nota. Solo permite valores entre 0 y 10."""
    while True:
        try:
            nota = float(input("Nota: "))     
            if 0 <= nota <= 10:
                return nota
            print("Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: ingrese un número.")