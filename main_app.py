from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 300)
        MainWindow.setMinimumSize(QtCore.QSize(300, 250))
        MainWindow.setMaximumSize(QtCore.QSize(350, 300))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        self.nilaiUTSLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.nilaiUTSLabel.setFont(font)
        self.nilaiUTSLabel.setObjectName("nilaiUTSLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nilaiUTSLabel)
        self.inputNilaiUts = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.inputNilaiUts.setFont(font)
        self.inputNilaiUts.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputNilaiUts.setObjectName("inputNilaiUts")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputNilaiUts)
        
        self.nilaiUASLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.nilaiUASLabel.setFont(font)
        self.nilaiUASLabel.setObjectName("nilaiUASLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nilaiUASLabel)
        self.inputNilaiUas = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.inputNilaiUas.setFont(font)
        self.inputNilaiUas.setObjectName("inputNilaiUas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputNilaiUas)
        
        self.nilaiTugasLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.nilaiTugasLabel.setFont(font)
        self.nilaiTugasLabel.setObjectName("nilaiTugasLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nilaiTugasLabel)
        self.inputNilaiTugas = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.inputNilaiTugas.setFont(font)
        self.inputNilaiTugas.setObjectName("inputNilaiTugas")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputNilaiTugas)
        
        self.nilaiPraktikLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.nilaiPraktikLabel.setFont(font)
        self.nilaiPraktikLabel.setObjectName("nilaiPraktikLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.nilaiPraktikLabel)
        self.inputNilaiPraktik = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.inputNilaiPraktik.setFont(font)
        self.inputNilaiPraktik.setObjectName("inputNilaiPraktik")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputNilaiPraktik)
        
        self.nilaiAngkaLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.nilaiAngkaLabel.setFont(font)
        self.nilaiAngkaLabel.setObjectName("nilaiAngkaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.nilaiAngkaLabel)
        self.outputNilaiAngka = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.outputNilaiAngka.setFont(font)
        self.outputNilaiAngka.setObjectName("outputNilaiAng ka")
        self.outputNilaiAngka.setReadOnly(True)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.outputNilaiAngka)
        
        self.nilaiHurufLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.nilaiHurufLabel.setFont(font)
        self.nilaiHurufLabel.setObjectName("nilaiHurufLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nilaiHurufLabel)
        self.outputNilaiHuruf = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.outputNilaiHuruf.setFont(font)
        self.outputNilaiHuruf.setObjectName("outputNilaiHuruf")
        self.outputNilaiHuruf.setReadOnly(True)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.outputNilaiHuruf)
        
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.buttonHitung = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHitung.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonHitung.setFont(font)
        self.buttonHitung.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonHitung.setObjectName("buttonHitung")
        self.buttonHitung.clicked.connect(self.hitung_nilai)
        self.horizontalLayout.addWidget(self.buttonHitung)
        
        self.buttonKosongkan = QtWidgets.QPushButton(self.centralwidget)
        self.buttonKosongkan.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonKosongkan.setFont(font)
        self.buttonKosongkan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonKosongkan.setObjectName("buttonKosongkan")
        self.buttonKosongkan.clicked.connect(self.kosongkan_input)
        self.horizontalLayout.addWidget(self.buttonKosongkan)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hitung Nilai"))
        self.label.setText(_translate("MainWindow", "HITUNG NILAI"))
        self.nilaiUTSLabel.setText(_translate("MainWindow", "Nilai UTS"))
        self.inputNilaiUts.setPlaceholderText(_translate("MainWindow", "Masukan Nilai UTS"))
        self.nilaiUASLabel.setText(_translate("MainWindow", "Nilai UAS"))
        self.inputNilaiUas.setPlaceholderText(_translate("MainWindow", "Masukan Nilai UAS"))
        self.nilaiTugasLabel.setText(_translate("MainWindow", "Nilai Tugas"))
        self.inputNilaiTugas.setPlaceholderText(_translate("MainWindow", "Masukan Nilai Tugas"))
        self.nilaiPraktikLabel.setText(_translate("MainWindow", "NilaiPraktik"))
        self.inputNilaiPraktik.setPlaceholderText(_translate("MainWindow", "Masukan Nilai Praktik"))
        self.nilaiAngkaLabel.setText(_translate("MainWindow", "Nilai Angka"))
        self.nilaiHurufLabel.setText(_translate("MainWindow", "Nilai Huruf"))
        self.buttonHitung.setText(_translate("MainWindow", "HITUNG"))
        self.buttonKosongkan.setText(_translate("MainWindow", "KOSONGKAN"))

    def hitung_nilai(self):
        nilai_uts = float(self.inputNilaiUts.text())
        nilai_uas = float(self.inputNilaiUas.text())
        nilai_tugas = float(self.inputNilaiTugas.text())
        nilai_praktik = float(self.inputNilaiPraktik.text())

        nilai_akhir = (0.2 * nilai_uts) + (0.2 * nilai_uas) + (0.3 * nilai_tugas) + (0.3 * nilai_praktik)

        if nilai_akhir >= 80:
            nilai_huruf = "A"
        elif nilai_akhir >= 71:
            nilai_huruf = "B+"
        elif nilai_akhir >= 65:
            nilai_huruf = "B"
        elif nilai_akhir >= 60:
            nilai_huruf = "C+"
        elif nilai_akhir >= 55:
            nilai_huruf = "C"
        elif nilai_akhir >= 50:
            nilai_huruf = "D+"
        elif nilai_akhir >= 40:
            nilai_huruf = "D"
        else:
            nilai_huruf = "E"
        
        self.outputNilaiAngka.setText(str(nilai_akhir))
        self.outputNilaiHuruf.setText(str(nilai_huruf))

    def kosongkan_input(self):
        self.inputNilaiUts.clear()
        self.inputNilaiUas.clear()
        self.inputNilaiTugas.clear()
        self.inputNilaiPraktik.clear()
        self.outputNilaiAngka.clear()
        self.outputNilaiHuruf.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
