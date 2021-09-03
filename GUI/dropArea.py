from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

HUMAN = False
COMPUTER = True

class dropArea(QGraphicsItem):

    def __init__(self, area: QRectF, column: int, parent=None):
        super().__init__(parent)

        self.area = area
        self.column = column
        self.pressed = False
        self.acceptPress = True
        self.hovered = False
        self.setAcceptHoverEvents(True)


    def boundingRect(self) -> QRectF:
        return self.area


    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget=None):
        hoverPen = QPen(QColor("#000000"), 2)

        redPen = QPen(QColor("#ff0004"))
        redBrush = QBrush(QColor("#ff0004"), Qt.BrushStyle.SolidPattern)
        
        if self.hovered:
           painter.setPen(hoverPen)
           painter.drawRect(self.area)

        if self.pressed: 
           column = self.column
           scene = self.scene()
           checkers = scene.checkers[0:8]
           checkersColumn = checkers[column]
           filled = scene.filledCheckers

           for row in range(7, -1, -1):
               if filled[row][column] == 0:
                 scene.filledCheckers[row][column] = 1
                 scene.addEllipse(checkersColumn[row], redPen, redBrush)
                 break
        
           scene.game.take_turns()
           self.pressed = False


    def paintComputer(self):
        yellowPen = QPen(QColor("#f5ec42"))
        yellowBrush = QBrush(QColor("#f5ec42"), Qt.BrushStyle.SolidPattern)

        if not self.acceptPress and not self.acceptHoverEvents():
           column = self.column
           scene = self.scene()
           checkers = scene.checkers[0:8]
           checkersColumn = checkers[column]
           filled = scene.filledCheckers

           for row in range(7, -1, -1):
               if filled[row][column] == 0:
                  scene.filledCheckers[row][column] = 2
                  scene.addEllipse(checkersColumn[row], yellowPen, yellowBrush)
                  break
        
           scene.game.take_turns()


    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.hovered = True
        self.update()

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.hovered = False
        self.update()

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.acceptPress:
          self.pressed = True  
          self.update()

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.acceptPress:
          self.pressed = False  
          self.update()
        
    def agentEvent(self):
        self.paintComputer()
        
