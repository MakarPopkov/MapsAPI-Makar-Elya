from PyQt5.QtWidgets import QApplication, QWidget, QAction, QDialog, QLineEdit
from PyQt5.QtCore import Qt
import sys
from io import BytesIO
from PIL import Image

from design import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Yandex Maps 2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())