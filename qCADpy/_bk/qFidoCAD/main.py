from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
from MainWindow import Ui_MainWindow
import sys
from  SchView import *
from Primitive import *

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("...")
        scene = QtWidgets.QGraphicsScene(self)
        scene.setSceneRect(0,0, 5000, 5000)

        rect_item = RectItem(QtCore.QRectF(0, 0, 100, 100))

        scene.addItem(rect_item)

        self.ui.schematicsViewer.setScene(scene)




def main():

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
