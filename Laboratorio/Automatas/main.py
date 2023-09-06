import csv
import random

# Cargar la función de transición desde el archivo CSV
def cargar_transiciones():
    transiciones = {}
    with open('transiciones.csv', 'r') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            estado_actual = fila['estado_actual']
            simbolo = fila['simbolo']
            estado_siguiente = fila['estado_siguiente']
            if estado_actual not in transiciones:
                transiciones[estado_actual] = {}
            transiciones[estado_actual][simbolo] = estado_siguiente
    return transiciones

# Verificar si una palabra es aceptada por el autómata
def verificar_palabra(palabra, transiciones, estado_inicial, estados_finales):
    estado_actual = estado_inicial
    for simbolo in palabra:
        if simbolo in transiciones[estado_actual]:
            estado_actual = transiciones[estado_actual][simbolo]
        else:
            return False
    return estado_actual in estados_finales

def generar_palabra_aleatoria(alfabeto, longitud):
    return ''.join(random.choice(alfabeto) for _ in range(longitud))

if __name__ == "__main__":
    transiciones = cargar_transiciones()
    estado_inicial = 'q0'
    estados_finales = {'q1'}

    for _ in range(2000):
        longitud_palabra = random.randint(1, 10)  # Cambia el rango según tu preferencia
        palabra = generar_palabra_aleatoria('012', longitud_palabra)  # Actualiza el alfabeto
        aceptada = verificar_palabra(palabra, transiciones, estado_inicial, estados_finales)
        resultado = "Aceptado" if aceptada else "No Aceptado"
        print(f">> {palabra} -> {resultado}")
