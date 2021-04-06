def generarNrosAleatoriosMetodoCongruencialLineal(cantidad=4, semilla=4, a=3, m=7):
    numeros_generados = []

    # Genero lista de numeros aleatorios
    for i in range(0, cantidad):
        if i == 0:
            aleatorio = round(semilla % m, 4)
        else:
            aleatorio = round((a * semilla) % m, 4)
        aleatorio_decimal = round(aleatorio / m, 4)
        numeros_generados.append({
            "nro_orden": i + 1,
            "semilla": semilla,
            "aleatorio_decimal": aleatorio_decimal
        })
        semilla = aleatorio

    return numeros_generados

def generarNrosAleatoriosMetodoCongruencialMixto(cantidad=4, semilla=4, a=3,c=2, m=7):
    # Inicializo datos
    numeros_generados = []

    # Genero lista de numeros aleatorios
    for i in range(0, cantidad):
        if i == 0:
            aleatorio = round(semilla % m, 4)
        else:
            aleatorio = round((a * semilla + c) % m, 4)
        aleatorio_decimal = round(aleatorio / m, 4)
        numeros_generados.append({
            "nro_orden": i + 1,
            "semilla": semilla,
            "aleatorio_decimal": aleatorio_decimal
        })
        semilla = aleatorio

    return numeros_generados

print(generarNrosAleatoriosMetodoCongruencialMixto())
print(generarNrosAleatoriosMetodoCongruencialLineal())