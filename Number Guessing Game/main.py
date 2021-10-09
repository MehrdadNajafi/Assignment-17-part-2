from random import randint

from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class NumberGuess(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.ui.push_btn.clicked.connect(self.check)
        self.ui.ng_btn.clicked.connect(self.new_game)
        self.ui.radio_btn1.setChecked(True)

        self.game_continue = True
        self.create_number()

    def create_number(self):
        if self.ui.radio_btn1.isChecked():
            self.rand_num = randint(0, 50)
        
        elif self.ui.radio_btn2.isChecked():
            self.rand_num = randint(0, 100)
        
        elif self.ui.radio_btn3.isChecked():
            self.rand_num = randint(0, 1000)

    def new_game(self):
        self.create_number()
        self.ui.textlabel.setText('Guess a number')
        self.game_continue = True

    def check(self):
        try:
            if self.game_continue:
                guess_num = int(self.ui.textbox.text())
                if guess_num == self.rand_num:
                    self.ui.textlabel.setText('Nice, You Win')
                    self.game_continue = False
                
                elif guess_num < self.rand_num:
                    self.ui.textlabel.setText('Go Upper')
                
                elif guess_num > self.rand_num:
                    self.ui.textlabel.setText('Go Lower')
            
            else:
                self.ui.textlabel.setText('You already won the game\nPush New Game')
        except:
            pass

app = QApplication()
window = NumberGuess()
app.exec()