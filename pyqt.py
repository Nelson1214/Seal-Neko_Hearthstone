# import sys

# from PyQt5.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QPushButton,
#     QWidget,
#     QVBoxLayout,
#     QScrollArea,
# )

# class Window(QWidget):
#     def __init__(self, heroList):
#         super().__init__()
#         self.setWindowTitle("HearthStone")
#         self.heroCount = len(heroList)
#         mainLayout = QHBoxLayout()
#         self.setLeftPanel(mainLayout)
        
#     def setLeftPanel(self, mainLayout):
#         heroVertical = QVBoxLayout()
#         widthCount = int(self.heroCount % 3)
#         heightCount = int((self.heroCount - widthCount) / 3)
#         print(heightCount)
#         for i in range(heightCount):
#             heroHorizonal = QHBoxLayout()
#             for j in range(3):
#                 heroButton = QPushButton(str(3 * i + j))
#                 heroHorizonal.addWidget(heroButton)
#             heroVertical.addLayout(heroHorizonal)
#         scrollArea = QScrollArea()
#         scrollArea.setWidget(heroVertical)
#         mainLayout.addWidget(scrollArea)
#         # mainLayout.addLayout(heroVertical)
#         heroHorizonal = QHBoxLayout()
#         heroButton = QPushButton('')
#         heroHorizonal.addWidget(heroButton)
#         heroHorizonal.addStretch(2)
#         heroVertical.addLayout(heroHorizonal)
#         # Set the layout on the application's window
#         self.setLayout(mainLayout)

# def createView(heroList):
#     app = QApplication(sys.argv)
#     window = Window(heroList)
#     window.show()
#     sys.exit(app.exec_())
from PySide2 import QtCore, QtWidgets
from functools import partial

class Test:
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.mainWidget = QtWidgets.QWidget()
        self.lights = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.window.setCentralWidget(self.mainWidget)

    def light_label_event(self, name, checked):
        print(name,checked)

    def populate_lights(self):
        self.light_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        for light in self.lights:
            light_label = QtWidgets.QPushButton(light)
            light_label.setCheckable(True)
            light_label.toggled.connect(partial(self.light_label_event,light))
            self.light_layout.addWidget(light_label)
        self.light_layout.addStretch()

    def light_palette_ui(self):
        self.vertical_layout_main = QtWidgets.QVBoxLayout(self.mainWidget)
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.vertical_layout_main.addWidget(self.scroll)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll_widget = QtWidgets.QWidget()
        self.scroll.setWidget(self.scroll_widget)

        self.populate_lights()        
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.window.show() 


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    t = Test()
    t.light_palette_ui()
    sys.exit(app.exec_())