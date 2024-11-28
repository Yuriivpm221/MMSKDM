from nodebox.graphics import *

def f(xp, yp, x1p, y1p):
    c = 0.95
    x1 = c * x1p
    x = x1 * dt + xp
    y1 = c * (y1p - 9.8 * dt)
    y = y1 * dt + yp
    return x, y, x1, y1

def draw(canvas):
    global x, y, x1, y1, t, dt, xt, s, x1t
    if canvas.mouse.button == LEFT:
        t, x, y, x1, y1 = 0, 0, 0, canvas.mouse.x, canvas.mouse.y
    if x1 != 0 and y1 != 0 and y >= 0:
        x, y, x1, y1 = f(x, y, x1, y1)
        t += dt

    canvas.clear()

    # Малюємо снаряд
    fill(0, 0, 0)
    ellipse(x=x, y=y, width=10, height=10)

    # Малюємо ціль
    fill(1, 0, 0)
    rect(x=xt, y=0, width=30, height=20)

    # Перевірка на влучання
    if xt < x < xt + 30 and 0 < y < 20:
        s += 1
        x, y, x1, y1 = 0, 0, 0, 0
        xt = 700
        x1t -= 0.1

    # Закінчення гри, якщо ціль вийшла за межі
    if xt < 0:
        exit()

    # Відображення рахунку
    fill(0, 0, 0)
    text(f"Score: {s}", 300, 300)

    # Рух цілі
    xt += x1t

# Ініціалізація змінних
x, y, x1, y1 = 0, 0, 0, 0
dt = 0.1
t = 0
xt = 700
x1t = -0.5
s = 0

canvas.size = 1280, 720
canvas.run(draw)
