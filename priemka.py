from PyQt5 import QtWidgets, QtGui 
import sys 
 
class MyApp(QtWidgets.QWidget):  # добавляем префикс QtWidgets 
    def __init__(self): 
        super().__init__() 
        self.initUI() 
        self.resize(400, 600) 
 
    def initUI(self):   
        # Создаем виджеты   
        self.label_name = QtWidgets.QLabel('Название:') 
        self.edit_name = QtWidgets.QLineEdit() 
        self.label_value = QtWidgets.QLabel('Количество:') 
        self.edit_value = QtWidgets.QLineEdit() 
        self.button = QtWidgets.QPushButton('Добавить') 
 
        font = QtGui.QFont() 
        font.setPointSize(20)  # выбираем размер шрифта 
        self.label_name.setFont(font)  # устанавливаем шрифт для label_name 
        font.setPointSize(15)  # выбираем размер шрифта 
        self.label_value.setFont(font) 
        self.button.setFont(font) 
 
        # Создаем словарь для хранения данных 
        self.data = {} 
 
        # Создаем компоновщик 
        vbox = QtWidgets.QVBoxLayout() 
        vbox.addWidget(self.label_name) 
        vbox.addWidget(self.edit_name) 
        vbox.addWidget(self.label_value) 
        vbox.addWidget(self.edit_value) 
        vbox.addWidget(self.button) 
 
        # Устанавливаем компоновку для окна 
        self.setLayout(vbox) 
 
        # Подключаем обработчик нажатия на кнопку 
        self.button.clicked.connect(self.add_data) 
 
        # Показываем окно 
        self.show() 
 
    def add_data(self): 
        # Получаем данные из полей ввода 
        name = self.edit_name.text() 
        value = self.edit_value.text() 
        self.edit_name.clear()
        self.edit_value.clear()
        # Добавляем данные в словарь 
        self.data[name] = int(value) 
 
        # Выводим словарь на консоль для проверки 
        print(self.data) 
 
if __name__ == '__main__':   # исправляем ошибку в проверке имени модуля
    app = QtWidgets.QApplication(sys.argv) 
    ex = MyApp() 
    sys.exit(app.exec_())