from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen 
class Ui_timer(object):
    def setupUi(self, timer):
        timer.setObjectName("timer")
        timer.setWindowModality(QtCore.Qt.ApplicationModal)
        timer.resize(525, 348)
        timer.setWindowTitle("Dragonkeeper: Timer")
        timer.setAutoFillBackground(True)
        timer.setSizeGripEnabled(True)
        timer.setModal(True)
        palette = timer.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 204, 0))
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        timer.setPalette(palette)

        self.verticalLayoutWidget = QtWidgets.QWidget(timer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 348))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 200))
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(500, 100))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.InputTime = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.InputTime.setMaximumSize(QtCore.QSize(500, 100))
        self.InputTime.setObjectName("InputTime")
        self.horizontalLayout_3.addWidget(self.InputTime)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_2.addWidget(self.StartButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setMinimumSize(QtCore.QSize(300, 0))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox2.setMinimumSize(QtCore.QSize(300, 0))
        self.checkBox2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox2.setObjectName("checkBox2")
        self.horizontalLayout.addWidget(self.checkBox2)

        self.checkBox3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox3.setMinimumSize(QtCore.QSize(300, 0))
        self.checkBox3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox3.setObjectName("checkBox3")
        self.horizontalLayout.addWidget(self.checkBox3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(timer)
        QtCore.QMetaObject.connectSlotsByName(timer)

    def retranslateUi(self, timer):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("timer", "Time:  "))
        self.StartButton.setText(_translate("timer", "Start"))
        self.checkBox.setText(_translate("timer", ": Mins"))
        self.checkBox2.setText(_translate("timer", ": Shutdown:  "))
        self.checkBox3.setText(_translate("timer", ": Restart"))
        palette = self.lcdNumber.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 204, 0))
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.lcdNumber.setPalette(palette)

        palette = self.label.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 204, 0))
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.label.setPalette(palette)

        palette = self.checkBox.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 204, 0))
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.checkBox.setPalette(palette)

        palette = self.checkBox2.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 204, 0))
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.checkBox2.setPalette(palette)

        palette = self.checkBox3.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 204, 0))
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.checkBox3.setPalette(palette)
