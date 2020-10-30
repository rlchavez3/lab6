import turtle
t = Turtle.turtle()
turtle.bgcolor('black')
turtle.screensize(500)
turtle.speed(0)
turtle.tracer(1, 0)

star_file = open('stars.txt', 'r')
lines = star_file.readlines()
star_file.close()

turtle.exitonclick()
