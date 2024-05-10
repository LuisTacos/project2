from PyQt6.QtWidgets import *
from calculator import *
import math
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clear)
        self.equalButton.clicked.connect(self.calculate)
        self.backButton.clicked.connect(self.delete)

        '''operators'''
        self.addButton.clicked.connect(self.addition)
        self.minusButton.clicked.connect(self.subtraction)
        self.multiplyButton.clicked.connect(self.multiplication)
        self.divideButton.clicked.connect(self.division)
        self.decimalButton.clicked.connect(self.decimal)

        '''numbers'''
        self.zeroButton.clicked.connect(self.zero)
        self.oneButton.clicked.connect(self.one)
        self.twoButton.clicked.connect(self.two)
        self.threeButton.clicked.connect(self.three)
        self.fourButton.clicked.connect(self.four)
        self.fiveButton.clicked.connect(self.five)
        self.sixButton.clicked.connect(self.six)
        self.sevenButton.clicked.connect(self.seven)
        self.eightButton.clicked.connect(self.eight)
        self.nineButton.clicked.connect(self.nine)



    '''clear/calculate'''
    def clear(self):
        self.outputLabel.setText("")

    def calculate(self):
        expression = self.outputLabel.text()
        try:
            result = eval(expression)
            self.outputLabel.setText(str(result))
        except Exception:
            self.outputLabel.setText("Error")


    def delete(self):
        text = self.outputLabel.text()
        if text:
            # Remove the last character from the text
            text = text[:-1]
            self.outputLabel.setText(text)
    '''operators'''
    def addition(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '+')

    def subtraction(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '-')

    def multiplication(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '*')

    def division(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '/')

    def decimal(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '.')

    '''numbers'''
    def zero(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '0')
    def one(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '1')
    def two(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '2')
    def three(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '3')
    def four(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '4')
    def five(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '5')
    def six(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '6')
    def seven(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '7')
    def eight(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '8')
    def nine(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + '9')

