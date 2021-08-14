# -*- coding: utf-8 -*-
import shutil
from PyQt5 import QtCore, QtWidgets

_translate = QtCore.QCoreApplication.translate

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(355,153)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 261, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(269, 39, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 71, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(11, 91, 261, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(269, 120, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 120, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.selectjpg)
        self.pushButton_2.clicked.connect(self.selectzip)
        self.pushButton_3.clicked.connect(exit)
        self.pushButton_4.clicked.connect(self.run)

        self.setWindowTitle(_translate("MainWindow", "zip2jpg"))
        self.label.setText(_translate("MainWindow", "jpg파일"))
        self.pushButton.setText(_translate("MainWindow", "찾아보기"))
        self.label_2.setText(_translate("MainWindow", "zip파일"))
        self.pushButton_2.setText(_translate("MainWindow", "찾아보기"))
        self.pushButton_3.setText(_translate("MainWindow", "닫기"))
        self.pushButton_4.setText(_translate("MainWindow", "시작"))
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()
    
    def selectjpg(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './')
        self.lineEdit.setText(_translate("Dialog", fname[0]))
    
    def selectzip(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './')
        self.lineEdit_2.setText(_translate("Dialog", fname[0]))
    
    def run(self):
        jpgName = self.lineEdit.text()
        zipName = self.lineEdit_2.text()
        newfile = jpgName[:-4]+'_i'+'.jpg'

        with open(zipName, 'rb') as t:
            data = t.read()

        try:
            shutil.copy(jpgName, newfile)
        except:
            pass

        with open(newfile,'ab+') as z:
            z.write(data)
        QtWidgets.QMessageBox.information(self,'작업 완료!','프로그램이 작업을 완료했습니다.',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.Yes)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
