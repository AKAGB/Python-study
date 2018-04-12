import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
    QPushButton, QTextEdit, QTextBrowser,
    QHBoxLayout, QVBoxLayout)
from youdao import Translator

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.translator = Translator()

    def initUI(self):
        # 创建组件
        self.trans_btn = QPushButton('翻译', self)     # 翻译按钮
        self.text_input = QTextEdit(self)             # 输入框
        self.text_output = QTextBrowser(self)        # 输出框
        
        self.set_main_layout()

        # 读取样式表
        with open('window.qss', 'r') as q:
            self.setStyleSheet(q.read())

        # 绑定事件
        self.trans_btn.clicked.connect(self.trans_clicked)

        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('翻译程序')
        self.show()

    def trans_clicked(self):
        """点击按钮时触发"""
        str_input = self.text_input.toPlainText()
        result = self.translator.translate(str_input)
        self.text_output.setText(result)

    def set_main_layout(self):
        """设置主布局"""
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(self.trans_btn)
        hbox.addStretch(1)

        hbox2.addStretch(1)
        hbox2.addWidget(self.text_input)
        hbox2.addStretch(1)
        hbox2.addWidget(self.text_output)
        hbox2.addStretch(1)

        # 添加垂直布局
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        # 设置主布局为垂直布局
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())