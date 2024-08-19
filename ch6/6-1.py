from PyQt5.QtWidgets import *
import sys
import winsound

class BeepSound(QMainWindow):  # 클래스 선언
    def __init__(self) :  # 생성자 함수
        super().__init__()
        self.setWindowTitle('삑 소리 내기') 		# 윈도우 이름과 위치 지정
        self.setGeometry(200,200,500,100)  # x,y,w,h

        shortBeepButton=QPushButton('짧게 삑',self)	# 버튼 생성
        longBeepButton=QPushButton('길게 삑',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다!',self)  # init 함수 안에서만 사용하는 게 아니라면 self 반드시 붙여줘야 함(다른 메서드에서도 사용된다)
        
        shortBeepButton.setGeometry(10,10,100,30)	# 버튼 위치와 크기 지정
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210,10,100,30)
        self.label.setGeometry(10,40,500,70)
        
        shortBeepButton.clicked.connect(self.shortBeepFunction) # 콜백 함수 지정
        longBeepButton.clicked.connect(self.longBeepFunction)         
        quitButton.clicked.connect(self.quitFunction)
       
    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')   
        winsound.Beep(1000,500)  # 500ms
        
    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다.')        
        winsound.Beep(1000,3000) 
                
    def quitFunction(self):
        self.close()
                
app=QApplication(sys.argv) 
win=BeepSound()  # 클래스 생성
win.show()
app.exec_()