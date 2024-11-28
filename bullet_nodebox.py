from nodebox.graphics import *

# Модель польоту снаряду
def f(xp, yp, x1p, y1p):
    x1 = x1p
    x = x1 * dt + xp
    y1 = y1p - 9.8 * dt
    y = y1 * dt + yp
    return x, y, x1, y1

def draw(canvas):
    global x, y, x1, y1
    canvas.clear()
    if y >= 0:
        x, y, x1, y1 = f(x, y, x1, y1)
    ellipse(x=x, y=y, width=10, height=10)

dt = 0.1
x, y, x1, y1 = 0, 0, 70, 70

canvas.size = 500, 500
canvas.run(draw)
