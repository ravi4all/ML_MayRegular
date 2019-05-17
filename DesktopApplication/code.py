# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import prediction

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 261, 81))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 600, 541, 81))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 261, 81))
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 290, 261, 81))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 400, 261, 81))
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 510, 371, 81))
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 70, 331, 71))
        self.lineEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 170, 331, 71))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 290, 331, 71))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 510, 331, 71))
        self.lineEdit_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(500, 420, 151, 41))
        self.radioButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(660, 420, 151, 41))
        self.radioButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Living Area"))
        self.pushButton.setText(_translate("MainWindow", "DO Prediction"))
        self.label_2.setText(_translate("MainWindow", "Land Value"))
        self.label_3.setText(_translate("MainWindow", "Rooms"))
        self.label_4.setText(_translate("MainWindow", "Central Air"))
        self.label_5.setText(_translate("MainWindow", "Predicted Price"))
        self.radioButton.setText(_translate("MainWindow", "Yes"))
        self.radioButton_2.setText(_translate("MainWindow", "No"))

        self.pushButton.clicked.connect(self.predict)

    def predict(self):
        try:
            livingArea = int(self.lineEdit.text())
            landValue = int(self.lineEdit_2.text())
            rooms = int(self.lineEdit_3.text())
            y_pred = prediction.pred(livingArea, landValue, rooms)
            print(y_pred)
            # self.lineEdit_5.text(str(y_pred))
        except BaseException as ex:
            print(ex)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
