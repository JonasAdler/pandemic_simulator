import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from presenter.presenter import Presenter


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QtGui.QIcon("./resources/virusIcon.png"))
    app.setApplicationDisplayName("Simulator")

    presenter = Presenter()
    presenter.ui.show()

    sys.exit(app.exec_())