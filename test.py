from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QStackedWidget, QPushButton, QFileDialog
from PyQt5 import uic, QtCore
import sys
import os


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Drag and Drop")
        # self.resize(720, 480)
        uic.loadUi('GUI.ui', self) # Load the .ui file
        _translate = QtCore.QCoreApplication.translate
        self.Upload_image_label= self.findChild(QLabel, 'Upload_image_label')
        self.Upload_image_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\"src/image/upload.png\"/></p></body></html>"))
        self.setAcceptDrops(True)
        self.import_image_label = self.findChild(QLabel, 'import_image_label') # Find the button
        self.return_button = self.findChild(QPushButton, 'return_button')
        self.return_button.clicked.connect(self.return_button_func)



        #\ setting background color to label when
        #\ mouse is not hovering over it(anti hover)
        self.Import_button = self.findChild(QPushButton, 'Import_button')
        self.Import_button.clicked.connect(self.Import_button_func)
        self.Import_button.setStyleSheet("""
                            QPushButton::hover {
                                font: 75 16pt "Consolas";
                                border-style: outset;
                                background-color : rgb(200, 240, 240);
                             }
                            QPushButton::pressed {
                                font: 75 16pt "Consolas";
                                border-style: outset;
                                background-color : rgb(100, 140, 140);
                             }
                            QPushButton{
                                font: 75 16pt "Consolas";
                                border-style: outset;
                                border-width: 2px;
                                border-color: black;
                                background-color : rgb(220, 245, 245);
                             }
                             """)

        




    def Import_button_func(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',os.getcwd(),"Image files (*.jpg *.png)")
        print(f"image : {fname[0]}")
        print(f"image type : {fname[1]}")
        if fname[0] is not '':
            self.stackedWidget.setCurrentIndex(1)



    def return_button_func(self, event):
        self.stackedWidget.setCurrentIndex(0)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f"image file : {f}")

        #\ go to next page
        self.stackedWidget = self.findChild(QStackedWidget, 'stackedWidget')
        self.stackedWidget.setCurrentIndex(1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())