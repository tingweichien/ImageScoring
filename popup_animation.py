from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread
import Index

#\loading animation class
class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200,200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)
        self.movie = QMovie(Index.LoadingGif)
        self.label_animation.setMovie(self.movie)


    def startAnimation(self):
        print("start animation")
        self.movie.start()
        self.show()

    def stopAnimation(self):
        self.movie.stop()
        self.close()



#\ worker class for QThread
class QThread_Worker(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.loading_animation = LoadingScreen()

    def run(self):
        print("worker run")
        self.progress.emit()
        self.loading_animation.startAnimation()

    def stop(self):
        print("worker stop")
        self.finished.emit()
        self.loading_animation.stopAnimation()