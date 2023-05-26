from PyQt5 import QtCore, QtGui, QtWidgets
from funcs import download_folder, painting


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 486)
        MainWindow.setStyleSheet("  color: rgb(85, 170, 255);    \n"
                                 "  background-color: #373e4e;\n"
                                 "  padding: 10px;\n"
                                 "  selection-background-color: rgb(39, 44, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, -7, 331, 61))
        self.label.setStyleSheet("  color: rgb(85, 170, 255);    \n"
                                 "  background-color: #373e4e;\n"
                                 "  padding: 10px;\n"
                                 "  selection-background-color: rgb(39, 44, 54);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 56, 331, 351))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setStyleSheet(" color: rgb(85, 170, 255);    \n"
                                    "  background-color: #373e4e;\n"
                                    "  padding: 10px;\n"
                                    "  selection-background-color: rgb(39, 44, 54);\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(120, 183, 140);\n"
                                      "border-radius: 20px;\n"
                                      "border: 2px solid #094065;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 41))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.rosstat_function)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">Выберите квартал и год</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow",
                                                "3 квартал 2022 года"))
        self.comboBox.setItemText(1, _translate("MainWindow",
                                                "2 квартал 2022 года"))
        self.comboBox.setItemText(2, _translate("MainWindow",
                                                "1 квартал 2022 года"))
        self.comboBox.setItemText(3, _translate("MainWindow", "2021 год"))
        self.comboBox.setItemText(4, _translate("MainWindow",
                                                "3 квартал 2021 года"))
        self.comboBox.setItemText(5, _translate("MainWindow",
                                                "2 квартал 2021 года"))
        self.comboBox.setItemText(6, _translate("MainWindow",
                                                "1 квартал 2021 года"))
        self.pushButton.setText(_translate("MainWindow", "Запустить"))

    def rosstat_function(self):
        download_folder(self.comboBox.currentIndex() + 1)
        painting()
