import turtle
import random
import matplotlib.pyplot as plt

def randwalk(n):
    x = 0
    y = 0
    step_x = [x]
    step_y = [y]

    for i in range(1,n+1):
        move = random.randint(0,3)
        if move == 0:
            x += 1
        if move == 1:
            x += -1
        if move == 2:
            y += 1
        if move == 3:
            y += -1
        step_x.append(x)
        step_y.append(y)
    return [step_x, step_y]

# '''Plotting the 2-D Random Walks'''
# randwalk1 = randwalk(1000)
# randwalk2 = randwalk(1000)
# randwalk3 = randwalk(1000)

# plt.plot(randwalk1[0], randwalk1[1], 'r-', label = "randwalk1")
# plt.plot(randwalk2[0], randwalk2[1], 'g-', label = "randwalk2")
# plt.plot(randwalk3[0], randwalk3[1], 'b-', label = "randwalk3")
# plt.title("2-D Random Walks")
# plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1), fancybox=True, shadow=True)
# plt.show() 

#import turtle library to animate the random walk
# import turtle
turtle.speed('fastest')

walk = randwalk(1000)
turtle.color("green")
for x, y in zip(*walk):
    #multiply by 5 to enlarge the random walk
    turtle.goto(x*5,y*5)

turtle.up()
turtle.goto(0,0)
turtle.color("blue")
walk2= randwalk(1000)
turtle.down()
for x, y in zip(*walk2):
    #multiply by 5 to enlarge the random walk
    turtle.goto(x*5,y*5)

turtle.up()
turtle.goto(0,0)
turtle.color("red")
walk3= randwalk(1000)
turtle.down()
for x, y in zip(*walk3):
    #multiply by 5 to enlarge the random walk
    turtle.goto(x*5,y*5)
turtle.exitonclick() 
#neat feature of turtle 