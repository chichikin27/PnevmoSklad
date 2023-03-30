import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('СкладХАБ')

                # установка размеров окна
        self.resize(400, 600)

        # Создаем сетку для размещения кнопок
        grid = QGridLayout()
        self.setLayout(grid)


        # Создаем кнопки для Приемки и Отгрузки
        btn1 = QPushButton('Приемка', self)
        btn2 = QPushButton('Отгрузка', self)
        btn3 = QPushButton('Инвентаризация', self)

        # Добавляем кнопки в сетку
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 1, 0)
        grid.addWidget(btn3, 2, 0)

app = QApplication(sys.argv)
menu = MainMenu()
menu.show()
sys.exit(app.exec_())