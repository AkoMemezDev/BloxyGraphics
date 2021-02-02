import turtle 

Jeff = turtle.Pen()

colourchoice = input("What colour would you like today? ")

Jeff.color(colourchoice)

Jeff.pensize(7)

Jeff.shape('square')

Jeff.speed(1)

steps = int(input("How many steps do you want it to take?"))

Jeff.fd(steps)
Jeff.rt(50)
Jeff.fd(steps)
Jeff.rt(50)
Jeff.fd(steps)
Jeff.rt(50)
Jeff.fd(steps)

#Thanks for looking at it and please if you want, modify it or use it!
