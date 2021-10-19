import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
# GUI
from PyQt5 import QtWidgets, uic, QtGui
import sys
import os


class Plot:
    counter = 0

    def __init__(self, m=None, n=None, x1=None, y1=None, x2=None, y2=None):
        self.__class__.counter += 1
        self.x = np.arange(-5, 5, 0.1)
        self.m = m
        self.n = n
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.label = None

        self.calculateY()


    def setColor(self, color):
        self.color = color

    def calculateY(self):
        if not(self.m is None):
            self.calculateWithEq()
            self.addLabelEq()

        if not(self.x1 is None):
            self.calculateWithPoints()
            self.addLabelPoi()

    def calculateWithEq(self):
        self.y = self.m * self.x + self.n

    def calculateWithPoints(self):
        pass

    def addLabelEq(self):
        self.label = f'f{self.counter}(x) = {self.m}x + {self.n} '

    def addLabelPoi(self):
        pass

# GUI
class Ui_MainWindow(QtWidgets.QMainWindow):

    """This is the class of the Graphical User Interface.
    - Style is loaded from UI file, which is generated with qt designer
    - don't touch the ui file, make your changes here

    Attributes:
        config (Config): is a Config-Element
        sm_byte (int): offset of byte which defines role of sps (master or slave)
    """

    def __init__(self):
        """initiates the gui
        - calls the __init__ method of QtWidgets.QMainWindow
        - loads style from ui file
        - shows name of bin-file which has to be generated

        - define methods/function of buttons
        """
        # Call the inherited classes __init__ method
        super(Ui_MainWindow, self).__init__()
        uic.loadUi("./school_function_drawer.ui", self)  # Load the .ui file
        # self.setWindowIcon(QtGui.QIcon(os.path.join("ressources", "logo.png")))
        self.setFixedSize(self.window().width(), self.window().height())
        # self.display_bin_file.setText(f"/{bin_name}")

        # buttons
        self.butAddLinEq.clicked.connect(self.addLinEq)
        self.butAddLinPoi.clicked.connect(self.addLinPoi)
        self.butPlot.clicked.connect(self.plot)
        self.butRefresh.clicked.connect(self.refreshPlot)

        # menubar
        # self.action_exit.triggered.connect(lambda: self.close())

        self.plots = []
        self.ax = None

        self.refreshPlot()

    def refreshPlot(self):
        self.y = []

    def refreshAxes(self):
        # set plot settings
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])

        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_position(('data',0))
        self.ax.spines['bottom'].set_position(('data',0))
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')


    def plot(self):
        self.refreshAxes()

        if len(self.y) == 0:
            return

        self.defineColors()
        for i in self.y:
            print(i.x,i.y,i.color)
            self.ax.plot(i.x, i.y, color=i.color,label=i.label)

        plt.legend(frameon=True)
        plt.show()

    def defineColors(self):
        self.cmap = get_cmap("viridis", len(self.y))
        for i in range(len(self.y)):
            self.y[i].setColor(self.cmap(i))

    def addLinEq(self):
        m = self.txtEqM.text()
        try:
            m = float(m.replace(',','.'))
        except:
            self.txtEqM.setText("")
            return

        n = self.txtEqN.text()
        try:
            n = float(n.replace(',','.'))
        except:
            self.txtEqN.setText("")
            return

        self.y.append(Plot(m=m, n=n))

    def addLinPoi(self):
        pass


if __name__ == '__main__':                                      # for starting

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Ui_MainWindow()
    MainWindow.show()

    sys.exit(app.exec_())
