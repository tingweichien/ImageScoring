# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Import_Page = QtWidgets.QWidget()
        self.Import_Page.setObjectName("Import_Page")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Import_Page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(350, 190, 422, 260))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Upload_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Upload_label.setStyleSheet("font: 75 16pt \"Consolas\";")
        self.Upload_label.setObjectName("Upload_label")
        self.gridLayout.addWidget(self.Upload_label, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setStyleSheet("font: 75 16pt \"Consolas\";\n"
"")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.Upload_image_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Upload_image_label.setLineWidth(0)
        self.Upload_image_label.setObjectName("Upload_image_label")
        self.gridLayout.addWidget(self.Upload_image_label, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.Import_Page)
        self.Result_Page = QtWidgets.QWidget()
        self.Result_Page.setObjectName("Result_Page")
        self.image_result_frame = QtWidgets.QFrame(self.Result_Page)
        self.image_result_frame.setGeometry(QtCore.QRect(370, 140, 276, 446))
        self.image_result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_result_frame.setObjectName("image_result_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.image_result_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.import_image_label = QtWidgets.QLabel(self.image_result_frame)
        self.import_image_label.setObjectName("import_image_label")
        self.verticalLayout_2.addWidget(self.import_image_label)
        self.result_table = QtWidgets.QTableWidget(self.image_result_frame)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(1)
        self.result_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        self.verticalLayout_2.addWidget(self.result_table)
        self.stackedWidget.addWidget(self.Result_Page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Scoring"))
        self.Upload_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Drag &amp; Drop image files here</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">or</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Import"))
        self.Upload_image_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/image/src/image/upload.png\"/></p></body></html>"))
        self.import_image_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Image</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        item = self.result_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stock photo scoring"))
        item = self.result_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "UGC photo scoring"))
        item = self.result_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Image keyword"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "image 1"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
import image_rcs_rc
