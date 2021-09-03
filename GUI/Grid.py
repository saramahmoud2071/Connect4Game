from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np

from dropArea import dropArea


class Grid(QGraphicsScene):

    def __init__(self, game: QMainWindow, parent=None):
        super().__init__(parent)

        """ Grid measures """
        self.row = 8
        self.col = 8
        self.checkerSize = 48

        self.margin = 10
        self.xOffset = 8
        self.yOffset = 5

        """ Game playing """
        self.game = game

        self.dropAreas = []
        self.checkers = []  
        self.filledCheckers = np.zeros((self.col,self.row), dtype=int)
        
        self.setBackgroundBrush(QColor("#346eeb"))


    def drawBackground(self, painter: QPainter, rect: QRectF):
       super().drawBackground(painter, rect)

       top = int(rect.top())
       bottom = int(rect.bottom())
       left = int(rect.left())
       right = int(rect.right())

       Pen = QPen(QColor("#FFFFFF"))
       Brush = QBrush(QColor("#FFFFFF"), Qt.BrushStyle.SolidPattern)
       painter.setPen(Pen)
       painter.setBrush(Brush)
       
       x = left
       rectWidth = self.margin + self.checkerSize + self.xOffset/2
       rectHeight = 30
       for i in range(self.col):
           rect = QRectF(x, top, rectWidth, rectHeight)
           area = dropArea(rect, i)
           self.dropAreas.append(area)
           self.addItem(area)
           painter.drawRect(rect)
           x += rectWidth
           if i+1 == 7:
               rectWidth = self.margin + self.checkerSize + self.xOffset/2
           else:
               rectWidth = self.checkerSize + self.xOffset


       firstTop = top + rectHeight + self.yOffset
       firstLeft = left + self.margin
       for x in range(firstLeft, right, self.checkerSize+self.xOffset):
           row = []
           for y in range(firstTop, bottom, self.checkerSize+self.yOffset):
               checker = QRectF(x, y, self.checkerSize, self.checkerSize)
               row.append(checker)
               painter.drawEllipse(checker)
           self.checkers.append(row)
        
       self.checkers = [value for value in self.checkers if value != []]
    
