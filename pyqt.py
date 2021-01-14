import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QLabel,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self, heroList):
        super().__init__()
        self.setWindowTitle("HearthStone")
        self.heroList = heroList
        self.heroCount = len(heroList)
        self.mainLayout = QHBoxLayout()
        self.setLeftPanel()
        self.setRightPanel()
        self.setLayout(self.mainLayout)
        
    def setLeftPanel(self):
        heroScroll = QScrollArea()
        heroVertical = QVBoxLayout()
        heroHorizonal = QHBoxLayout()
        for index, hero in enumerate(self.heroList):
            if (index % 3 == 0):
                heroHorizonal = QHBoxLayout()
                heroVertical.addLayout(heroHorizonal)
            heroButton = QPushButton(hero.get_name())
            heroButton.clicked.connect(lambda ch, hero=hero : self.setDetail(hero.get_id()))
            heroButton.setIcon(QIcon("./hs/" + str(hero.get_id()) + ".png")) 
            heroHorizonal.addWidget(heroButton)
        heroScroll.setLayout(heroVertical)
        heroScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        heroScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        heroScroll.setWidgetResizable(False)
        heroScroll.setFixedWidth(400)
        self.mainLayout.addWidget(heroScroll)

    def setRightPanel(self):
        dataVertical = QVBoxLayout()
        self.heroNameLabel = QLabel("Name : ")
        self.getPickRateLabel = QLabel("Pick rate : ")
        self.popularityLabel = QLabel("Popularity : ")
        dataVertical.addWidget(self.heroNameLabel)
        dataVertical.addWidget(self.getPickRateLabel)
        dataVertical.addWidget(self.popularityLabel)
        self.mainLayout.addLayout(dataVertical)

    def setDetail(self, hero_id):
        currentHero = None
        for hero in self.heroList:
            if (hero.get_id() == hero_id):
                currentHero = hero
                break
        self.heroNameLabel.setText("Name : " + currentHero.get_name())
        self.getPickRateLabel.setText("Pick rate : " + str(currentHero.get_pick_rate()))
        self.popularityLabel.setText("Popularity : " + str(currentHero.get_popularity()))
        return


def createView(heroList):
    app = QApplication(sys.argv)
    window = Window(heroList)
    window.show()
    sys.exit(app.exec_())
    