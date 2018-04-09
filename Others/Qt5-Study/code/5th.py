"""
创建状态栏
QtWidget.QMainWindow类提供一个应用主窗口，默认创建一个拥有
状态栏、工具栏和菜单栏的经典应用窗口骨架
statusBar()方法返回该主窗口的状态栏对象
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())