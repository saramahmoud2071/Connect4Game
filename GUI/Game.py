from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

""" Solving algorithms """
from solvingAlgorithms.calculateScore import *
from solvingAlgorithms.Minimax import *

""" Game widgets """
from Grid import Grid
from Tree import Tree
from Won import Ui_WinWidget
from Tie import Ui_TieWidget
from Lost import Ui_LoseWidget

HUMAN = False
COMPUTER = True
   
class Ui_GameWindow(QMainWindow):

    def __init__(self, pruning: bool, k: int, parent=None):
        super().__init__(parent)
        
        """ passing game attributes """
        self.pruning = pruning
        self.k = k

        """ for storing which player has turn now """
        self.turn = HUMAN

        """ intializting window attributes """

        self.setWindowTitle(u"Connect-4 Game")
        self.resize(960, 682)

        icon = QIcon()
        icon.addFile(u"Icons/connect4-16px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        self.Ui_Components()


    def Ui_Components(self):
        """ window components """

        """ User widget """
        self.user = QWidget(self)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(50, 510, 180, 130))
        self.user.setStyleSheet(u"border-radius: 25%;\n"
                                 "background-color: rgb(252, 242, 215);\n"
                                 "border: 3px solid black ")

        # User label
        self.userLabel = QLabel(self.user)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setGeometry(QRect(80, 20, 61, 31))
        font = QFont()
        font.setFamily(u"Lucida Bright")
        font.setPointSize(16)
        font.setItalic(True)
        self.userLabel.setFont(font)
        self.userLabel.setText(u"User")
        self.userLabel.setStyleSheet(u"border: None")

        # red checker icon label
        self.redChecker = QLabel(self.user)
        self.redChecker.setObjectName(u"redChecker")
        self.redChecker.setGeometry(QRect(10, 10, 48, 48))
        self.redChecker.setStyleSheet(u"border: None")
        self.redChecker.setPixmap(QPixmap(u"Icons/icons8-red-circle-48.png"))

        # User widget breaking line
        self.line_1 = QFrame(self.user)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(0, 60, 180, 2))
        self.line_1.setStyleSheet(u"border: 1px solid black")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        # User turns label 
        self.redTurnsLabel = QLabel(self.user)
        self.redTurnsLabel.setObjectName(u"redTurnsLabel")
        self.redTurnsLabel.setGeometry(QRect(20, 70, 41, 19))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.redTurnsLabel.setFont(font1)
        self.redTurnsLabel.setText( u"Turns")
        self.redTurnsLabel.setStyleSheet(u"border: None;")

        # User score label 
        self.redScoreLabel = QLabel(self.user)
        self.redScoreLabel.setObjectName(u"redScoreLabel")
        self.redScoreLabel.setGeometry(QRect(20, 100, 39, 19))
        self.redScoreLabel.setFont(font1)
        self.redScoreLabel.setText(u"Score")
        self.redScoreLabel.setStyleSheet(u"border: None;")

        """ red turns Value """
        self.redTurns = QLabel(self.user)                               
        self.redTurns.setObjectName(u"redTurns")
        self.redTurns.setGeometry(QRect(80, 70, 80, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.redTurns.setFont(font2)
        self.redTurns.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.redTurns.setStyleSheet(u"background-color: #FFFFFF; \n"
                                     "border: 1px solid black")
        self.redTurns.setText("0")

        """ red turns Value """
        self.redScore = QLabel(self.user)
        self.redScore.setObjectName(u"redScore")
        self.redScore.setGeometry(QRect(80, 100, 80, 20))
        self.redScore.setFont(font2)
        self.redScore.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.redScore.setStyleSheet(u"background-color: #FFFFFF; \n"
                                     "border: 1px solid black")
        self.redScore.setText("0")


        """ Computer widget """
        self.computer = QWidget(self)
        self.computer.setObjectName(u"computer")
        self.computer.setGeometry(QRect(280, 510, 180, 130))
        self.computer.setStyleSheet(u"border-radius: 25%;\n"
                                     "background-color: rgb(252, 242, 215);\n"
                                     "border: 1px solid black ")

        # Computer label
        self.computerLabel = QLabel(self.computer)
        self.computerLabel.setObjectName(u"computerLabel")
        self.computerLabel.setGeometry(QRect(60, 20, 101, 31))
        self.computerLabel.setFont(font)
        self.computerLabel.setText(u"Computer")
        self.computerLabel.setStyleSheet(u"border: None")

        # yellow checker icon label
        self.yellowChecker = QLabel(self.computer)
        self.yellowChecker.setObjectName(u"yellowChecker")
        self.yellowChecker.setGeometry(QRect(10, 10, 48, 48))
        self.yellowChecker.setStyleSheet(u"border: None")
        self.yellowChecker.setPixmap(QPixmap(u"Icons/icons8-yellow-circle-48.png"))

        # Computer widget breaking line
        self.line_2 = QFrame(self.computer)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 60, 180, 2))
        self.line_2.setStyleSheet(u"border: 1px solid black")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        # Computer turns label 
        self.yellowTurnsLabel = QLabel(self.computer)
        self.yellowTurnsLabel.setObjectName(u"yellowTurnsLabel")
        self.yellowTurnsLabel.setGeometry(QRect(20, 70, 41, 19))
        self.yellowTurnsLabel.setFont(font1)
        self.yellowTurnsLabel.setText(u"Turns")
        self.yellowTurnsLabel.setStyleSheet(u"border: None;")

        # Computer score label 
        self.yellowScoreLabel = QLabel(self.computer)
        self.yellowScoreLabel.setObjectName(u"yellowScoreLabel")
        self.yellowScoreLabel.setGeometry(QRect(20, 100, 39, 19))
        self.yellowScoreLabel.setFont(font1)
        self.yellowScoreLabel.setText(u"Score")
        self.yellowScoreLabel.setStyleSheet(u"border: None;")

        """ yellow turns Value """
        self.yellowTurns = QLabel(self.computer)
        self.yellowTurns.setObjectName(u"yellowTurns")
        self.yellowTurns.setGeometry(QRect(80, 70, 80, 20))
        self.yellowTurns.setFont(font2)
        self.yellowTurns.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.yellowTurns.setStyleSheet(u"background-color: #FFFFFF; \n"
                                        "border: 1px solid black")
        self.yellowTurns.setText("0")

        """ yellow score Value """
        self.yellowScore = QLabel(self.computer)
        self.yellowScore.setObjectName(u"yellowScore")
        self.yellowScore.setGeometry(QRect(80, 100, 80, 20))
        self.yellowScore.setFont(font2)
        self.yellowScore.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.yellowScore.setStyleSheet(u"background-color: #FFFFFF; \n"
                                        "border: 1px solid black")
        self.yellowScore.setText("0")


        """ Timer widget """
        # Timer icon
        self.timerIcon = QLabel(self)
        self.timerIcon.setObjectName(u"timerIcon")
        self.timerIcon.setGeometry(QRect(210, 10, 24, 24))
        self.timerIcon.setPixmap(QPixmap(u"Icons/icons8-clock-24.png"))

        # Timer label
        self.timer = QLabel(self)
        self.timer.setObjectName(u"timer")
        self.timer.setGeometry(QRect(250, 10, 60, 24))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(13)
        font3.setItalic(True)
        font3.setWeight(50)
        self.timer.setFont(font3)

        # Timer calculator
        self.time = QTimer(self)
        self.startTime = int(time.time())
        self.time.timeout.connect(self.display_time)
        self.time.start(1000) # 1 second


        """ Exit button """
        self.exit = QCommandLinkButton(self)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(870, 0, 71, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(13)
        font4.setBold(False)
        self.exit.setFont(font4)
        self.exit.setText(u"Exit")
        self.exit.clicked.connect(self.exit_clicked)


        """ Game grid """
        self.grid = QGraphicsView(self)
        self.grid.setObjectName(u"grid")
        self.grid.setGeometry(QRect(20, 40, 460, 460))
        self.gridScene = Grid(self, self.grid)
        self.grid.setScene(self.gridScene)
        self.grid.setSceneRect(0, 0, 458, 458)


        """ Tree label """
        self.treeLabel = QLabel(self)
        self.treeLabel.setObjectName(u"treeLabel")
        self.treeLabel.setGeometry(QRect(680, 10, 110, 24))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(13)
        font5.setItalic(True)
        self.treeLabel.setFont(font5)
        self.treeLabel.setText(u"Minimax Tree")


        """ Minimax Tree """
        self.tree = Tree(self)
        self.tree.setObjectName(u"tree")
        self.tree.setGeometry(QRect(500, 40, 441, 601))


        """ Result LAyout """
        self.winWidget = Ui_WinWidget(self)
        self.winWidget.hide()

        self.loseWidget = Ui_LoseWidget(self)
        self.loseWidget.hide()

        self.tieWidget = Ui_TieWidget(self)
        self.tieWidget.hide()


    """ Calculating the score of the current state for the current player """
    def calculate_score(self, state, player):
        horizontal = 0
        vertical = 0
        rightDiagonal = 0
        leftDiagonal = 0

        for i in range (8):
            for j in range (8):
                # get no of connected 4 horizontally for the current player
                if j in range (0,5):
                   horizontal += horizontal4(state, player, i, j)

                # get no of connected 4 vertically for the current player
                if i in range (3,8):
                    vertical += vertical4(state, player, i, j)

                # get no of connected 4 diagonally for the current player
                if i in range(0,5):
                   if j in range (0,5):
                       rightDiagonal += rightDiagonal4(state, player, i, j)
                       
                   if j in range (3,8):
                        leftDiagonal += leftDiagonal4(state, player, i, j)
         
        return (horizontal + vertical + rightDiagonal + leftDiagonal)


    """ Swapping turns between human and computer """
    def take_turns(self):
        totalTurns = int(self.redTurns.text()) + int(self.yellowTurns.text())
        if totalTurns == 64:
            self.time.stop()
            if int(self.redScore.text()) > int(self.yellowScore.text()):
                self.winWidget.setScore(self.redScore.text())
                self.winWidget.setTime(self.timer.text())
                self.winWidget.show()
            elif int(self.redScore.text()) < int(self.yellowScore.text()):
                self.loseWidget.setScore(self.redScore.text())
                self.loseWidget.setTime(self.timer.text())
                self.loseWidget.show()
            else:
                self.tieWidget.setScore(self.redScore.text())
                self.tieWidget.setTime(self.timer.text())
                self.tieWidget.show()

        else:
            if self.turn == HUMAN:
              turns = int(self.redTurns.text()) + 1
              self.redTurns.setText(str(turns))
              score = self.calculate_score(self.gridScene.filledCheckers, self.turn)
              self.redScore.setText(str(score))
              self.user.setStyleSheet(u"border-radius: 25%;\n"
                                       "background-color: rgb(252, 242, 215);\n"
                                       "border: 1px solid black ")
              self.computer.setStyleSheet(u"border-radius: 25%;\n"
                                           "background-color: rgb(252, 242, 215);\n"
                                           "border: 3px solid black ")
              self.turn = COMPUTER
              self.play_computer()

            else:
              turns = int(self.yellowTurns.text()) + 1
              self.yellowTurns.setText(str(turns))
              score = self.calculate_score(self.gridScene.filledCheckers, self.turn)
              self.yellowScore.setText(str(score))
              self.computer.setStyleSheet(u"border-radius: 25%;\n"
                                           "background-color: rgb(252, 242, 215);\n"
                                           "border: 1px solid black ")
              self.user.setStyleSheet(u"border-radius: 25%;\n"
                                       "background-color: rgb(252, 242, 215);\n"
                                       "border: 3px solid black ")
              self.turn = HUMAN
              self.play_human()

    def play_human(self):
        dropAreas = self.gridScene.dropAreas
        for area in dropAreas:
            area.acceptPress = True
            area.setAcceptHoverEvents(True)

    def play_computer(self):
        dropAreas = self.gridScene.dropAreas
        for area in dropAreas:
            area.acceptPress = False
            area.setAcceptHoverEvents(False)
        
        state = self.gridScene.filledCheckers # AI
        decision, root = make_decision(state, self.k, self.pruning) # AI
        new_state, new_utility = decision
        column = self.column_changed(state, new_state) # AI
        #self.BFS(root)
        dropAreas[column].update()
    
    def column_changed(self, state, new_state):
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] != new_state[i][j]:
                    return j

    def BFS(self, intialNode):
        frontier = [intialNode]
        explored = set()

        text = "Minimax Tree Nodes:"

        while len(frontier) != 0:
            node = frontier.pop(0)
            explored.add(node.state)

            text = text + "parent = \n" + self.state_format(node.parent.sate) 
            if node.minimax == MAX:
              text = text + "Max" + "player \n"
            else:
              text = text + "Min" + "player \n"
            text = text + "added to col. " + str(node.change) + "\n"
            text = text + "utility = " + str(node.utility) + "\n"
            text = text + "depth = " + str(node.depth) + "\n"
            text = text + "state = \n" + self.state_format(node.state)

            self.tree.setText(text)
            
            for child in node.children:
                if child not in frontier and child.state not in explored:
                    frontier.append(child)
		

    def state_format(self, state):
        state_format = ""
        for i in range(8):
            for j in range(8):
                state_format = state_format + state[i][j] + " "
        state_format = state_format + "\n"

        return state_format

    def time_conversion(self, time_s):
        minutes = time_s // 60
        seconds = time_s % 60

        if minutes<10:
            minutes = "0" + str(minutes)
        if seconds<10:
            seconds = "0" + str(seconds)

        return str(minutes), str(seconds)

    def display_time(self):
        currentTime = int(time.time()) - self.startTime
        minutes, seconds = self.time_conversion(currentTime)
        displayTime = minutes + " : " + seconds

        self.timer.setText(displayTime)


    def exit_clicked(self):
        self.close()
        self.previous.show()
        
