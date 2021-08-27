from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from Game import Ui_GameWindow

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(u"Connect-4 Game")
        self.resize(582, 461)

        icon = QIcon()
        icon.addFile(u"Icons/connect4 16px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        self.Ui_Components()
        

    def Ui_Components(self):
        self.gameIcon = QLabel(self)
        self.gameIcon.setObjectName(u"gameIcon")
        self.gameIcon.setGeometry(QRect(120, 30, 71, 61))
        self.gameIcon.setPixmap(QPixmap(u"Icons/connect4 64px.png"))

        self.gameLabel = QLabel(self)
        self.gameLabel.setObjectName(u"gameLabel")
        self.gameLabel.setGeometry(QRect(190, 30, 281, 51))
        font1 = QFont()
        font1.setFamily(u"Calisto MT")
        font1.setPointSize(32)
        font1.setItalic(True)
        self.gameLabel.setFont(font1)
        self.gameLabel.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.gameLabel.setText(u"Connect-4 Game")

        self.AIsettings = QGroupBox(self)
        self.AIsettings.setObjectName(u"AIsettings")
        self.AIsettings.setGeometry(QRect(120, 130, 351, 161))
        font2 = QFont()
        font2.setFamily(u"Calisto MT")
        font2.setPointSize(16)
        font2.setItalic(True)
        self.AIsettings.setFont(font2)
        self.AIsettings.setStyleSheet(u"color: rgb(150, 0, 0);")
        self.AIsettings.setTitle(u"AI Agent settings")

        self.pruning = QCheckBox(self.AIsettings)
        self.pruning.setObjectName(u"pruning")
        self.pruning.setGeometry(QRect(30, 30, 261, 31))
        font3 = QFont()
        font3.setFamily(u"Lucida Sans Typewriter")
        font3.setPointSize(12)
        self.pruning.setFont(font3)
        self.pruning.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pruning.setStyleSheet(u"color: black;")
        self.pruning.setText(u"Minimax with \ud835\udfaa-\ud835\udf37 pruning")

        self.Klabel = QLabel(self.AIsettings)
        self.Klabel.setObjectName(u"Klabel")
        self.Klabel.setGeometry(QRect(30, 70, 31, 31))
        font4 = QFont()
        font4.setFamily(u"Lucida Sans Typewriter")
        font4.setPointSize(14)
        font4.setItalic(True)
        self.Klabel.setFont(font4)
        self.Klabel.setStyleSheet(u"color: black;")
        self.Klabel.setText(u"K*")

        self.K = QLineEdit(self.AIsettings)
        self.K.setObjectName(u"K")
        self.K.setGeometry(QRect(70, 70, 101, 31))
        font5 = QFont()
        font5.setPointSize(11)
        self.K.setFont(font5)
        self.K.setStyleSheet(u"color: rgb(63,63,63);")
        self.K.setValidator(QIntValidator(3, 64))

        self.invalidInput = QLabel(self.AIsettings)
        self.invalidInput.setObjectName(u"invalidInput")
        self.invalidInput.setGeometry(QRect(190, 70, 80, 31))
        font6 = QFont()
        font6.setPointSize(10)
        self.invalidInput.setFont(font6)
        self.invalidInput.setStyleSheet(u"color: red")

        self.Knote = QLabel(self.AIsettings)
        self.Knote.setObjectName(u"Knote")
        self.Knote.setGeometry(QRect(20, 120, 310, 16))
        font7 = QFont()
        font7.setFamily(u"Lucida Sans Unicode")
        font7.setPointSize(10)
        font7.setItalic(True)
        self.Knote.setFont(font7)
        self.Knote.setStyleSheet(u"color: black;")
        self.Knote.setText(u"* K is the level where the solution tree terminates")

        self.playLabel = QLabel(self)
        self.playLabel.setObjectName(u"playLabel")
        self.playLabel.setGeometry(QRect(210, 330, 71, 41))
        font8 = QFont()
        font8.setFamily(u"Calisto MT")
        font8.setPointSize(26)
        self.playLabel.setFont(font8)
        self.playLabel.setStyleSheet(u"color: rgb(46, 204, 113);")
        self.playLabel.setText(u"Play")

        self.play = QPushButton(self)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(290, 310, 91, 91))
        self.play.setMouseTracking(True)
        self.play.setStyleSheet(u"QPushButton#play {\n"
                                 "border-radius : 45;\n"
                                 "border : 4px solid rgb(46,204,113);\n"
                                 "background-color: rgb(46,204,113);\n"
                                 "}\n"
                                 "QPushButton#play:hover {\n"
                                 "border-color : white; \n"
                                 "}")
        icon1 = QIcon()
        icon1.addFile(u"Icons/icons8-play-90 .png", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setIconSize(QSize(40, 40))
        self.play.clicked.connect(self.play_clicked)
        

    def play_clicked(self):
        if self.K.hasAcceptableInput():
            self.window2 = Ui_GameWindow()
            self.window2.setParent(self)
            self.window2.show()
            self.close()
        else:
            self.invalidInput.setText("Invalid Input")
            

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window1 = Ui_MainWindow()
    window1.show()
    sys.exit(App.exec_())




        
        
        

        