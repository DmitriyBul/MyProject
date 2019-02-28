import sys
from PyQt5.QtWidgets import QApplication, QWidget
import time
from threading import Thread
from PyQt5.QtCore import QCoreApplication
    
def fun1():
    sec = 0
    for i in range(10):
        time.sleep(1)
        sec += 1
        print(sec)
    
def windget_creation():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    while(True):
        t1 = Thread(target=fun1)
        t2 = Thread(target=windget_creation)

        t1.start()
        t2.start()
        t1.join()
    
        print("dome")