import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times", 14)
computerScore = 0
playerScore = 0

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(350, 150, 550, 550)
		self.setWindowTitle("Rock Paper Scissors GAME")
		self.UI()

	def UI(self):
		#######################SCORES##############################
		self.scoreComputerText = QLabel("Computer score:    ", self)
		self.scorePlayerText = QLabel("Your score:     ", self)

		self.scoreComputerText.move(30,20)
		self.scorePlayerText.move(330,20)

		self.scoreComputerText.setFont(textFont)
		self.scorePlayerText.setFont(textFont)

		#######################IMAGES##############################
		self.imageComputer = QLabel(self)
		self.imageComputer.setPixmap(QPixmap("images/rock.png"))
		self.imageComputer.move(50, 100)

		self.imagePlayer = QLabel(self)
		self.imagePlayer.setPixmap(QPixmap("images/rock.png"))
		self.imagePlayer.move(330, 100)

		self.imageGame = QLabel(self)
		self.imageGame.setPixmap(QPixmap("images/game.png"))
		self.imageGame.move(230, 160)

		#######################BUTTONS##############################
		self.btnStart = QPushButton("Start", self)
		self.btnStart.setFont(textFont)
		self.btnStart.move(100, 300)

		self.btnStop = QPushButton("Stop", self)
		self.btnStop.setFont(textFont)
		self.btnStop.move(350, 300)

		self.btnStart.clicked.connect(self.start)
		self.btnStop.clicked.connect(self.stop)
		#######################TIMER##############################
		self.timer = QTimer(self)
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.playGame)


	def playGame(self):
		self.rndComputer = randint(1, 3)
		if (self.rndComputer == 1):
			self.imageComputer.setPixmap(QPixmap("images/rock.png"))
		elif (self.rndComputer == 2):
			self.imageComputer.setPixmap(QPixmap("images/paper.png"))
		elif (self.rndComputer == 3):
			self.imageComputer.setPixmap(QPixmap("images/scissors.png"))

		self.rndPlayer = randint(1, 3)
		if (self.rndPlayer == 1):
			self.imagePlayer.setPixmap(QPixmap("images/rock.png"))
		elif (self.rndPlayer == 2):
			self.imagePlayer.setPixmap(QPixmap("images/paper.png"))
		elif (self.rndPlayer == 3):
			self.imagePlayer.setPixmap(QPixmap("images/scissors.png"))


	def start(self):
		self.timer.start()


	def stop(self):
		global computerScore
		global playerScore
		self.timer.stop()

		if self.rndComputer == self.rndPlayer:
			QMessageBox.information(self, "Information", "Draw Game")

		elif self.rndComputer== 1 and self.rndPlayer == 2:
			QMessageBox.information(self,"Information","You Win")
			playerScore +=1
			self.scorePlayerText.setText("Your Score:{}".format(playerScore))
		elif self.rndComputer == 1 and self.rndPlayer == 3:
			QMessageBox.information(self, "Information", "Computer Wins")
			computerScore +=1
			self.scoreComputerText.setText("Computer Score:{}".format(computerScore))

		elif self.rndComputer == 2 and self.rndPlayer ==1:
			QMessageBox.information(self, "Information", "Computer Wins")
			computerScore += 1
			self.scoreComputerText.setText("Computer Score:{}".format(computerScore))
		elif self.rndComputer == 2 and self.rndPlayer == 3:
			QMessageBox.information(self, "Information", "You Win")
			playerScore += 1
			self.scorePlayerText.setText("Your Score:{}".format(playerScore))

		elif self.rndComputer == 3 and self.rndPlayer == 1:
			QMessageBox.information(self, "Information", "You Win")
			playerScore += 1
			self.scorePlayerText.setText("Your Score:{}".format(playerScore))
		elif self.rndComputer == 3 and self.rndPlayer ==2:
			QMessageBox.information(self, "Information", "Computer Wins")
			computerScore += 1
			self.scoreComputerText.setText("Computer Score:{}".format(computerScore))

		if computerScore == 3 or playerScore ==3 :
			mbox=QMessageBox.information(self,"Information","Game Over")
			sys.exit()



def main():
	App = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(App.exec_())

if __name__ == '__main__':
	main()