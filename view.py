from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt

class View(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle('My Super Calculator')
        self.setFixedSize(240, 240)


        self.__central_widget = QWidget(self)
        self.setCentralWidget(self.__central_widget)

        self.__general_layout = QVBoxLayout()
        self.__central_widget.setLayout(self.__general_layout)

        self.__create_display()
        self.__create_buttons()

    def __create_display(self):
        self.__display = QLineEdit()
        self.__display.setFixedHeight(36)
        self.__display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.__display.setReadOnly(True)
        self.__general_layout.addWidget(self.__display)

    def __create_buttons(self):
        buttons = {'7': (0,0),
        '8' : (0,1),
        '9' : (0,2), 
        '/' : (0,3),
        '4' : (1,0),

        
        
        }


# minuto 02:10,pero ver desde antes





