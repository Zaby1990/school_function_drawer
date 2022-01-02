import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from abc import abstractmethod

class Function():
    counter=0    
    def __init__(self):
        self.x = np.arange(-5, 5, 0.1)
        self.__class__.counter += 1

    def setColor(self, color):
        self.color = color

    @abstractmethod
    def calculateY(self):
        pass

class QuadPlot(Function):
    counter = 0

    def __init__(self, a=None, b=None, c=None, d=None, e=None, f=None, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.label = None

        self.calculateY()

    def calculateY(self):
        if not((self.a is None) or (self.b is None) or (self.c is None)):
            self.calculateWithEq1()
            self.addLabel1()

        elif not((self.d is None) or (self.e is None) or (self.f is None)):
            self.calculateWithEq2()
            self.addLabel2()

        elif not((self.x1 is None) or (self.x2 is None) or (self.x3 is None) or (self.y1 is None) or (self.y2 is None) or (self.y3 is None)):
            done = self.calculateWithPoints()
            if done:
                self.addLabel1()

        else:
            return

    def addLabel1(self):
        self.label = f'f{self.counter}(x) = {self.a:1.3f}x² + {self.b:1.3f}x + {self.c:1.3f}'

    def addLabel2(self):
        self.label = f'f{self.counter}(x) = {self.d:1.3f}(x + {self.e:1.3f})² + {self.f:1.3f}'

    def calculateWithEq1(self):
        self.y = self.a * (self.x)**2 + self.b * self.x + self.c

    def calculateWithEq2(self):
        self.y = self.d  * ( self.x + self.e)**2 + self.f

    def calculateWithPoints(self):
        try:
            i = (self.y2 - self.y1) / (self.x2**2 - self.x1**2)
            ii = (self.y3 - self.y2) / (self.x3**2 - self.x2**2)
            iii = 1 / (self.x2 + self.x1)
            iv = 1 / (self.x3 + self.x2)

            self.b = (i - ii) / (iii - iv)
            self.a = ii - self.b * iv
            self.c = self.y1 - self.a * self.x1**2 - self.b * self.x1

        except Exception as e:
            print("nicht lösbar")
            print(e)
            return False

        self.calculateWithEq1()
        return True

class LinearPlot(Function):
    counter = 0

    def __init__(self, m=None, n=None, x1=None, y1=None, x2=None, y2=None):
        super().__init__()
        self.m = m
        self.n = n
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.label = None

        self.calculateY()

    def calculateY(self):
        if not((self.m is None) & (self.n is None)):
            self.calculateWithEq()

        if not((self.x1 is None) & (self.x2 is None) & (self.y1 is None) & (self.y2 is None)):
            self.calculateWithPoints()

        self.addLabel()
    def calculateWithEq(self):
        self.y = self.m * self.x + self.n

    def calculateWithPoints(self):
        self.m = (self.y2-self.y1)/(self.x2-self.x1)
        self.n = self.y1 - self.m * self.x1

        self.calculateWithEq()

    def addLabel(self):
        self.label = f'f{self.counter}(x) = {self.m:1.3f}x + {self.n:1.3f} '

    # def addLabel(self):
        # pass

class RootPlot(Function):
    # y = a * (b*x+f)^(c/d) + e
    counter=0

    def __init__(self, a=1, b=1, c=1, d=2, e=0,f=0):
        super().__init__()
        self.x = np.arange((0-f), 5, 0.01)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.label = None

        self.calculateY()

    def addLabel(self):
        if self.a == 1:
            label_a = ""
        else:
            label_a = f"{self.a:1.3f}"

        if self.b == 1:
            label_b = ""
        else:
            label_b = f"{self.b:1.3f}"

        if self.c == 1:
            label_c = "1"
        else:
            label_c = f"{self.c:1.3f}"

        if self.d == 2:
            label_d = "2"
        else:
            label_d = f"{self.d:1.3f}"

        if self.e == 0:
            label_e = ""
        else:
            label_e = f"{self.e:1.3f}"

        if self.f == 0:
            label_f = ""
        else:
            label_f = f"{self.f:1.3f}"

        self.label = f'f{self.counter}(x) = {label_a}({label_b}x+{label_f})^(label_c) + {self.n:1.3f} '

    def calculateY(self):
        self.y = self.a * (self.b*self.x+self.f)**(self.c/self.d) + self.e

class AbsPlot(Function):
    # y = m*|x|+n  maybe cound be changed to more difficulty
    counter=0

    def __init__(self, m=1, n=0):
        super().__init__()
        self.m = m
        self.n = n

        self.calculateY()

    def addLabel(self):
        if self.n == 0:
            label_n = ""
        else:
            label_n = f"{self.n:1.3f}"

        if self.m == 1:
            label_m = ""
        else:
            label_m = f"{self.m:1.3f}"

        self.label = f'f{self.counter}(x) = {label_m}|x| + {self.n}'

    def calculateY(self):
        self.y = self.m * np.abs(self.x) + self.n

class ExpPlot(Function):
    # y = a*(x+b) + c  
    counter=0

    def __init__(self, a=1, b=0,c=0):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

        self.calculateY()

    def addLabel(self):
        if self.a.type() == int:
            label_a = f"{self.a:d}"
        else:
            label_a = f"{self.a:1.3f}"

        if self.b == 0:
            label_b = ""
        else:
            label_b = f"{self.b:1.3f}"

        if self.c == 0:
            label_c = ""
        else:
            label_c = f"{self.c:1.3f}"

        self.label = f'f{self.counter}(x) = {label_a}^(x) - {self.c}'
        print("warning, label exp plot has to be redefined!")

    def calculateY(self):
        self.y = self.a ** (self.x+self.b) + self.c


if __name__ == "__main__":
    plots=[]

    class sonder(Function):
        def __init__(self):
            super().__init__()
            self.x =np.arange(-5,5,0.01)
            self.y = -2/(self.x+3)

    plots.append(LinearPlot(2,3))
    plots.append(QuadPlot(e=-2,d=1,f=-3))
    plots.append(RootPlot(f=1))
    plots.append(AbsPlot())
    plots.append(ExpPlot(2,0,-3))
    plots.append(sonder())




    # set plot settings
    fig, ax = plt.subplots(figsize=(16,9))

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data',0))
    ax.spines['bottom'].set_position(('data',0))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(range(-5,6))
    ax.set_yticks(range(-5,6))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    ax.grid(True)

    cmap = get_cmap("viridis", len(plots))
    for i in range(len(plots)):
        plots[i].setColor(cmap(i))
    for i in plots:
        ax.plot(i.x, i.y,color=i.color)

    plt.show()

