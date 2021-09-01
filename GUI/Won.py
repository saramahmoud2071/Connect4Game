from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_WinWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        """ intializting window attributes """
        self.setGeometry(QRect(0, 0, 960, 682))
        self.setStyleSheet(u"background-color: rgb(0, 0, 0, 0.5);")

        """ adding window components """
        self.Ui_Components()


    def Ui_Components(self):

        """ background widget """
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 960, 682))

        """ Win widget """
        self.card = QWidget(self.widget)
        self.card.setObjectName(u"card")
        self.card.setGeometry(QRect(310, 170, 300, 340))
        self.card.setStyleSheet(u"background-color: None;")

        # upper part label
        self.upperLabel = QLabel(self.card)
        self.upperLabel.setObjectName(u"upperLabel")
        self.upperLabel.setGeometry(QRect(0, 0, 300, 130))
        self.upperLabel.setStyleSheet(u"border-top-right-radius: 50%;\n"
                                       "border-top-left-radius: 50%;\n"
                                       "background-color: rgb(0, 227, 0);")

        # "You Won" label
        self.won = QLabel(self.card)
        self.won.setObjectName(u"lost")
        self.won.setGeometry(QRect(100, 50, 150, 46))
        font = QFont()
        font.setFamily(u"Calisto MT")
        font.setPointSize(30)
        font.setItalic(True)
        self.won.setFont(font)
        self.won.setText(u"You Won")
        self.won.setStyleSheet(u"background-color: rgb(0, 227, 0);\n"
                                 "color: white")

        # emoji label
        self.emoji = QLabel(self.card)
        self.emoji.setObjectName(u"emoji")
        self.emoji.setGeometry(QRect(40, 50, 48, 48))
        self.emoji.setStyleSheet(u"background-color: rgb(0, 227, 0);")
        self.emoji.setPixmap(QPixmap(u"Icons/icons8-smiling-face-48.png"))

        # bottom part label
        self.bottomLabel = QLabel(self.card)
        self.bottomLabel.setObjectName(u"bottomLabel")
        self.bottomLabel.setGeometry(QRect(0, 130, 300, 160))
        self.bottomLabel.setStyleSheet(u"border-bottom-right-radius: 50%;\n"
                                        "border-bottom-left-radius: 50%;\n"
                                        "background-color: rgb(255, 255, 255);")

        # score label 
        self.scoreLabel = QLabel(self.card)
        self.scoreLabel.setObjectName(u"scoreLabel")
        self.scoreLabel.setGeometry(QRect(60, 170, 58, 23))
        font1 = QFont()
        font1.setFamily(u"Lucida Bright")
        font1.setPointSize(16)
        self.scoreLabel.setFont(font1)
        self.scoreLabel.setText(u"Score")
        self.scoreLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # time label 
        self.timeLabel = QLabel(self.card)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(60, 220, 55, 23))
        self.timeLabel.setFont(font1)
        self.timeLabel.setText(u"Time")
        self.timeLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        

        """ Score Value """
        self.score = QLabel(self.card)
        self.score.setObjectName(u"score")
        self.score.setGeometry(QRect(149, 170, 100, 27))
        font2 = QFont()
        font2.setPointSize(14)
        self.score.setFont(font2)
        self.score.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.score.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                  "border: 1px solid black;\n"
                                  "color: rgb(88, 92, 122);")

        """ Time Value """
        self.time = QLabel(self.card)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(150, 220, 100, 27))
        self.time.setFont(font2)
        self.time.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.time.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                  "border: 1px solid black;\n"
                                  "color: rgb(88, 92, 122);")
                                 
    """ passing the user score """                   
    def setScore(self, score: str):
        self.score.setText(score)

    """ passing the time consumed """
    def setTime(self, time: str):
        self.time.setText(time)

