from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from math import *

class Tree(QGraphicsScene):

    def __init__(self, root, parent=None):
        super().__init__(parent)

        self.root = root
        self.drawNode(self.root)

    def drawNode(self, node):
        pass

    def drawLine(self, node):
        pass

    def drawArrow(self, node):
        pass