import os
from elevate import elevate
from sys import exit as quit
import sys, time
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer, QEventLoop
from timer import Ui_timer

def is_root():
    return os.getuid() == 0

def getrooted():
    if is_root() == False:
        elevate()
    if is_root() == True:
        print("im now root")
    else:
        print("no roots here, cya")
        quit()

#getrooted()


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_timer()
        self.ui.setupUi(self)
        self.show()
        self.ui.StartButton.clicked.connect(self.button_pressed)
        self.counter = 0
        self.usertime = 0

    def button_pressed(self):
        self.button_waspressed = 1
        if self.counter == 0:
            self.usertime = int(self.ui.InputTime.toPlainText())
        if self.ui.checkBox.isChecked() == True:
            self.counter = self.usertime * 60
        else:
            self.counter = self.usertime
        self.ui.lcdNumber.display(self.counter)

        while self.counter > 0:
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()
            self.counter = self.counter - 1
            self.ui.lcdNumber.display(self.counter)
            if self.counter <= 0:
                self.counter = 0
                if self.button_waspressed == 1: #stops repeating command execution
                    self.button_waspressed = 0
                    if self.ui.checkBox2.isChecked() == True:
                        os.system("halt -p")
                    elif self.ui.checkBox3.isChecked() == True:
                        os.system("reboot")


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
