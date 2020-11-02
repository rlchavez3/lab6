import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.screensize(500)
turtle.speed(0)
turtle.tracer(1, 0)

star_file = open('stars.txt', 'r')
stars = star_file.readlines()
star_file.close()

for line in stars:
  split = line.split()
  x = float(split[0]) * 250
  y = float(split[1]) * 250
  m = round(10/(float(split[4]) + 2))
  if m > 10:
    m = 10
  elif m < 1:
    m = 1
  t.up()
  t.color('white')
  t.goto(x, y)
  t.dot(m)

turtle.exitonclick()
