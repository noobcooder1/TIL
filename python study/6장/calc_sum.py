import turtle as t
answer = t.textinput("title", "계속하려면 yes, 아니면 아무 글자나 입력하시오.")
t.pensize(5)

while answer == "yes":
    t.shape("turtle")
    t.up()
    t.goto(-150, 0)
    t.down()

    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)

    t.clear()
    answer = t.textinput("title", "계속하려면 yes, 아니면 아무 글자나 입력하시오.")




