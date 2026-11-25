import json

ARCHIVO = "alumnos.json"


def cargar_alumnos():
    """Lee el archivo y devuelve el diccionario de alumnos."""
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)      


def guardar_alumnos(alumnos):
    """Escribe el diccionario de alumnos en el archivo."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)