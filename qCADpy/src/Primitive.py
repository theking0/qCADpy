from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush

class RectItem(QtWidgets.QGraphicsRectItem):
    def __init__(self, rect):
        QtWidgets.QGraphicsRectItem.__init__(self, QRectF(rect))
        self.setFlag(QtWidgets.QGraphicsRectItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsRectItem.ItemIsSelectable, True)

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):
        block_size = 20
        x = round(event.scenePos().x()/block_size)*block_size
        y = round(event.scenePos().y()/block_size)*block_size
        pos = QPointF(x, y)
        self.setPos(pos)