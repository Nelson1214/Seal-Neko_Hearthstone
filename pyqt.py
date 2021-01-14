import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QScrollArea,
)

class Window(QWidget):
    def __init__(self, heroList):
        super().__init__()
        self.setWindowTitle("HearthStone")
        self.heroCount = len(heroList)
        mainLayout = QHBoxLayout()
        self.setLeftPanel(mainLayout)
        
    def setLeftPanel(self, mainLayout):
        heroVertical = QVBoxLayout()
        widthCount = int(self.heroCount % 3)
        heightCount = int((self.heroCount - widthCount) / 3)
        print(heightCount)
        for i in range(heightCount):
            heroHorizonal = QHBoxLayout()
            for j in range(3):
                heroButton = QPushButton(str(3 * i + j))
                heroHorizonal.addWidget(heroButton)
            heroVertical.addLayout(heroHorizonal)
        mainLayout.addLayout(heroVertical)
        heroHorizonal = QHBoxLayout()
        heroButton = QPushButton('')
        heroHorizonal.addWidget(heroButton)
        heroHorizonal.addStretch(2)
        heroVertical.addLayout(heroHorizonal)
        # Set the layout on the application's window
        self.setLayout(mainLayout)

def createView(heroList):
    app = QApplication(sys.argv)
    window = Window(heroList)
    window.show()
    sys.exit(app.exec_())
    