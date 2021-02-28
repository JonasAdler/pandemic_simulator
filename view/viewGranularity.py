from PyQt5 import QtWidgets, QtCore

from resources import constVariables
from view.granularityWindow import Ui_Dialog

class ViewGranularityWindow(QtWidgets.QDialog, Ui_Dialog):

    granularitySelectedSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(ViewGranularityWindow, self).__init__()
        self.setupUi(self)

        self.connectSignals()

    def connectSignals(self):
        self.confirmButtonGW.clicked.connect(self.confirmButtonClicked)
        self.cancelButtonGW.clicked.connect(self.cancelButtonClicked)

    def confirmButtonClicked(self):
        self.granularitySelectedSignal.emit(self.granularitySpinBoxGW.value())
        self.close()

    def cancelButtonClicked(self):
        self.close()