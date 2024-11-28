from __future__ import division
import matplotlib.pyplot as plt
from scipy.optimize import root
from math import pi, sin, cos, atan

class Frame:
    def __init__(self, x1, y1, x2, y2, L):
        self.x1, self.y1, self.x2, self.y2, self.L = x1, y1, x2, y2, L
    def eqs(self):
        return [(self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 - self.L**2]
    def plot(self):
        plt.plot([self.x1, self.x2], [self.y1, self.y2], 'ko-')

class Connector:
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def eqs(self):
        return [self.e1.x2 - self.e2.x1, self.e1.y2 - self.e2.y1]
    def plot(self):
        plt.plot([self.e1.x2], [self.e1.y2], 'ro')

class Connector2:
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def eqs(self):
        return [self.e1.x2 - self.e2.x1, self.e1.y2 - self.e2.y1,
                (self.e1.y1 - self.e1.y2) / (self.e1.x1 - self.e1.x2) - (self.e2.y2 - self.e2.y1) / (self.e2.x2 - self.e2.x1)]
    def plot(self):
        plt.plot([self.e1.x2], [self.e1.y2], 'yo')

class System:
    def __init__(self, e):
        self.e = e
    def eqs(self):
        return [eq for ei in self.e for eq in ei.eqs()]
    def plot(self):
        for ei in self.e:
            ei.plot()

def f(X, s):
    exec rootstr+"=X"
    return s.eqs()

t, a = 0, 0
T, X = [], []
d = type('', (), dict(xa=0, ya=0, xb=-1.345, yb=3.01195, L0=0.81371, L1=3.0, L2=2.0, L3=2.29))()
fr0 = Frame(x1=0.0, y1=0.0, x2=0.81371, y2=0, L=d.L0)
fr1 = Frame(x1=0.81371, y1=0, x2=0.65, y2=3, L=3.0)
fr2 = Frame(x1=0.65, y1=3, x2=-1.345, y2=3.01195, L=2.0)
fr3 = Frame(x1=-1.345, y1=3.01195, x2=-3.6, y2=3, L=2.29)
con0 = Connector(fr0, fr1)
con1 = Connector(fr1, fr2)
con2 = Connector2(fr2, fr3)
s = System([fr0, fr1, fr2, fr3, con0, con1, con2])
rootstr = "s.e[1].x1, s.e[1].y1, s.e[1].x2, s.e[1].y2, s.e[2].x1, s.e[2].y1, s.e[3].x2, s.e[3].y2"

while a < 2*pi:
    s.e[0].x2 = s.e[0].L * cos(a) + s.e[0].x1
    s.e[0].y2 = s.e[0].L * sin(a) + s.e[0].y1
    roots = [x + 0.001 for x in eval(rootstr)]
    sol = root(f, roots, args=(s,), method='lm')
    exec rootstr+"=sol.x"
    b = atan((s.e[3].y2 - s.e[3].y1) / (s.e[3].x2 - s.e[3].x1))
    x, y = s.e[0].x1 + s.e[3].x1 - s.e[3].L, -s.e[3].L * b
    plt.plot([x], [y], 'bo')
    plt.text(x + 0.1, y, t)
    plt.text(s.e[0].x2, s.e[0].y2, t)
    s.plot()
    T.append(t)
    X.append(y)
    t += 1
    a += pi / 16

plt.show()

import scipy
dt = T[1] - T[0]
V = scipy.gradient(X, dt)
A = scipy.gradient(V, dt)
plt.plot(T, X, 'k-', lw=2)
plt.plot(T, V, 'k--', lw=2)
plt.plot(T, A, 'r', lw=2)
plt.show()
