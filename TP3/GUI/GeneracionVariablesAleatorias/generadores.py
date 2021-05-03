import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class controladorDistribuciones():

    def generarDistribucionUniforme(self,cantidad,A,B):
        numeros_generados = []
        A=float(A.replace(",", "."))
        B=float(B.replace(",", "."))
        cantidad=int(cantidad)
        # Genero lista de numeros aleatorios
        for i in range(0, cantidad):
            X =round(A + (random.random() * (B-A)),4)
            numeros_generados.append({
                "nro_orden": i + 1,
                "nro_random": X
            })

        return numeros_generados


    def generarDistribucionExponencial(self,cantidad,media):
        numeros_generados = []
        media = float(media.replace(",", "."))
        #landa=float(landa)
        cantidad = int(cantidad)
        # Genero lista de numeros aleatorios
        for i in range(0, cantidad):
            X = round(-media* math.log(1 - random.random()), 4)
            #X = round(-1/landa * math.log(1 - random.random()), 4)
            numeros_generados.append({
                "nro_orden": i + 1,
                "nro_random": X
            })

        return numeros_generados


    def generarDistribucionNormal(self,cantidad,media,desviacion):
        numeros_generados = []
        media = float(media.replace(",", "."))
        desviacion=float(desviacion.replace(",", "."))
        cantidad = int(cantidad)
        # Genero lista de numeros aleatorios
        for i in range(0, cantidad):
            Z=round((((random.random()+random.random()+random.random()+random.random()+
               random.random()+random.random()+random.random()+random.random()+
              random.random()+random.random()+random.random()+random.random())-6) *desviacion) + media ,2)

            numeros_generados.append({
                "nro_orden": i + 1,
                "nro_random": Z
            })
        return numeros_generados

    def generarDistribucionCuasson(self,cantidad,media):
        numeros_generados = []
        media=float(media.replace(",", "."))
        cantidad = int(cantidad)
        # Genero lista de numeros aleatorios
        for i in range(0, cantidad):
            p=1
            x=-1
            a=math.exp(-media)
            u=random.random()
            p= p * u
            while p >=a:
                u=random.random()
                p= p* u
                x= x+ 1
            numeros_generados.append({
                "nro_orden": i + 1,
                "nro_random":x
            })
        return numeros_generados

    def dividirEnIntervalos(self,cantIntervalos,maximo, minimo):
        paso = (maximo - minimo) / cantIntervalos
        intervalos = []
        mediaDeCadaIntervalo = []
        i = 0
        while i < cantIntervalos:
            if i == 0:
                intervalos.append([round(minimo, 4), round(minimo + paso, 4 )])
            else:
                minimoAnterior = round(intervalos[i - 1][1], 4)
                intervalos.append([minimoAnterior, round(minimoAnterior + paso, 4)])

            i += 1

        for i in intervalos:
            mediaDeCadaIntervalo.append(round((i[0] + i[1]) / 2, 4))

        return intervalos, mediaDeCadaIntervalo

    # funcion de esteban para calcular Fo
    '''
    def calcular_frecuencia_observada(self, cantidadIntervalos, serie ):
        print("despues de entrar")
        frecuenciaTotal = []

        ancho = ( max(serie) - min(serie) ) / cantidadIntervalos

        frecuenciaxIntervalo = 0
        i = 0
        limiteInferior = min(serie)
        while i < cantidadIntervalos:
            j = 0
            while j < len(serie):
                if serie[j] >= limiteInferior and serie[j] < (limiteInferior + ancho):
                    frecuenciaxIntervalo += 1
                j += 1

            frecuenciaTotal.append(frecuenciaxIntervalo)

            i += 1
            limiteInferior = limiteInferior + ancho
            frecuenciaxIntervalo = 0


        return frecuenciaTotal
    '''


    def testChiCuadrado(self,id,serie,cantIntervalos,maximo,minimo,media_Exp=None,
                        media_Norm=None,desviac_Norm=None,landa_Cuason=None):
        maximo=int(maximo)
        minimo=int(minimo)
        id=int(id)

        if media_Exp is not None:
            media_Exp = float(media_Exp.replace(",", "."))
            if media_Exp == int(media_Exp):
                media_Exp = int(media_Exp)
        if media_Norm is not None:
            media_Norm = float(media_Norm.replace(",", "."))
            if media_Norm == int(media_Norm):
                media_Norm = int(media_Norm)
        if desviac_Norm is not None:
            desviac_Norm = float(desviac_Norm.replace(",", "."))
            if desviac_Norm == int(desviac_Norm):
                desviac_Norm = int(desviac_Norm)
        if landa_Cuason is not None:
            landa_Cuason= float(landa_Cuason.replace(",", "."))
            if landa_Cuason == int(landa_Cuason):
                landa_Cuason = int(landa_Cuason)

        cantIntervalos = int(cantIntervalos)

        frecuenciaReal = []
        frecuencias_esperadas=[]

        intervalos, mediaDeCadaIntervalo = self.dividirEnIntervalos(cantIntervalos,maximo,minimo)

        '''
        como contaba frecuencia Herni
        for i in intervalos:
            contadorApariciones = 0

            item = 0

            while item < len(serie):
                if serie[item] >= i[0] and serie[item] < i[1]:
                    contadorApariciones += 1

                item += 1

            frecuenciaReal.append(contadorApariciones)
        
        '''

        #-----------------------------------------------------------------------------------------------------
        #Nueva forma de contar frecuencia
        ancho = ( max(serie) - min(serie) ) / cantIntervalos
        frecuenciaxIntervalo = 0
        i = 0
        limiteInferior = min(serie)
        while i < cantIntervalos:
            j = 0
            while j < len(serie):
                if serie[j] >= limiteInferior and serie[j] < (limiteInferior + ancho):
                    frecuenciaxIntervalo += 1
                j += 1

            frecuenciaReal.append(frecuenciaxIntervalo)

            i += 1
            limiteInferior = limiteInferior + ancho
            frecuenciaxIntervalo = 0

        #---------------------------------------------------------------------------------------------

        if id==0:
            frecuencias_esperadas = [len(serie) / cantIntervalos] * cantIntervalos


        else:
            for i in intervalos:
                frecuencia_esperada = 0
                maximo=i[1]
                minimo=i[0]

                if id==1:
                    frecuencia_esperada = round((stats.expon(0, media_Exp).cdf(maximo) -
                                                         stats.expon(0, media_Exp).cdf(minimo)) *
                                                        len(serie), 4)
                elif id==2:
                    frecuencia_esperada = round((stats.norm(media_Norm, desviac_Norm).cdf(maximo) -
                                                         stats.norm(media_Norm, desviac_Norm).cdf(minimo)) *
                                                        len(serie), 4)
                elif id==3:
                    frecuencia_esperada = round((stats.poisson(landa_Cuason).cdf(maximo) -
                                                         stats.poisson(landa_Cuason).cdf(minimo)) *
                                                        len(serie), 4)

                if frecuencia_esperada == int(frecuencia_esperada):
                    frecuencia_esperada = int(frecuencia_esperada)
                frecuencias_esperadas.append(frecuencia_esperada)

        return frecuencias_esperadas, frecuenciaReal, mediaDeCadaIntervalo

    def prueba_chicuadrado(self, frecuencias_observadas, frecuencias_esperadas):

        '''
        Lo de abajo era una solucion alternativa, ya que creia que el problema estaban en las lineas antes establecidas

        c_acumulado = 0

        i = 0

        while i < len(frecuencias_observadas):
            c = (pow(frecuencias_esperadas[i] - frecuencias_observadas[i], 2)) / frecuencias_esperadas[i]

            c_acumulado = c_acumulado + c

            i += 1


        '''

        diferencia1 = np.subtract(frecuencias_observadas, frecuencias_esperadas)
        # me devuelve FO-FE

        diferencia2 = np.power(diferencia1, 2)
        # me devuelve (FO-FE)^2

        diferencia3 = np.divide(diferencia2, frecuencias_esperadas)
        # me devuelve (FO-FE)^2/FE

        chi_cuadrado = round(np.sum(diferencia3),4)
        # me devuelve el total de sum (FO-FE)^2/FE

        total = np.sum(frecuencias_observadas)  # <--- Esta linea fue creada para controlar que se cuenten el total de las frecuencias observadas

        return chi_cuadrado


       # return c_acumulado




    def generar_histograma(self,mediaDeCadaIntervalo,frecuenciasEsperadas,frecuenciasObserbadas):

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



    def calcular_frecuencia_observada(self, cantidadIntervalos, serie ):
        frecuenciaTotal = []

        ancho = ( max(serie) - min(serie) ) / cantidadIntervalos

        frecuenciaxIntervalo = 0
        i = 0
        limiteInferior = min(serie)
        while i < cantidadIntervalos:
            j = 0
            while j in serie:
                if serie[j] >= limiteInferior and serie[j] < (limiteInferior + ancho):
                    frecuenciaxIntervalo += 1
                j += 1

            frecuenciaTotal.append(frecuenciaxIntervalo)

        limiteInferior = limiteInferior + ancho
        frecuenciaxIntervalo = 0
        i += 1


        return frecuenciaTotal





