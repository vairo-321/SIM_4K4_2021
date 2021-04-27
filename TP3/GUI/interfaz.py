import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QTableWidgetItem
from PyQt5 import uic
from GUI.GeneracionVariablesAleatorias.generadores import controladorDistribuciones



class Generador_Numeros(QMainWindow):
    controlador=None
    numeros_aleatorios=[]
    A=None
    B=None
    media_Exp=None
    media_Norm=None
    landa_Cuason=None
    desviac_Norm=None
    def __init__(self):
        super() . __init__()

        uic.loadUi("ventanaVariablesAleatorias.ui",self)
        self.controlador=controladorDistribuciones()

        self.cmbDistribucion.currentIndexChanged.connect(self.accion_seleccionar_distribucion)
        self.btn_generar.clicked.connect(self.accion_generar_numeros)
        self.btn_limpiar.clicked.connect(self.limpiar_interfaz_generar_numeros)
        self.btn_PruebaChiCuadrado.clicked.connect(self.accion_prueba_ChiCuadrado)
        self.btn_limpiarIntervalos.clicked.connect(self.limpiar_interfaz_prueba_frecuencia)


    def filtrar(self, numeros):
        resultado = []
        for diccionario in numeros:
            resultado.append(diccionario['nro_random'])
        return resultado

    def limpiar_interfaz_prueba_frecuencia(self):
        self.txt_intervalos.clear()


    def accion_prueba_ChiCuadrado(self):
        id_metodo = self.cmbDistribucion.itemData(self.cmbDistribucion.currentIndex())

        self.numeros_aleatorios = self.filtrar(self.numeros_aleatorios)
        minimo = min(self.numeros_aleatorios)
        maximo = max(self.numeros_aleatorios)

        #media_Exp = self.txt_mediaExp.text()
        #media_Norm = self.txt_mediaNormal.text()
        #desviac_Norm = self.txt_desvNorm.text()
        #landa_Cuason = self.txt_landaCuason.text()


        if len(self.numeros_aleatorios) == 0:
            self.mostrar_mensaje("Error", "Primero debe generar los números aleatorios")
            return

        cantidad_intervalos = self.txt_intervalos.text()
        if cantidad_intervalos == "" or int(cantidad_intervalos) <= 0:
            self.mostrar_mensaje("Error", "La cantidad de intervalos tiene que ser mayor a cero")
            return

        frecuenciaEsperada, frecuenciaReal, mediaDeCadaIntervalo = self.controlador.testChiCuadrado(id_metodo,
            self.numeros_aleatorios, cantidad_intervalos,maximo,minimo,self.media_Exp,self.media_Norm,self.desviac_Norm,self.landa_Cuason)

        chi_cuadrado = self.controlador.prueba_chicuadrado(frecuenciaEsperada, frecuenciaReal)
        self.mostrar_mensaje("Valor obtenido", "El valor de Chi cuadrado obtenido es %s"
                             % str(chi_cuadrado).replace(".", ","))
        self.controlador.generar_histograma(mediaDeCadaIntervalo,frecuenciaEsperada,frecuenciaReal)

    def accion_seleccionar_distribucion(self):
        id_metodo = self.cmbDistribucion.itemData(self.cmbDistribucion.currentIndex())

        if id_metodo == 0:
            self.txt_A.setEnabled(True)
            self.txt_B.setEnabled(True)
            self.txt_mediaExp.setEnabled(False)
            self.txt_mediaNormal.setEnabled(False)
            self.txt_desvNorm.setEnabled(False)
            self.txt_landaCuason.setEnabled(False)
            self.txt_mediaExp.clear()
            self.txt_mediaNormal.clear()
            self.txt_desvNorm.clear()
            self.txt_landaCuason.clear()

        elif id_metodo==1:
            self.txt_A.setEnabled(False)
            self.txt_B.setEnabled(False)
            self.txt_mediaExp.setEnabled(True)
            self.txt_mediaNormal.setEnabled(False)
            self.txt_desvNorm.setEnabled(False)
            self.txt_landaCuason.setEnabled(False)

            self.txt_A.clear()
            self.txt_B.clear()
            self.txt_mediaNormal.clear()
            self.txt_desvNorm.clear()
            self.txt_landaCuason.clear()




        elif id_metodo==2:
            self.txt_A.setEnabled(False)
            self.txt_B.setEnabled(False)
            self.txt_mediaExp.setEnabled(False)
            self.txt_mediaNormal.setEnabled(True)
            self.txt_desvNorm.setEnabled(True)
            self.txt_landaCuason.setEnabled(False)

            self.txt_A.clear()
            self.txt_B.clear()
            self.txt_mediaExp.clear()
            self.txt_landaCuason.clear()

        elif id_metodo==3:
            self.txt_A.setEnabled(False)
            self.txt_B.setEnabled(False)
            self.txt_mediaExp.setEnabled(False)
            self.txt_mediaNormal.setEnabled(False)
            self.txt_desvNorm.setEnabled(False)
            self.txt_landaCuason.setEnabled(True)

            self.txt_A.clear()
            self.txt_B.clear()
            self.txt_mediaExp.clear()
            self.txt_mediaNormal.clear()
            self.txt_desvNorm.clear()

    def accion_generar_numeros(self):
        id_metodo = self.cmbDistribucion.itemData(self.cmbDistribucion.currentIndex())
        A=None
        B=None
        media_Exp = None
        desviac_Norm = None
        landa_Cuason = None
        media_Norm=None
        if id_metodo ==0:
            A = self.txt_A.text()
            if A == "":
                self.mostrar_mensaje("Error", "La constante \"A\" no puede ser vacía")
                return
            B= self.txt_B.text()
            if B == "":
                self.mostrar_mensaje("Error", "La constante \"B\" no puede ser vacía")
                return
        elif id_metodo == 1:
            media_Exp = self.txt_mediaExp.text()
            if media_Exp == "":
                self.mostrar_mensaje("Error", "La constante \"mu\" no puede ser vacía")
                return
        elif id_metodo == 2:
            media_Norm = self.txt_mediaNormal.text()
            if media_Norm == "":
                self.mostrar_mensaje("Error", "La constante \"mu\" no puede ser vacía")
                return
            desviac_Norm = self.txt_desvNorm.text()
            if desviac_Norm == "" or float(desviac_Norm.replace(",", ".")) < 0:
                self.mostrar_mensaje("Error", "La constante \"sigma\" tiene que ser mayor o igual a cero")
                return
        elif id_metodo == 3:
            landa_Cuason = self.txt_landaCuason.text()
            if landa_Cuason == "" or float(landa_Cuason.replace(",", ".")) <= 0:
                self.mostrar_mensaje("Error", "La constante \"lambda\" tiene que ser mayor a cero")
                return
        self.A = A
        self.B = B
        self.media_Exp = media_Exp
        self.media_Norm = media_Norm
        self.desviac_Norm = desviac_Norm
        self.landa_Cuason = landa_Cuason

        cantidad_numeros = self.txt_cantNumeros.text()
        if cantidad_numeros == "" or int(cantidad_numeros) <= 0:
            self.mostrar_mensaje("Error", "La cantidad de números tiene que ser mayor a cero")
            return


        if id_metodo == 0:
            self.numeros_aleatorios = self.controlador.generarDistribucionUniforme(cantidad_numeros,A,B)
        elif id_metodo == 1:
            self.numeros_aleatorios = self.controlador.generarDistribucionExponencial(cantidad_numeros,media_Exp)
        elif id_metodo == 2:
            self.numeros_aleatorios = self.controlador.generarDistribucionNormal(cantidad_numeros,media_Norm,desviac_Norm)
        elif id_metodo == 3:
            self.numeros_aleatorios = self.controlador.generarDistribucionCuasson(cantidad_numeros,landa_Cuason)

        self.cargar_tabla_numeros_aleatorios()

    def cargar_tabla_numeros_aleatorios(self):
        self.dgv_VariablesAleatorias.setRowCount(len(self.numeros_aleatorios))
        index = 0
        for n in self.numeros_aleatorios:
            # Obtengo datos en formato conveniente
            nro_orden = str(n.get("nro_orden"))
            nro_random = str(n.get("nro_random")).replace(".", ",")
            # Agrego fila a tabla
            self.dgv_VariablesAleatorias.setItem(index, 0, QTableWidgetItem(nro_orden))
            self.dgv_VariablesAleatorias.setItem(index, 1, QTableWidgetItem(nro_random))
            index += 1


    def mostrar_mensaje(self, titulo, mensaje):
        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def preparar_interfaz(self):
        # Cargo combo box
        self.cmbDistribucion.clear()
        self.cmbDistribucion.addItem("Distribución Uniforme", 0)
        self.cmbDistribucion.addItem("Distribución exponencial", 1)
        self.cmbDistribucion.addItem("Distribución normal ", 2)
        self.cmbDistribucion.addItem("Distribucion cuasson", 3)

        # Preparo tabla de numeros generados
        self.dgv_VariablesAleatorias.setColumnCount(2)
        self.dgv_VariablesAleatorias.setHorizontalHeaderLabels(["N° de orden","Número aleatorio"])
    def limpiar_interfaz_generar_numeros(self):
        # Limpio txts
        self.txt_A.clear()
        self.txt_B.clear()
        self.txt_cantNumeros.clear()
        self.txt_mediaExp.clear()

        # Selecciono opcion por defecto en combo boxs
        self.cmbDistribucion.setCurrentIndex(0)

        # Limpio grilla
        self.dgv_VariablesAleatorias.clearSelection()
        self.dgv_VariablesAleatorias.setCurrentCell(-1, -1)
        self.dgv_VariablesAleatorias.setRowCount(0)
        self.numeros_aleatorios = []

    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_interfaz_generar_numeros()



def main():
    app= QApplication(sys.argv)
    GUI= Generador_Numeros()
    GUI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
