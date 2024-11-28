from nodebox.graphics import *

def f(xp, yp, x1p, y1p):
    c = 0.95
    x1 = c * x1p
    x = x1 * dt + xp
    y1 = c * (y1p - 9.8 * dt)
    y = y1 * dt + yp
    return x, y, x1, y1

def draw(canvas):
    global x, y, x1, y1, t, dt
    if canvas.mouse.button == LEFT:
        t, x, y, x1, y1 = 0, 0, 0, canvas.mouse.x, canvas.mouse.y
    if x1 != 0 and y1 != 0 and y >= 0:
        x, y, x1, y1 = f(x, y, x1, y1)
        t += dt
    canvas.clear()
    fill(0, 0, 0)
    ellipse(x=x, y=y, width=10, height=10)

x, y, x1, y1 = 0, 0, 0, 0
dt = 0.1
canvas.size = 1280, 720
canvas.run(draw)
