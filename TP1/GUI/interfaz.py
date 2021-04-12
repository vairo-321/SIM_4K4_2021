import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from GUI.GeneracionNroRandom.generadores import controlGeneradores
from random import *


class Generador_Numeros(QMainWindow):
    controlador = None
    numeros_aleatorios = []
    semilla=None
    a=None
    c=None
    m=None
    aleatorio=[]
    frecuenciaEsperada=[]
    frecuenciaReal=[]

    def __init__(self):
        super() . __init__()

        uic.loadUi("ventanaGenerarNumeros.ui",self)
        self.controlador = controlGeneradores()


        self.cmb_MetodoAleatorio.currentIndexChanged.connect(self.accion_seleccionar_metodo)
        self.btn_limpiar.clicked.connect(self.limpiar_interfaz_generar_numeros)
        self.btn_generarNumeros.clicked.connect(self.accion_generar_numeros)
        self.btn_proxNumero.clicked.connect(self.accion_generar_proximo_numero)
        self.btn_limpiarIntervalos.clicked.connect(self.limpiar_interfaz_prueba_frecuencia)
        self.btn_PruebaChiCuadrado.clicked.connect(self.accion_prueba_ChiCuadrado)

    def filtrar(self, numeros):
        resultado = []
        for diccionario in numeros:
            resultado.append(diccionario['aleatorio_decimal'])
        return resultado

    def accion_prueba_ChiCuadrado(self):
        self.aleatorio=self.filtrar(self.numeros_aleatorios)
        if len(self.numeros_aleatorios) == 0:
            self.mostrar_mensaje("Error", "Primero debe generar los números aleatorios")
            return

        cantidad_intervalos = self.txt_intervalos.text()
        if cantidad_intervalos == "" or int(cantidad_intervalos) <= 0:
            self.mostrar_mensaje("Error", "La cantidad de intervalos tiene que ser mayor a cero")
            return

        frecuenciaEsperada, frecuenciaReal,mediaDeCadaIntervalo = self.controlador.testChiCuadrado(self.aleatorio, cantidad_intervalos)

        chi_cuadrado = self.controlador.prueba_chicuadrado(frecuenciaEsperada, frecuenciaReal)
        self.mostrar_mensaje("Valor obtenido", "El valor de Chi cuadrado obtenido es %s"
                            % str(chi_cuadrado).replace(".", ","))
        self.controlador.generar_grafico(mediaDeCadaIntervalo,frecuenciaEsperada,frecuenciaReal)

    def limpiar_interfaz_prueba_frecuencia(self):
        self.txt_intervalos.clear()


    def accion_generar_proximo_numero(self):
        return 0


    def accion_seleccionar_metodo(self):

        # Activo o desactivo input de constante c dependiendo del metodo elegido
        id_metodo = self.cmb_MetodoAleatorio.itemData(self.cmb_MetodoAleatorio.currentIndex())
        if id_metodo == 0:
            self.txt_semilla.setEnabled(True)
            self.txt_cte_a.setEnabled(True)
            self.txt_cte_c.setEnabled(True)
            self.txt_cte_m.setEnabled(True)
        elif id_metodo == 1:
            self.txt_semilla.setEnabled(True)
            self.txt_cte_a.setEnabled(True)
            self.txt_cte_c.clear()
            self.txt_cte_c.setEnabled(False)
            self.txt_cte_m.setEnabled(True)
        else:
            self.txt_semilla.clear()
            self.txt_semilla.setEnabled(False)
            self.txt_cte_a.clear()
            self.txt_cte_a.setEnabled(False)
            self.txt_cte_c.clear()
            self.txt_cte_c.setEnabled(False)
            self.txt_cte_m.clear()
            self.txt_cte_m.setEnabled(False)

    def validar_txt(self):
        return 0

    def accion_generar_numeros(self):

        # Obtengo metodo
        id_metodo = self.cmb_MetodoAleatorio.itemData(self.cmb_MetodoAleatorio.currentIndex())
        semilla = None
        a = None
        c = None
        m = None

        if id_metodo == 0 or id_metodo == 1:
            semilla = self.txt_semilla.text()
            if semilla == "" or float(semilla.replace(",", ".")) < 0:
                self.mostrar_mensaje("Error", "La semilla tiene que ser mayor o igual a cero")
                return
            a = self.txt_cte_a.text()
            if a == "" or float(a.replace(",", ".")) <= 0:
                self.mostrar_mensaje("Error", "La constante \"a\" tiene que ser mayor a cero")
                return
        if id_metodo == 0:
            c = self.txt_cte_c.text()
            if c == "" or float(c.replace(",", ".")) <= 0:
                self.mostrar_mensaje("Error", "La constante \"c\" tiene que ser mayor a cero")
                return
        if id_metodo == 0 or id_metodo == 1:
            m = self.txt_cte_m.text()
            if m == "" or float(m.replace(",", ".")) <= 0:
                self.mostrar_mensaje("Error", "La constante \"m\" tiene que ser mayor a cero")
                return
            if float(semilla.replace(",", ".")) >= float(m.replace(",", ".")):
                self.mostrar_mensaje("Error", "La semilla tiene que ser menor a la constante \"m\"")
                return
            if float(a.replace(",", ".")) >= float(m.replace(",", ".")):
                self.mostrar_mensaje("Error", "La constante \"a\" tiene que ser menor a la constante \"m\"")
                return
            if id_metodo == 0:
                if float(c.replace(",", ".")) >= float(m.replace(",", ".")):
                    self.mostrar_mensaje("Error", "La constante \"c\" tiene que ser menor a la constante \"m\"")
                    return

        cantidad_numeros = self.txt_cantNumeros.text()
        if cantidad_numeros == "" or int(cantidad_numeros) <= 0:
            self.mostrar_mensaje("Error", "La cantidad de números tiene que ser mayor a cero")
            return
        # Genero numeros aleatorios dependiendo del metodo seleccionado
        if id_metodo == 0:
            self.numeros_aleatorios = self.controlador.generarNrosAleatoriosMetodoCongruencialMixto(
                cantidad_numeros, semilla, a, c, m)
        elif id_metodo == 1:
            self.numeros_aleatorios = self.controlador.generarNrosAleatoriosMetodoCongruencialLineal(
                cantidad_numeros, semilla, a, m)
        elif id_metodo == 2:
            self.numeros_aleatorios = self.controlador.generarMetodoProvistoPorElLenguaje(cantidad_numeros)

        # Cargo tabla
        self.cargar_tabla_numeros_aleatorios()

    def cargar_tabla_numeros_aleatorios(self):
        self.dgv_numerosAleatorios.setRowCount(len(self.numeros_aleatorios))
        index = 0
        for n in self.numeros_aleatorios:

            # Obtengo datos en formato conveniente
            nro_orden = str(n.get("nro_orden"))
            semilla = n.get("semilla")
            if semilla is not None:
                if int(semilla) == semilla:
                    semilla = int(semilla)
                semilla = str(semilla).replace(".", ",")
            else:
                semilla = ""
            aleatorio_decimal = str(n.get("aleatorio_decimal")).replace(".", ",")
            # Agrego fila a tabla
            self.dgv_numerosAleatorios.setItem(index, 0, QTableWidgetItem(nro_orden))
            self.dgv_numerosAleatorios.setItem(index, 1, QTableWidgetItem(semilla))
            self.dgv_numerosAleatorios.setItem(index, 2, QTableWidgetItem(aleatorio_decimal))
            index += 1



    def preparar_interfaz(self):
        # Cargo combo box
        self.cmb_MetodoAleatorio.clear()
        self.cmb_MetodoAleatorio.addItem("Método congruencial mixto", 0)
        self.cmb_MetodoAleatorio.addItem("Método congruencial multiplicativo", 1)
        self.cmb_MetodoAleatorio.addItem("Método provisto por el lenguaje", 2)

       # Preparo tabla de numeros generados
        self.dgv_numerosAleatorios.setColumnCount(3)
        self.dgv_numerosAleatorios.setHorizontalHeaderLabels(["N° de orden", "Semilla", "Número aleatorio"])

    def limpiar_interfaz_generar_numeros(self):
        # Limpio txts
        self.txt_semilla.clear()
        self.txt_cte_a.clear()
        self.txt_cte_c.clear()
        self.txt_cte_m.clear()
        self.txt_cantNumeros.clear()

        # Selecciono opcion por defecto en combo boxs
        self.cmb_MetodoAleatorio.setCurrentIndex(0)

        # Limpio grilla
        self.dgv_numerosAleatorios.clearSelection()
        self.dgv_numerosAleatorios.setCurrentCell(-1, -1)
        self.dgv_numerosAleatorios.setRowCount(0)
        self.numeros_aleatorios = []

    def mostrar_mensaje(self, titulo, mensaje):
        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_interfaz_generar_numeros()
        self.limpiar_interfaz_prueba_frecuencia()

def main():
    app= QApplication(sys.argv)
    GUI= Generador_Numeros()
    GUI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
