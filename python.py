import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(200, 200, 400, 200)
        
        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.update_position)
        self.player.mediaStatusChanged.connect(self.update_status)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()

        self.label_song = QLabel("No song selected")
        layout.addWidget(self.label_song)
        
        self.button_open = QPushButton("Add Music")
        self.button_open.clicked.connect(self.open_file)
        layout.addWidget(self.button_open)
        
        self.button_previous = QPushButton("Previous")
        self.button_previous.clicked.connect(self.play_previous)
        layout.addWidget(self.button_previous)
        
        self.button_play = QPushButton("Play")
        self.button_play.clicked.connect(self.play_pause)
        layout.addWidget(self.button_play)
        
        self.button_next = QPushButton("Next")
        self.button_next.clicked.connect(self.play_next)
        layout.addWidget(self.button_next)
        
        self.setLayout(layout)
        
    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Music (*.mp3 *.wav)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            filename = file_dialog.selectedFiles()[0]
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.label_song.setText(os.path.basename(filename))
        
    def play_pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.button_play.setText("Play")
        else:
            self.player.play()
            self.button_play.setText("Pause")
            
    def play_next(self):
        self.player.playlist().next()
        
    def play_previous(self):
        self.player.playlist().previous()
        
    def update_position(self, position):
        pass
        
    def update_status(self, status):
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = MusicPlayer()
    window.show()
    app.exec_()
