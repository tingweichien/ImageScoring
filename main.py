from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QStackedWidget, QPushButton, QFileDialog, QWidget, QMessageBox, QFrame, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import sys
import os
import Index
import requests
import threading
from popup_animation import LoadingScreen, QThread_Worker



#\ main GUI function
class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Drag and Drop")
        # self.resize(720, 480)
        self.setWindowIcon(QtGui.QIcon(Index.icon_path))
        uic.loadUi('GUI.ui', self) # Load the .ui file
        _translate = QtCore.QCoreApplication.translate
        self.Upload_image_label= self.findChild(QLabel, 'Upload_image_label')
        self.Upload_image_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\"src/image/upload.png\"/></p></body></html>"))
        self.setAcceptDrops(True)
        self.import_image_label = self.findChild(QLabel, 'import_image_label') # Find the button
        self.return_button = self.findChild(QPushButton, 'return_button')
        self.return_button.clicked.connect(self.return_button_func)

        #\ create the loading animation
        self.LoadingAnimation = LoadingScreen()
        # self.create_animation_QThread()

        #\ set the page to 0
        self.stackedWidget = self.findChild(QStackedWidget, 'stackedWidget')
        self.stackedWidget.setCurrentIndex(0)

        #\ central widget
        wid = self.findChild(QWidget, "import_page_widget")


        #\ Flag
        #\ for the first time to build the layout
        self.first_build_flag = True


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



    #\ Create QThred for loading animation
    def create_animation_QThread(self):
        #\ create QThread object
        self.thread = QThread()

        #\ create worker object
        self.worker = QThread_Worker()

        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.worker.stop)



    #\ Import image Button
    def Import_button_func(self):

        #\ file to import
        fname = QFileDialog.getOpenFileNames(self, 'Open file',os.getcwd(),"Image files (*.jpg *.png)")
        print(f"image : {fname[0]}")
        print(f"image type : {fname[1]}")
        self.files = fname[0]

        # #\ Move worker to the thread
        # self.worker.moveToThread(self.thread)

        # # Start the thread
        # self.thread.start()

        #\ build the result page
        self.build_result_page()



    #\ return to the first import page
    def return_button_func(self, event):
        # self.image_result_frame_layout.deleteLater()
        # self.image_result_frame_layout.destroyed()
        for i in range(self.picture_total_num):
            self.image_result_frame_layout.removeWidget(self.result_frame_layout_list[i])
        self.stackedWidget.setCurrentIndex(0)



    #\ drag image into the GUI
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


    #\ drag image into the GUI
    def dropEvent(self, event):
        #\ file to import
        self.files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in self.files:
            print(f"image file : {f}")


        #\ Move worker to the thread
        self.worker.moveToThread(self.thread)

        # #\ run the loading animation
        # self.thread.start()

        # #\ go to next page
        # self.build_result_page()




    #\ build the reult page
    def build_result_page(self):

        #\ start the building page
        if len(self.files) !=  0:
            #\ change page
            self.stackedWidget.setCurrentIndex(1)

            #\ Same Y position6
            result_widget_Y = (self.frameGeometry().height()-Index.result_frame_height)/2

            #\ build a layout to form the result frame
            if self.first_build_flag == True:
                self.result_frame_layout = QHBoxLayout()

            self.result_page = self.findChild(QWidget, "Result_Page")
            self.result_widget = []
            self.picture_total_num = len(self.files)

            #\ do the api first since this takes most of the times
            self.quality = []
            self.quality_ugc = []
            self.API_response(self.picture_total_num+1)

            #\ thread end
            # print("end of the loading animation thread~")
            # self.worker.stop()

            #\
            self.result_frame_layout_list = []
            for num in range(1, self.picture_total_num+1, 1):
                #\ change the X position
                result_widget_X = self.frameGeometry().width() * num / (self.picture_total_num + 1) - Index.result_frame_width / 2
                self.result_widget_construct(result_widget_X,
                                            result_widget_Y,
                                            self.result_page,
                                            num,
                                            self.files[num-1])

                #\ add the widget to the lower frame layout
                self.result_frame_layout.addWidget(self.image_result_frame)
                self.result_frame_layout_list.append(self.image_result_frame)
        else:
            print("[Warning] No import file or wrong file type")
            self.infoDialog("Import file or wrong file type ", "warning")

        #\ add the layout to the lower frame
        self.lower_frame = self.findChild(QFrame, 'lower_frame')
        self.upper_frame = self.findChild(QFrame, 'upper_frame')
        self.lower_frame.setLayout(self.result_frame_layout)

        #\ set the page layout again
        if self.first_build_flag == True:
            self.image_result_frame_layout = QVBoxLayout()

        self.image_result_frame_layout.addWidget(self.upper_frame)
        self.image_result_frame_layout.addWidget(self.lower_frame)
        self.image_result_frame.setLayout(self.image_result_frame_layout)

        #\ disable the flag which set for the initialization
        self.first_build_flag = False





    #\ Info Dialog
    def infoDialog(text, title):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)


    #\ result widget
    def result_widget_construct(self, X:int, Y:int, frame:QFrame, number:int, image_path:str):
        """
        Description:
            The result widget that include image and table
            +--higher frame------------------------------------ ...
            |                                   +----------+
            |                                   |  button  | .....
            |                                   +----------+
            +--lower frame-------------------------------------- ....
            |   +---frame---------------+       +------...
            |   |                      Q|       |
            |   |        IMAGE         B|       |
            |   |       (QLabel)       O|       |
            |   |                      X|       |
            |   |______________________L|  ...  |
            |   |       TABLE          A|       |
            |   |      | (H01)         Y|       |
            |   | -----+-------------- O|       |
            |   | (H10)|               U|       |
            |   | (H20)|               T|       |
            |   | (H30)|                |       |
            |   +-----------------------+       +------ ...
            +-------------------------------------------- ....

        Args:
            X : widget horizontal position
            Y : widget vertical position
            frame : the frame that this widget will build on
            number : how many widget needs to create and give it the different name
        """
        #\ --Frame--
        self.image_result_frame = QFrame(frame)
        self.image_result_frame.setGeometry(QtCore.QRect(X, Y, Index.result_frame_width, Index.result_frame_height))
        self.image_result_frame.setFrameShape(QFrame.StyledPanel)
        self.image_result_frame.setFrameShadow(QFrame.Raised)
        self.image_result_frame.setObjectName("image_result_frame_" + str(number))


        #\ --Image label--
        self.image = QLabel(self.image_result_frame)
        self.image_path = image_path
        pixmap = QtGui.QPixmap(self.image_path)
        pixmap_resize = pixmap.scaled(Index.result_image_width, Index.result_image_height, QtCore.Qt.IgnoreAspectRatio)
        self.image.setPixmap(pixmap_resize)


        #\ --Table--
        self.table = QTableWidget(4, 1, self.image_result_frame)
        print(Index.result_horizontal_table_header(number))
        self.table.setHorizontalHeaderLabels([Index.result_horizontal_table_header(number)])
        self.table.setVerticalHeaderLabels(Index.result_vertical_table_header)
        self.table.setMaximumWidth(Index.result_frame_width)
        self.Table_content(number)


        #\ --layout in the frame--
        #\ Add the vertical Boxlayout
        if self.first_build_flag == True:
            self.layout = QVBoxLayout()

        #\ Add the widhet
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.table)
        self.image_result_frame.setLayout(self.layout)








    #\ Description:
    #\     use the API here
    #\     https://labs.everypixel.com/api/docs
    def API_response(self, picture_total_num):
        authorization = (Index.client_id, Index.client_secret)
        for num in range(1, picture_total_num, 1):
            #\ quality
            with open(self.files[num-1], 'rb') as image:
                data = {'data': image}
                self.quality.append(requests.post('https://api.everypixel.com/v1/quality', files=data, auth=authorization).json())
            #\ quality_ugc
            with open(self.files[num-1], 'rb') as image:
                data = {'data': image}
                self.quality_ugc.append(requests.post('https://api.everypixel.com/v1/quality_ugc', files=data, auth=authorization).json())





    #\ create table and insert the element with the response from api
    def Table_content(self, num):
        #\ quality
        if self.quality[num-1]["status"] == "ok":
            self.table.setItem(0,0,QTableWidgetItem(str(round(100*self.quality[num-1]["quality"]["score"], 2)) + "%"))
        else :
            print(f"quality response problem : {self.quality}")

        #\ quality_ugc
        if self.quality_ugc[num-1]["status"] == "ok":
            self.table.setItem(1,0,QTableWidgetItem(str(100*round(self.quality_ugc[num-1]["quality"]["score"], 2)) + "%"))
            self.table.setItem(2,0,QTableWidgetItem(Index.quality_ugc_class_TF[self.quality_ugc[num-1]["quality"]["class"]]))
        else:
            print(f"quality ugc response problem : {self.quality_ugc}")

            #\ keyword
            # keywords = requests.post('https://api.everypixel.com/v1/keywords', files=data, auth=authorization).json()
            # self.table.setItem(3,0,QTableWidgetItem(keywords))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())