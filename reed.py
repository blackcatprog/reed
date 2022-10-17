from winreg import *

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        MainWindow.resize(790, 540)
        MainWindow.setMinimumSize(QtCore.QSize(790, 542))
        MainWindow.setMaximumSize(QtCore.QSize(790, 542))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 261, 541))
        self.frame.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(75, 470, 111, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 3px;\n"
"border: 5px;\n"
"background-color: rgb(1, 159, 151);\n"
"color: black;")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(90, 40, 74, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 224, 16))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 0, 744, 198))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 5, 260, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(170, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 3px;\n"
"border: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.lineEdit_4.setMaxLength(12)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 3px;\n"
"border: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(150, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 3px;\n"
"border: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.lineEdit_2.setMaxLength(12)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(150, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius: 3px;\n"
"border: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.lineEdit_3.setMaxLength(12)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius: 3px;\n"
"border: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.lineEdit_5.setMaxLength(12)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 5, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 210, 414, 84))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(15, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_5.setText("<a style='text-decoration: none; color: white;' href='https://github.com/blackcatprog/cli-vk-cleaner'>REED</a>")
        self.label_5.setOpenExternalLinks(True)

        # buttons bind
        self.pushButton.clicked.connect(lambda: self.apply())

    def apply(self):
        try:
            if self.checkBox.isChecked():
                path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
                key = CreateKey(HKEY_CURRENT_USER, path)
                SetValueEx(key, "ShowSecondsInSystemClock", 0, REG_DWORD, 0x0000001)
                CloseKey(key)
            else:
                path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
                key = CreateKey(HKEY_CURRENT_USER, path)
                SetValueEx(key, "ShowSecondsInSystemClock", 0, REG_DWORD, 0x0000000)
                CloseKey(key)

            #selected colors
            path = r"Control Panel\Colors"
            key = OpenKey(HKEY_CURRENT_USER, path, 0, KEY_ALL_ACCESS)
            hilight = self.lineEdit.text()
            hilight_text = self.lineEdit_2.text()
            SetValueEx(key, "Hilight", 0, REG_SZ, hilight)
            SetValueEx(key, "HilightText", 0, REG_SZ, hilight_text)
            CloseKey(key)

            #deafult new folder name
            path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\NamingTemplates"
            key = CreateKey(HKEY_CURRENT_USER, path)
            folder_name = self.lineEdit_3.text()
            SetValueEx(key, "RenameNameTemplate", 0, REG_SZ, folder_name)
            CloseKey(key)

            #change libs title
            path = r"SOFTWARE\Classes\CLSID\{031E4825-7B94-4dc3-B131-E946B44C8DD5}"
            key = CreateKey(HKEY_CURRENT_USER, path)
            libs_name = self.lineEdit_4.text()
            SetValueEx(key, "LocalizedString", 0, REG_SZ, libs_name)
            CloseKey(key)

            #on camera notification
            if self.checkBox_2.isChecked():
                path = r"SOFTWARE\Microsoft\OEM\Device\Capture"
                key = CreateKey(HKEY_LOCAL_MACHINE, path)
                SetValueEx(key, "NoPhysicalCameraLED", 0, REG_DWORD, 0x0000001)
                CloseKey(key)
            else:
                path = r"SOFTWARE\Microsoft\OEM\Device\Capture"
                key = CreateKey(HKEY_LOCAL_MACHINE, path)
                SetValueEx(key, "NoPhysicalCameraLED", 0, REG_DWORD, 0x0000000)
                CloseKey(key)

            #preview size on taskbar
            path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Taskband"
            key = CreateKey(HKEY_CURRENT_USER, path)
            libs_name = self.lineEdit_5.text()
            SetValueEx(key, "MinThumbSizePx", 0, REG_DWORD, 400)
            CloseKey(key)

            #delete "Edit with Paint 3D" from context menu
            if self.checkBox_3.isChecked():
                path_list = [
                    r"SOFTWARE\Classes\SystemFileAssociations\.jpg\Shell\3D Edit",
                    r"SOFTWARE\Classes\SystemFileAssociations\.jpeg\Shell\3D Edit",
                    r"SOFTWARE\Classes\SystemFileAssociations\.png\Shell\3D Edit",
                    r"SOFTWARE\Classes\SystemFileAssociations\.bmp\Shell\3D Edit",
                    r"SOFTWARE\Classes\SystemFileAssociations\.jpe\Shell\3D Edit"
                ]
            
                for path in path_list:
                    try:
                        DeleteKey(OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_ALL_ACCESS), "")
                    except Exception:
                        pass

        except PermissionError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Запустите программу от имени администратора!")
            msg.setWindowTitle("Внимание!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REED"))
        self.pushButton.setText(_translate("MainWindow", "Применить"))
        self.label_5.setText(_translate("MainWindow", "REED"))
        self.label_6.setText(_translate("MainWindow", "Кастомизация Windows, через реестр"))
        self.label.setText(_translate("MainWindow", "Цвет выделения"))
        self.label_2.setText(_translate("MainWindow", "Цвет выделенного текста"))
        self.label_3.setText(_translate("MainWindow", "Имя новой папки по умолчанию       "))
        self.label_4.setText(_translate("MainWindow", "Название раздела \"Библиотеки\""))
        self.label_7.setText(_translate("MainWindow", "Размер превью программы на панели задач"))
        self.checkBox.setText(_translate("MainWindow", "Отображение секунд в часах"))
        self.checkBox_2.setText(_translate("MainWindow", "Показывать уведомление о включении камеры"))
        self.checkBox_3.setText(_translate("MainWindow", "Убрать \"Изменить с помощью Paint 3D\" из контекстного меню"))
        self.lineEdit.setText("56 148 255")
        self.lineEdit_2.setText("255 255 255")
        self.lineEdit_3.setText("Новая папка")
        self.lineEdit_4.setText("Библиотеки")
        self.lineEdit_5.setText("400")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())