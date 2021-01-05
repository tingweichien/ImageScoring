#\ result module with image label and table

from PyQt5.QtWidgets import QLabel, QTableWidget, QFrame
from PyQt5 import QtCore
import Index

class image_table():
    def __init__(self, X, Y, frame, number):
        self.image_result_frame = QFrame(frame)
        self.image_result_frame.setGeometry(QtCore.QRect(X, Y, 276, 446))
        self.image_result_frame.setFrameShape(QFrame.StyledPanel)
        self.image_result_frame.setFrameShadow(QFrame.Raised)
        self.image_result_frame.setObjectName("image_result_frame_" + number)
        self.image = QLabel(self.image_result_frame)
        self.table = QTableWidget(3, 1, self.image_result_frame)
        self.table.setHorizontalHeaderLabels(Index.result_horisontal_table_header(number))
        self.table.setVerticalHeaderLabels(Index.result_vertical_table_header)