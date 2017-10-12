import sys
from aaa import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from DBService import DBService


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    lst = [1,3,5,7]
    window.listWidget.addItems(lst)
    
    window.show()

sys.exit(app.exec_())
