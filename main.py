import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from presenter.presenter import Presenter


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    presenter = Presenter()
    presenter.ui.show()

    sys.exit(app.exec_())