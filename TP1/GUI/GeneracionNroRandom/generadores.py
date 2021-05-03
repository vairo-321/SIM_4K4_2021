from random import uniform
import matplotlib.pyplot as plt
import numpy as np



class controlGeneradores():
    numeros=[]
    serie=[]
    def generarMetodoProvistoPorElLenguaje(self,cantidad):
        # Convierto tipos de datos
        cantidad = int(cantidad)

        # Inicializo datos
        numeros_generados = []

        # Genero lista de numeros aleatorios
        for i in range(0, cantidad):
            aleatorio_decimal = round(uniform(0, 1), 4)
            numeros_generados.append({
                "nro_orden": i + 1,
                "aleatorio_decimal": aleatorio_decimal
            })

        return numeros_generados



    def generarNrosAleatoriosMetodoCongruencialLineal(self,cantidad, semilla, a, m):
        cantidad = int(cantidad)
        semilla = round(float(semilla.replace(",", ".")), 4)
        a = round(float(a.replace(",", ".")), 4)
        m = round(float(m.replace(",", ".")), 4)
        # Inicializo datos
        numeros_generados = []
        aleatorio=None

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


    #def generarNrosAleatoriosMetodoCongruencialMixto(s=56, G=3, C=43,K=5, cantidad=100):

    def generarNrosAleatoriosMetodoCongruencialMixto(self,cantidad, semilla, a, c, m):
        cantidad = int(cantidad)
        semilla = round(float(semilla.replace(",", ".")), 4)
        a = round(float(a.replace(",", ".")), 4)
        c = round(float(c.replace(",", ".")), 4)
        m = round(float(m.replace(",", ".")), 4)
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


    def dividirEnIntervalos(self,cantIntervalos):
        maximo = 1
        minimo = 0
        paso = (maximo - minimo) / cantIntervalos
        intervalos = []
        mediaDeCadaIntervalo = []
        i = 0
        while i < cantIntervalos:
            if i == 0:
                intervalos.append([round(minimo, 2), round(minimo + paso, 2)])
            else:
                minimoAnterior = round(intervalos[i - 1][1], 2)
                intervalos.append([minimoAnterior, round(minimoAnterior + paso, 2)])

            i += 1

        for i in intervalos:
            mediaDeCadaIntervalo.append(round((i[0] + i[1]) / 2, 2))

        return intervalos, mediaDeCadaIntervalo

    # metodo que realiza el test de Chi cuadrado a una serie con una cantidad x de intervalos
    # Para cada intervalo de frecuencia toma como mayor o igual al limite inferior y como
    # menor a limite superior
    # Devuelve un vector con las frecuencias esperadas y un vector con las frecuencias reales

    #def testChiCuadrado(serie,cantIntervalos):

    def testChiCuadrado(self,serie,cantIntervalos):
        serie1=len(serie)
        numero=serie
        cantIntervalos=int(cantIntervalos)
        #tomando todos los random del metodo congruencial lineal en serie
        frecuenciaEsperada = [serie1 / cantIntervalos] * cantIntervalos
        frecuenciaReal = []

        intervalos, mediaDeCadaIntervalo = self.dividirEnIntervalos(cantIntervalos)
        # print(intervalos)

        for i in intervalos:
            contadorApariciones = 0

            item = 0

            while item < serie1:
                if numero[item] >= i[0] and numero[item] < i[1]:
                    contadorApariciones += 1

                item += 1

            frecuenciaReal.append(contadorApariciones)

        return frecuenciaEsperada, frecuenciaReal, mediaDeCadaIntervalo

    def prueba_chicuadrado(self, frecuencias_observadas, frecuencias_esperadas):

        diferencia1 = np.subtract(frecuencias_observadas, frecuencias_esperadas)
        # me devuelve FO-FE

        diferencia2 = np.power(diferencia1, 2)
        # me devuelve (FO-FE)^2

        diferencia3 = np.divide(diferencia2, frecuencias_esperadas)
        # me devuelve (FO-FE)^2/FE

        chi_cuadrado = round(np.sum(diferencia3),4)
        # me devuelve el total de sum (FO-FE)^2/FE

        return chi_cuadrado

    def generar_grafico(self,mediaDeCadaIntervalo,frecuenciasEsperadas,frecuenciasObserbadas):

        x = np.arange(len(mediaDeCadaIntervalo))
        width = 0.35
        fig,ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, frecuenciasObserbadas, width, label="Observadas")
        rects2 = ax.bar(x + width / 2, frecuenciasEsperadas, width, label="Esperadas")

        ax.set_ylabel("frecuenciasObserbadas")
        ax.set_title("Frecuencias esperadas y observadas")
        ax.set_xticks(x)
        ax.set_xticklabels(mediaDeCadaIntervalo)
        ax.legend()
        plt.show()


    def agregarUnNumeroMCL(self,cantidad, semilla, a, m,i):
        cantidad = int(cantidad)
        numero = []
        semilla = float(semilla)
        a = float(a)
        m = float(m)
        semilla = semilla * m
        semilla = int(semilla)
        i = int(i)
        for n in range(0, cantidad):
            aleatorio = round((a * semilla ) % m, 4)
            random = round(aleatorio / m, 4)
            numero.append({
                "nro_orden": n + 1 + i,
                "semilla": semilla,
                "aleatorio_decimal": random})
            semilla = random
        return numero

    def agregarUnNumeroMCM(self,cantidad,semilla, a, c, m,i):
        cantidad = int(cantidad)
        numero=[]
        semilla = float(semilla)
        a = float(a)
        m = float(m)
        c= float(c)
        semilla=semilla*m
        semilla=int(semilla)
        i = int(i)
        for n in range(0, cantidad):
            aleatorio = round((a * semilla + c) % m, 4)
            random = round(aleatorio / m, 4)
            numero.append({
            "nro_orden": n + 1 + i,
            "semilla": semilla,
            "aleatorio_decimal": random})
            semilla = random
        return numero