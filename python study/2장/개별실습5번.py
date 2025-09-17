import turtle as t

radius = 50

t.up()
t.goto(0, 0)
t.down()

t.begin_fill()
t.circle(radius)

t.up()
t.goto(100, 0)
radius += 20
t.down()

t.begin_fill()
t.circle(radius)

t.up()
t.goto(200, 0)
radius += 20
t.down()

t.begin_fill()
t.circle(radius)

t.done()