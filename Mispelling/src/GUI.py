# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Mispelling(object):
    def setupUi(self, Mispelling):
        Mispelling.setObjectName(_fromUtf8("Mispelling"))
        Mispelling.resize(801, 424)
        Mispelling.setWindowOpacity(1.0)
        Mispelling.setAutoFillBackground(False)
        Mispelling.setStyleSheet(_fromUtf8("background-color: rgb(25, 25, 25);"))
        self.centralwidget = QtGui.QWidget(Mispelling)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 171, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 209, 781, 111))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(255, 94, 94); ;\n"
"}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 20, 781, 91))
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 781, 101))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(102, 137, 153)\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(102, 137, 153) ;\n"
"}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 20, 781, 81))
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 360, 171, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Mispelling.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Mispelling)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Mispelling.setStatusBar(self.statusbar)

        self.retranslateUi(Mispelling)
        QtCore.QMetaObject.connectSlotsByName(Mispelling)

    def retranslateUi(self, Mispelling):
        Mispelling.setWindowTitle(_translate("Mispelling", "Mispelling", None))
        self.pushButton.setText(_translate("Mispelling", "Send", None))
        self.groupBox.setTitle(_translate("Mispelling", "Text", None))
        self.groupBox_2.setTitle(_translate("Mispelling", "Original Text", None))
        self.pushButton_2.setText(_translate("Mispelling", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Mispelling = QtGui.QMainWindow()
    ui = Ui_Mispelling()
    ui.setupUi(Mispelling)
    Mispelling.show()
    sys.exit(app.exec_())

