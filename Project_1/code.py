from PyQt5 import QtCore, QtGui, QtWidgets
import SentimentAnalysis
import re, csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 804)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 1201, 141))
        self.textEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 261, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 20, 441, 61))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 380, 601, 361))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 290, 281, 61))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 430, 301, 31))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 510, 301, 51))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 600, 301, 51))
        self.label_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1010, 420, 151, 61))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1010, 510, 151, 61))
        self.lineEdit_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1010, 600, 151, 61))
        self.lineEdit_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1248, 31))
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
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Review Analysis System"))
        self.label_2.setText(_translate("MainWindow", "Reviews Analysis"))
        self.label_3.setText(_translate("MainWindow", "Positive Reviews"))
        self.label_4.setText(_translate("MainWindow", "Negative Reviews"))
        self.label_5.setText(_translate("MainWindow", "Total Reviews"))

        self.pushButton.clicked.connect(self.prediction)
        self.printAnalysis()

    def printAnalysis(self):
        try:
            file = open('prediction.txt')
            self.data = file.read()
            # print(self.data)
            pattern = '([0-9]\d+|[0-9])'
            counts = re.findall(pattern, self.data)
            self.negCount = int(counts[0])
            self.posCount = int(counts[1])
            self.lineEdit.setText(counts[1])
            self.lineEdit_2.setText(counts[0])
            self.lineEdit_3.setText(str(int(counts[0])+int(counts[1])))

        except BaseException:
            file = open('prediction.txt','w')
            data = "Negative : 0, Positive : 0"
            file.write(data)
        finally:
            file.close()

    def prediction(self):
        text = self.textEdit.toPlainText()
        pred = SentimentAnalysis.test(text)
        # print(pred)
        if pred == 'Negative':
            self.negCount += 1
        else:
            self.posCount += 1

        self.readWrite(self.negCount, self.posCount)
        self.saveReview(text,pred)

    def readWrite(self,neg,pos):
        with open('prediction.txt','w') as file:
            data = "Negative : {}, Positive : {}".format(neg,pos)
            file.write(data)
        self.printAnalysis()

    def saveReview(self,text,pred):
        file = open('reviews.csv','a',newline='')
        data = {"review":text, "pred":pred}
        writer = csv.writer(file)
        writer.writerow(data.values())
        file.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
