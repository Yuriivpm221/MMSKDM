import matplotlib.pyplot as plt
from scipy.optimize import root

def f(X):
    L1, L2 = 1, 2
    x1, y1, x2, y2 = X
    eqs = []
    
    eqs += [x1 - 0.5]
    eqs += [x1**2 + y1**2 - L1**2]
    eqs += [(x2 - x1)**2 + (y2 - y1)**2 - L2**2]
    eqs += [y2]
    return eqs

sol = root(f, [0, 0, 0, 0], method='lm')
x1, y1, x2, y2 = sol.x

plt.plot([0, x1], [0, y1], 'ko-')
plt.plot([x1, x2], [y1, y2], 'ko-')
plt.show()
