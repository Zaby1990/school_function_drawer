import numpy as np
import matplotlib.pyplot as plt


class QuadPlot:
    counter = 0

    def __init__(self, a=None, b=None, c=None, d=None, e=None, f=None, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None):
        self.__class__.counter += 1
        self.x = np.arange(-5, 5, 0.1)
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

    def setColor(self, color):
        self.color = color

if __name__ == '__main__':
    # test

    a = QuadPlot(a=1, b=2, c=3)

    b = QuadPlot(d=2, e=-3, f=3)

    c = QuadPlot(x1=1.5, y1=-1, x2=1, y2=0, x3=2, y3=0)
    # plt.plot(a.x, a.y)
    plt.plot(b.x, b.y)
    plt.plot(c.x, c.y)
    plt.gca().grid()

    plt.show()
