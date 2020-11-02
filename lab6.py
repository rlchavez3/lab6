# setting up turtle screen
import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.screensize(500)
turtle.speed(0)
turtle.tracer(1, 0)

# getting data from stars file
star_file = open('stars.txt', 'r')
stars = star_file.readlines()
star_file.close()

# iterating through data and drawing
for line in stars:
  split = line.split()
  # x coordinate conversion
  x = float(split[0]) * 250
  # y coordinate conversion
  y = float(split[1]) * 250
  # magnitude conversion and limit
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
