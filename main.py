import sys
from kiwoom.kiwoom import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class Main():
    def __init__(self):
        self.app = QApplication(sys.argv) # QApplication 객체 생성.
        self.kiwoom = Kiwoom()
        self.kiwoom.show()
        self.app.exec_() # 이벤트 루프 실행.

if __name__ == "__main__":
    Main()
