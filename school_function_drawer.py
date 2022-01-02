import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
# GUI
from PyQt5 import QtWidgets, uic, QtGui
import sys
import os
# import own Files
from functions import *

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
        self.butAddQuadPoi.clicked.connect(self.addQuadPoi)
        self.butAddQuadEq_1.clicked.connect(self.addQuadEq_1)
        self.butAddQuadEq_2.clicked.connect(self.addQuadEq_2)

        # menubar
        # self.action_exit.triggered.connect(lambda: self.close())

        self.plots = []
        self.ax = None

        self.refreshPlot()

    def refreshPlot(self):
        self.y = []

    def refreshAxes(self):
        # set plot settings
        self.fig, self.ax = plt.subplots(figsize=(16,9))

        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])

        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_position(('data',0))
        self.ax.spines['bottom'].set_position(('data',0))
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        self.ax.set_xticks(range(-5,6))
        self.ax.set_yticks(range(-5,6))
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        self.ax.grid(True)


    def plot(self):
        self.refreshAxes()

        if len(self.y) == 0:
            return

        self.defineColors()
        for i in self.y:
            # print(i.x,i.y,i.color)
            self.ax.plot(i.x, i.y, color=i.color,label=i.label)

        if self.legend_activated.isChecked():
            plt.legend(frameon=True, fontsize=12)
            
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

        self.y.append(LinearPlot(m=m, n=n))

    def addLinPoi(self):
        x1 = self.txtLinPoiX1.text()
        y1 = self.txtLinPoiY1.text()
        x2 = self.txtLinPoiX2.text()
        y2 = self.txtLinPoiY2.text()

        try:
            x1 = float(x1.replace(',','.'))
        except:
            self.txtLinPoiX1.setText("")
            return
        try:
            y1 = float(y1.replace(',','.'))
        except:
            self.txtLinPoiY1.setText("")
            return
        try:
            x2 = float(x2.replace(',','.'))
        except:
            self.txtLinPoiX2.setText("")
            return
        try:
            y2 = float(y2.replace(',','.'))
        except:
            self.txtLinPoiY2.setText("")
            return

        self.y.append(LinearPlot(x1=x1, x2=x2, y1=y1, y2=y2))

    def addQuadEq_1(self):
        a = self.txtEqA.text()
        try:
            a = float(a.replace(',','.'))
        except:
            self.txtEqA.setText("")
            return

        b = self.txtEqB.text()
        try:
            b = float(b.replace(',','.'))
        except:
            self.txtEqB.setText("")
            return

        c = self.txtEqC.text()
        try:
            c = float(c.replace(',','.'))
        except:
            self.txtEqC.setText("")
            return

        self.y.append(QuadPlot(a=a, b=b, c=c))

    def addQuadEq_2(self):
        d = self.txtEqD.text()
        try:
            d = float(d.replace(',','.'))
        except:
            self.txtEqD.setText("")
            return

        e = self.txtEqE.text()
        try:
            e = float(e.replace(',','.'))
        except:
            self.txtEqE.setText("")
            return

        f = self.txtEqF.text()
        try:
            f = float(f.replace(',','.'))
        except:
            self.txtEqF.setText("")
            return

        self.y.append(QuadPlot(d=d, e=e, f=f))

    def addQuadPoi(self):
        x1 = self.txtQuadPoiX1.text()
        y1 = self.txtQuadPoiY1.text()
        x2 = self.txtQuadPoiX2.text()
        y2 = self.txtQuadPoiY2.text()
        x3 = self.txtQuadPoiX3.text()
        y3 = self.txtQuadPoiY3.text()
        
        try:
            x1 = float(x1.replace(',','.'))
        except:
            self.txtQuadPoiX1.setText("")
            return
        try:
            y1 = float(y1.replace(',','.'))
        except:
            self.txtQuadPoiY1.setText("")
            return
        try:
            x2 = float(x2.replace(',','.'))
        except:
            self.txtQuadPoiX2.setText("")
            return
        try:
            y2 = float(y2.replace(',','.'))
        except:
            self.txtQuadPoiY2.setText("")
            return
        try:
            x3 = float(x3.replace(',','.'))
        except:
            self.txtQuadPoiX3.setText("")
            return
        try:
            y3 = float(y3.replace(',','.'))
        except:
            self.txtQuadPoiY3.setText("")
            return

        self.y.append(QuadPlot(x1=x1, x2=x2, x3=x3, y1=y1, y2=y2, y3=y3))

if __name__ == '__main__':                                      # for starting

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Ui_MainWindow()
    MainWindow.show()

    sys.exit(app.exec_())
