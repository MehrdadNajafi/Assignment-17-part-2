from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Translator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.load_database()

        self.ui.translate_btn.clicked.connect(self.translate)

        self.ui.radio_btn1.setChecked(True)

    def load_database(self):
        self.translate_list = []
        data = open('translate.txt', 'r', encoding="utf-8")
        data = data.read()
        data = data.split('\n')
        for i in range(1, len(data), 2):
            dict = {'english' : data[i-1],
                    'persian' : data[i]  }
            self.translate_list.append(dict)
    
    def translate(self):
        try:
            text = str(self.ui.textbox.text()).lower()
            text = str(text).split(' ')
            translate_text = ''

            if self.ui.radio_btn1.isChecked():
                for item in text:
                    for word in self.translate_list:
                        if item == word['english']:
                            if item == text[-1]:
                                translate_text += word['persian']
                            else:
                                translate_text += word['persian'] + ' '
                            break
                    else:
                        translate_text += '???' + ' '
            
            elif self.ui.radio_btn2.isChecked():
                for item in text:
                    for word in self.translate_list:
                        if item == word['persian']:
                            if item == text[-1]:
                                translate_text += word['english']
                            else:
                                translate_text += word['english'] + ' '
                            break
                    else:
                        translate_text += '???' + ' '

            self.ui.label.setText(str(translate_text))

        except:
            pass

app = QApplication([])
window = Translator()
app.exec()