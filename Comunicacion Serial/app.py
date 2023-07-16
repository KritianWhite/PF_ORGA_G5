import serial
import time
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

arduino = serial.Serial('COM8', 9600)
time.sleep(2)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('C:/Users/Taro/Documents/Cursos_2023/Vacaciones_junio/Orga/PF_ORGA_G5/Comunicacion Serial/interfaz.ui', self)
        self.setWindowTitle('Control de Luces')
        self.pushButton_3.clicked.connect(self.ConversionNumeroBinarioDecimal)


        
    def on(self):
        arduino.write(b'1')  

        
    def off(self):
        arduino.write(b'0')  

    def ConversionNumeroBinarioDecimal(self):
        numero = self.lineEdit.text()
        numero = int(numero, 2)
        print(numero)
        arduino.write(b'\n')
        arduino.write(b'Puntaje final del jugador: ') 
        arduino.write(b'\n')
        arduino.write(str(numero).encode())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())        
