from PyQt5 import QtWidgets, QtCore, QtGui
from GridBuilder import *


class SchView(QtWidgets.QGraphicsView):

    def __init__(self, parent):
        super(SchView, self).__init__(parent)

        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setBackgroundBrush(GridBuilder.drawGrid(20, 20, GridType.GT_Dot))

