

import sys 

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit
from PyQt5 import QtWidgets, QtGui 
 
class MyApp(QtWidgets.QWidget):  
     
    def __init__(self):
        super().__init__() 
        self.initUI() 
        self.resize(400, 600) 
 
    def initUI(self):   
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Название товара', 'Количество'])
        vbox = QVBoxLayout() 
        vbox.addWidget(self.table) 
        self.setLayout(vbox)         
        self.show() 

class MainMenu(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle('СкладХАБ') 
        self.resize(400, 600) 
        grid = QGridLayout() 
        self.setLayout(grid) 
        btn1 = QPushButton('Приемка', self) 
        btn2 = QPushButton('Отгрузка', self) 
        btn3 = QPushButton('Инвентаризация', self) 
        grid.addWidget(btn1, 0, 0) 
        grid.addWidget(btn2, 1, 0) 
        grid.addWidget(btn3, 2, 0) 
        btn1.clicked.connect(self.openReceptionWindow)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Название товара', 'Количество'])
        grid.addWidget(self.table, 0, 1, 3, 1) 

    def openReceptionWindow(self):
        receptionWindow = QWidget()
        receptionWindow.setWindowTitle('Окно приемки')
        receptionWindow.resize(400, 150)
        grid = QGridLayout()
        receptionWindow.setLayout(grid)

        # Создаем поля ввода для данных
        name = QLineEdit()
        name_label = QLabel('Название товара:')
        quantity = QLineEdit()
        quantity_label = QLabel('Количество:')

        # Создаем кнопку "Добавить"
        add_btn = QPushButton('Добавить')

        # Добавляем поля ввода и кнопку на форму
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(name, 0, 1)
        grid.addWidget(quantity_label, 1, 0)
        grid.addWidget(quantity, 1, 1)
        grid.addWidget(add_btn, 2, 0)

        # Функция для добавления данных в таблицу
        def addData():
            # Получаем данные из полей ввода
            name_text = name.text()
            quantity_text = quantity.text()
            # Добавляем данные в таблицу
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(name_text))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(quantity_text))
            # Очищаем поля ввода
            name.clear()
            quantity.clear()
  
        add_btn.clicked.connect(addData) # Подключаем функцию для клика на кнопке "Добавить"
        receptionWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    menu = MainMenu() 
    menu.show() 
    sys.exit(app.exec_())
