import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Greeting_window(QWidget):
        def __init__(self):
                QWidget.__init__(self, None)

                self.num = 0

                layout = QVBoxLayout()

                self.name_label = QLabel("Your Name: ")
                layout.addWidget(self.name_label)

                self.name_entry = QLineEdit()
                layout.addWidget(self.name_entry)

                greeting_button = QPushButton("Go!")
                layout.addWidget(greeting_button)

                self.connect(greeting_button, SIGNAL("clicked()"), self.greeting)

                self.setLayout(layout)

        def greeting(self):
                dialog = QDialog(self)

                layout = QVBoxLayout()

                label = QLabel("Hi " + self.name_entry.text())
                layout.addWidget(label)

                close_button = QPushButton("close window")
                self.connect(close_button, SIGNAL("clicked()"), dialog.close)

                layout.addWidget(close_button)
                dialog.setLayout(layout)

                dialog.show()

def main():
        app = QApplication(sys.argv)

        w = Greeting_window()
        w.show()

        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
        
