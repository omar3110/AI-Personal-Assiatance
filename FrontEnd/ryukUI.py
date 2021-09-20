
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ryuk(object):
    def setupUi(self, Ryuk):
        Ryuk.setObjectName("Ryuk")
        Ryuk.resize(694, 586)
        self.centralwidget = QtWidgets.QWidget(Ryuk)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 600))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 281, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            "I:/ryuk - Copy/initializing.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 611, 331))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("I:/ryuk - Copy/wave.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 420, 421, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("I:/ryuk - Copy/loading.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 61, 23))
        self.pushButton.setStyleSheet("background-color: rgb(229, 215, 10);\n"
                                      "\n"
                                      "font: 75 8pt \"Small Fonts\";\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 510, 61, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(139, 3, 3);\n"
                                        "font: 75 8pt \"Small Fonts\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 10, 111, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("I:/ryuk - Copy/frame1.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 10, 111, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("I:/ryuk - Copy/frame1.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(460, 30, 91, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
                                       "font: 75 14pt \"Small Fonts\";\n"
                                       "color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(570, 30, 91, 31))
        self.textBrowser_2.setStyleSheet("background-color: transparent;\n"
                                         "font: 75 14pt \"Small Fonts\";\n"
                                         "color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        Ryuk.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ryuk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 21))
        self.menubar.setObjectName("menubar")
        Ryuk.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ryuk)
        self.statusbar.setObjectName("statusbar")
        Ryuk.setStatusBar(self.statusbar)

        self.retranslateUi(Ryuk)
        QtCore.QMetaObject.connectSlotsByName(Ryuk)

    def retranslateUi(self, Ryuk):
        _translate = QtCore.QCoreApplication.translate
        Ryuk.setWindowTitle(_translate("Ryuk", "MainWindow"))
        self.label.setText(_translate("Ryuk", "TextLabel"))
        self.pushButton.setText(_translate("Ryuk", "RUN"))
        self.pushButton_2.setText(_translate("Ryuk", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ryuk = QtWidgets.QMainWindow()
    ui = Ui_Ryuk()
    ui.setupUi(Ryuk)
    Ryuk.show()
    sys.exit(app.exec_())
