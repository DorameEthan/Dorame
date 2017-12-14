import turtle, random

window = turtle.Screen()
window.bgcolor ('black')


t = turtle.Turtle ()
t.color('cyan')
t.pensize (0.2)
t.shape('turtle')
t.speed (-10)

x = 2
y = 1
z = 1


print (y)
while 1==1:
  z=(z+1)
  t.forward (20)
  t.right (x)
  x=(1.1*(x/z)-z)
  while x > 259:
     x=x-360
  print (x)
