import sys 
import os 
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from pydub import AudioSegment
from PyQt5.QtWidgets import QPushButton, QStyleFactory
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HBS - WAV to MP3 Converter")
        self.setGeometry(100, 100, 500, 300)

        # "Select File" 버튼 생성
        select_file_btn = QPushButton("Select File", self)
        select_file_btn.setGeometry(50, 50, 100, 30)
        select_file_btn.clicked.connect(self.select_file)

        # "Convert" 버튼 생성
        convert_btn = QPushButton("Convert", self)
        convert_btn.setGeometry(200, 50, 100, 30)
        convert_btn.clicked.connect(self.convert)

        # "Clear" 버튼 생성
        clear_btn = QPushButton("Clear", self)
        clear_btn.setGeometry(350, 50, 100, 30)
        clear_btn.clicked.connect(self.clear)

    def select_file(self):
        # WAV 파일 선택
        options = QFileDialog.Options()

        file_name, _ = QFileDialog.getOpenFileName(self, "Select WAV file", "", "WAV files (*.wav)", options=options)

        if file_name:
            # 선택된 WAV 파일 경로 저장
            self.wav_path = file_name
        else:
            # WAV 파일 선택 취소
            self.wav_path = ""

    def convert(self):
        if not hasattr(self, "wav_path"):
            # WAV 파일 선택 안됨
            #QMessageBox.warning(self, "Error", "Please select a WAV file first.")
            self.show_warning()
            return

        # MP3 파일 경로
        mp3_path = os.path.splitext(self.wav_path)[0] + ".mp3"

        # WAV 파일 로드
        audio_segment = AudioSegment.from_wav(self.wav_path)

        # MP3 파일로 저장
        audio_segment.export(mp3_path, format="mp3")

        # 완료 메시지 출력
        QMessageBox.information(self, "Conversion complete", f"{self.wav_path} was successfully converted to {mp3_path}")

        # WAV 파일 경로 초기화
        self.wav_path = ""

        if os.path.exists(mp3_path):
            # MP3 파일 삭제
            os.remove(mp3_path)

    def clear(self):
        # WAV 파일 경로 초기화
        self.wav_path = ""

        # MP3 파일 경로 삭제
        mp3_path = os.path.splitext(self.wav_path)[0] + ".mp3"
        if os.path.exists(mp3_path):
            os.remove(mp3_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    while True:
        app.processEvents()
