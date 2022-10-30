from enum import Enum
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush


class GridType(Enum):
    GT_Square   = 0
    GT_Cross    = 1
    GT_Dot      = 2

class GridBuilder:

    @staticmethod
    def drawGrid(self ,size, type):
        pixmap = QPixmap(size, size)

        pixmapWidth = pixmap.width() - 1
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        pen = QPen(Qt.gray, 1)
        painter.setPen(pen)

        if type == GridType.GT_Square:
            painter.drawLine(0, 0, pixmapWidth, 0)
            painter.drawLine(0, 0, 0, pixmapWidth)

        elif type == GridType.GT_Cross:
            painter.drawLine(0, 0, 2, 0)
            painter.drawLine(0, 0, 0, 2)
            painter.drawLine(0, pixmapWidth - 1, 0, pixmapWidth)
            painter.drawLine(pixmapWidth - 1, 0, pixmapWidth, 0)

        elif type == GridType.GT_Dot:
            painter.drawPoint(pixmapWidth,pixmapWidth)

        brush = QBrush(pixmap)
        del painter, pen, pixmap
        return brush
