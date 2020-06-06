import threading

from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsDropShadowEffect


class GUI(threading.Thread, QWidget):

    def __init__(self):
        QWidget.__init__(self)
        threading.Thread.__init__(self)

        self.setFixedSize(480, 500)
        self.setStyleSheet("background-color:#000000")
        self.label_animation = QLabel(self)

        self.movie = QMovie('jarvis.gif')
        self.label_animation.setMovie(self.movie)

        self.time = QLabel(self)
        self.time.setAlignment(Qt.AlignCenter)
        self.time.resize(350, 250)
        self.time.setStyleSheet("color: #00BFFF;background-color:transparent;font:80px;font-weight: bold")
        self.time.move(70, 280)

        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#ffffff"))
        self.shadow_effect.setOffset(1, 1)

        self.time.setGraphicsEffect(self.shadow_effect)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.movie.start()
        self.show()

        self.show_time()

    def show_time(self):
        current_time = QTime.currentTime()
        text = current_time.toString('hh:mm:ss')
        self.time.setText(text)
