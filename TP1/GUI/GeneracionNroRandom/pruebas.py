import random
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

def filtrarAleatorio():
    numeros=[{'nro_orden': 1, 'semilla': 4, 'aleatorio_decimal': 0.5714}, {'nro_orden': 2, 'semilla': 4, 'aleatorio_decimal': 0.0}, {'nro_orden': 3, 'semilla': 0, 'aleatorio_decimal': 0.2857}, {'nro_orden': 4, 'semilla': 2, 'aleatorio_decimal': 0.1429}]
    resultado=[]
    for diccionario in numeros:
        resultado.append(diccionario['aleatorio_decimal'])
    return resultado
def filtrarSemilla():
    numeros=[{'nro_orden': 4, 'semilla': 2, 'aleatorio_decimal': 0.1429}]
    resultado=[]
    for diccionario in numeros:
        resultado.append(diccionario['semilla'])
    return resultado

numeros=[{'nro_orden': 1, 'semilla': 4, 'aleatorio_decimal': 0.5714}, {'nro_orden': 2, 'semilla': 4, 'aleatorio_decimal': 0.0}, {'nro_orden': 3, 'semilla': 0, 'aleatorio_decimal': 0.2857}, {'nro_orden': 4, 'semilla': 2, 'aleatorio_decimal': 0.1429}]
ultimo= numeros[-1]
def agregarNumero(a=4,m=3,c=2):
    semilla= filtrarSemilla()
    semilla = round(float(semilla.replace(",", ".")), 4)
    a = round(float(a.replace(",", ".")), 4)
    m = round(float(m.replace(",", ".")), 4)
    c = round(float(c.replace(",", ".")), 4)
    random = (a * semilla + c) % m

    numeros.append({
        "semilla": semilla,
        "aleatorio_decimal": random
    })
    semilla = random
    return numeros

print(ultimo)
print(filtrarAleatorio())
print(filtrarSemilla())


print(generarNrosAleatoriosMetodoCongruencialMixto())
print(generarNrosAleatoriosMetodoCongruencialLineal())
