import sys
from PyQt5.QtWidgets import (QWidget, QApplication, 
    QPushButton, QTextEdit, QTextBrowser, QGridLayout, )
from youdao import Translator

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.initUI()

    def initUI(self):
        # 创建网格布局
        grid = QGridLayout()
        grid.setSpacing((20))

        # 创建组件
        self.trans_btn = QPushButton('翻译', self)     # 翻译按钮       
        self.text_input = QTextEdit(self)             # 输入框
        self.text_output = QTextBrowser(self)        # 输出框

        # 布局
        grid.addWidget(self.trans_btn, 0, 0)
        grid.addWidget(self.text_input, 1, 0, 1, 1)
        grid.addWidget(self.text_output, 1, 1, 1, 1)

        self.setLayout(grid)

        # 绑定事件
        self.trans_btn.clicked.connect(self.trans_clicked)

        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('翻译程序')
        self.show()
    
    def trans_clicked(self):
        str_input = self.text_input.toPlainText()
        result = self.translator.translate(str_input)
        self.text_output.setText(result)

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()