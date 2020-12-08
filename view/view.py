from PyQt5 import QtWidgets, QtCore

from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        self.connectSignals()

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit()

    def startSimulation(self):
        i = 1
        #self.stackedWidget.setCurrentWidget(self.simulatorWidget)

    def updateScene(self, scene):
        self.graphicsView_2.setScene(scene)
        #self.graphicsView.fitInView(0, 0, 1000, 1000)

