import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class controladorDistribuciones():

    def generarDistribucionUniforme(self,cantidad,A,B):
        numeros_generados = []
        A=float(A)
        B=float(B)
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
        media = float(media)
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
        media = float(media)
        desviacion=float(desviacion)
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
        media=int(media)
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

    def testChiCuadrado(self,id,serie,cantIntervalos,maximo,minimo,media_Exp,
                        media_Norm,desviac_Norm,landa_Cuason):
        maximo=int(maximo)
        minimo=int(minimo)
        id=int(id)
        serie1 = len(serie)
        #media_Exp=int(media_Exp)
        #media_Norm=int(media_Norm)
        #desviac_Norm=int(media_Norm)


        cantIntervalos = int(cantIntervalos)

        frecuenciaReal = []

        intervalos, mediaDeCadaIntervalo = self.dividirEnIntervalos(cantIntervalos,maximo,minimo)
        # print(intervalos)

        for i in intervalos:
            contadorApariciones = 0

            item = 0

            while item < len(serie):
                if serie[item] >= i[0] and serie[item] < i[1]:
                    contadorApariciones += 1

                item += 1

            frecuenciaReal.append(contadorApariciones)

        frecuenciaEsperada=[]
    #https://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/
        if id == 0:
            frecuenciaEsperada = [len(serie) / cantIntervalos] * cantIntervalos

        elif id == 1:
            #frecuenciaEsperada = round((stats.expon(0,media_Exp).cdf(maximo) - stats.expon(0,media_Exp).cdf(minimo))* serie1, 2)
           frecuenciaEsperada = [len(serie) / cantIntervalos] * cantIntervalos

        elif id == 2:
            #frecuenciaEsperada = round((stats.norm(media_Norm, desviac_Norm).cdf(maximo) - stats.norm(media_Norm, desviac_Norm).cdf(minimo)) * serie1, 2)
            frecuenciaEsperada = [len(serie) / cantIntervalos] * cantIntervalos

        elif id == 3:
            #frecuenciaEsperada = round((stats.poisson(landa_Cuason).cdf(maximo) - stats.poisson(landa_Cuason).cdf(minimo)) * serie1, 2)
            frecuenciaEsperada = [len(serie) / cantIntervalos] * cantIntervalos


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







    def generarGraficosDeDistribucionDeProbabilidad(self,id_metodo,numeros_aleatorios,minimo,maximo,media_Exp=None,media_Norm=None,desviac_Norm=None,landa_Cuason=None):
        id=int(id_metodo)
        maximo=int(maximo)
        minimo=int(minimo)
        cantidadVariables=len(numeros_aleatorios)

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
            landa_Cuason = float(landa_Cuason.replace(",", "."))
            if landa_Cuason == int(landa_Cuason):
                landa_Cuason = int(landa_Cuason)

        if id==0:
            uniforme = stats.uniform()
            x = np.linspace(uniforme.ppf(minimo),
                            uniforme.ppf(maximo), cantidadVariables)
            fp = uniforme.pdf(x)  # Función de Probabilidad
            fig, ax = plt.subplots()
            ax.plot(x, fp, '--')
            ax.vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)
            plt.title('Distribución Uniforme')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

        elif id==1:
            exponencial = stats.expon(media_Exp)
            x = np.linspace(exponencial.ppf(minimo),
                            exponencial.ppf(maximo), cantidadVariables)
            fp = exponencial.pdf(x)  # Función de Probabilidad
            plt.plot(x, fp)
            plt.title('Distribución Exponencial')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

        elif id==2:
            mu, sigma = media_Norm,desviac_Norm  # media y desvio estandar
            normal = stats.norm(mu,sigma)
            x = np.linspace(normal.ppf(minimo),
                            normal.ppf(maximo), cantidadVariables)
            fp = normal.ppf(x)  # Función de Probabilidad
            plt.plot(x, fp)
            plt.title('Distribución Normal')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

        elif id==3:
            mu = landa_Cuason # parametro de forma
            poisson = stats.poisson(mu)  # Distribución
            x = np.arange(poisson.ppf(minimo),
                          poisson.ppf(maximo),cantidadVariables)
            fmp = poisson.pmf(x)  # Función de Masa de Probabilidad
            plt.plot(x, fmp, '--')
            plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
            plt.title('Distribución Poisson')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

