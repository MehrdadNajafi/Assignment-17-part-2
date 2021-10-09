import random

from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Password(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.ui.push_btn.clicked.connect(self.create_pass)
        self.ui.radio_btn1.setChecked(True)

        self.word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.special_word = ['!', '@', '#', '$', '%', '&', '*', '+', '=']

    def create_pass(self):
        new_pass = ''
        selected_range = 8
        
        if self.ui.radio_btn2.isChecked():
            selected_range = 12

        elif self.ui.radio_btn3.isChecked():
            selected_range = 20
            
        for i in range(selected_range):
            choice = random.randint(0, 2)
            choice_for_word = random.randint(0,1)
            
            if choice == 0:
                if choice_for_word == 0:
                    new_pass += random.choice(self.word_list)
                elif choice_for_word == 1:
                    new_pass += random.choice(self.word_list).upper()
            
            elif choice == 1:
                new_pass += str(random.randint(0, 9))

            elif choice == 2:
                new_pass += random.choice(self.special_word)
        self.ui.textbox.setText(new_pass)

app = QApplication([])
window = Password()
app.exec()