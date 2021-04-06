from random import uniform
import numpy as np

class controlGeneradores():

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


    # segun video (ver minuto 10:30)
    def generarNrosAleatoriosMetodoCongruencialLineal(self,cantidad, semilla, a, m):
        # Inicializo datos
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


    #def generarNrosAleatoriosMetodoCongruencialMixto(s=56, G=3, C=43,K=5, cantidad=100):


    def generarNrosAleatoriosMetodoCongruencialMixto(self,cantidad, semilla, a,c, m):

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


    def dividirEnIntervalos(self,cantIntervalos=10, maximo=1, minimo=0):
        paso = (maximo - minimo) / cantIntervalos
        intervalos = []
        mediaDeCadaIntervalo = []
        i = 0
        while i < cantIntervalos:
            if i == 0:
                intervalos.append([round(minimo, 4), round(minimo + paso, 4)])
            else:
                minimoAnterior = round(intervalos[i - 1][1], 4)
                intervalos.append([minimoAnterior, round(minimoAnterior + paso, 4)])

            i += 1

        for i in intervalos:
            mediaDeCadaIntervalo.append(round((i[0] + i[1]) / 2, 4))

        return intervalos, mediaDeCadaIntervalo

    # metodo que realiza el test de Chi cuadrado a una serie con una cantidad x de intervalos
    # Para cada intervalo de frecuencia toma como mayor o igual al limite inferior y como
    # menor a limite superior
    # Devuelve un vector con las frecuencias esperadas y un vector con las frecuencias reales

    #def testChiCuadrado(serie,cantIntervalos):
    def testChiCuadrado( self,cantIntervalos=10):
        #tomando todos los random del metodo congruencial lineal en serie
        serie=[0.0112, 0.1904, 0.2368, 0.0256, 0.4352, 0.3984, 0.7728, 0.1376, 0.3392, 0.7664, 0.0288, 0.4896, 0.3232, 0.4944, 0.4048, 0.8816, 0.9872, 0.7824, 0.3008, 0.1136, 0.9312, 0.8304, 0.1168, 0.9856, 0.7552, 0.8384, 0.2528, 0.2976, 0.0592, 0.0064, 0.1088, 0.8496, 0.4432, 0.5344, 0.0848, 0.4416, 0.5072, 0.6224, 0.5808, 0.8736, 0.8512, 0.4704, 0.9968, 0.9456, 0.0752, 0.2784, 0.7328, 0.4576, 0.7792, 0.2464, 0.1888, 0.2096, 0.5632, 0.5744, 0.7648, 0.0016, 0.0272, 0.4624, 0.8608, 0.6336, 0.7712, 0.1104, 0.8768, 0.9056, 0.3952, 0.7184, 0.2128, 0.6176, 0.4992, 0.4864, 0.2688, 0.5696, 0.6832, 0.6144, 0.4448, 0.5616, 0.5472, 0.3024, 0.1408, 0.3936, 0.6912, 0.7504, 0.7568, 0.8656, 0.7152, 0.1584, 0.6928, 0.7776, 0.2192, 0.7264, 0.3488, 0.9296, 0.8032, 0.6544, 0.1248, 0.1216, 0.0672, 0.1424, 0.4208, 0.1536]
        frecuenciaEsperada = [len(serie)/ cantIntervalos] * cantIntervalos
        frecuenciaReal = []

        intervalos, mediaDeCadaIntervalo = dividirEnIntervalos(cantIntervalos)
        # print(intervalos)

        for i in intervalos:
            contadorApariciones = 0

            item = 0

            while item < len(serie):
                if serie[item] >= i[0] and serie[item] < i[1]:
                    contadorApariciones += 1

                item += 1

            frecuenciaReal.append(contadorApariciones)

        return frecuenciaEsperada, frecuenciaReal
    #def calculo_chi_Cuadrado(frecuenciaEsperada,frecuenciaReal):

    def calculo_chi_Cuadrado(self):
        #del congruencial lineal
        serieA_FE=[10, 10, 10, 10, 10, 10, 10, 10 , 10, 10 ]
        serieB_FO=[10, 13, 9, 8, 13, 8, 8, 14, 10, 7]

        diferencia1 = [e2 - e1 for e1, e2 in zip(serieA_FE, serieB_FO)]
        diferencia_1= np.subtract(serieB_FO, serieA_FE)
        #me devuelve FO-FE

        diferencia2 = np.power(diferencia1,2)
        #me devuelve (FO-FE)^2

        diferencia3 = np.divide(diferencia2,serieA_FE)
        #me devuelve (FO-FE)^2/FE

        diferencia4 = np.sum(diferencia3)
        #me devuelve el total de sum (FO-FE)^2/FE

        #diferencia5=np.comsum(difererncia3)
        #me devuelve el sum de (FO-FE)^2/FE

        return diferencia1, diferencia_1, diferencia2,diferencia3,diferencia4,#diferencia5

    def media_varianza(self):
        lista=np.array([0.0112, 0.1904, 0.2368, 0.0256, 0.4352, 0.3984, 0.7728, 0.1376, 0.3392, 0.7664, 0.0288, 0.4896, 0.3232, 0.4944, 0.4048, 0.8816, 0.9872, 0.7824, 0.3008, 0.1136, 0.9312, 0.8304, 0.1168, 0.9856, 0.7552, 0.8384, 0.2528, 0.2976, 0.0592, 0.0064, 0.1088, 0.8496, 0.4432, 0.5344, 0.0848, 0.4416, 0.5072, 0.6224, 0.5808, 0.8736, 0.8512, 0.4704, 0.9968, 0.9456, 0.0752, 0.2784, 0.7328, 0.4576, 0.7792, 0.2464, 0.1888, 0.2096, 0.5632, 0.5744, 0.7648, 0.0016, 0.0272, 0.4624, 0.8608, 0.6336, 0.7712, 0.1104, 0.8768, 0.9056, 0.3952, 0.7184, 0.2128, 0.6176, 0.4992, 0.4864, 0.2688, 0.5696, 0.6832, 0.6144, 0.4448, 0.5616, 0.5472, 0.3024, 0.1408, 0.3936, 0.6912, 0.7504, 0.7568, 0.8656, 0.7152, 0.1584, 0.6928, 0.7776, 0.2192, 0.7264, 0.3488, 0.9296, 0.8032, 0.6544, 0.1248, 0.1216, 0.0672, 0.1424, 0.4208, 0.1536])
        media= round(lista.mean(),4)
        varianza=round(lista.var(),4)
        return media, varianza

#print("")
#print ("metodo congruencial lineal")
#print(generarNrosAleatoriosMetodoCongruencialLineal())
#print("")
#print("metodo congruencial mixto")
#print(generarNrosAleatoriosMetodoCongruencialMixto())
#print("")
#print("metodo numeros aleatorios")
#print(generarNumerosAleatoriosPython())
#print("")
#print("[[intervalos] - [media]]")
#print(dividirEnIntervalos())
#print("")
#print("Test-ChiCuadrado: (frecuencia esperada  -  frecuencia observada ) del congruencial lineal")
#print(testChiCuadrado())
#print("")
#print("calculo de chi cuadrado")
#print(calculo_chi_Cuadrado())
#print("")
#print("media y varianza")
#print(media_varianza())