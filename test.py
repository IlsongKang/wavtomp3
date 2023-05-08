from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPalette, QColor

app = QApplication([])
dialog = QFileDialog()
# 파일 선택 대화상자의 배경색을 노란색으로 변경
# dialog.setStyleSheet("QFileDialog { background-color: %s }")

options = QFileDialog.Options()
#options |= QFileDialog.DontUseNativeDialog
fileName, _ = QFileDialog.getOpenFileName(None, "Select file", "", "All Files (*);;WAV Files (*.wav)", options=options)






