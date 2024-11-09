import turtle
import random

class Polygon():
    def __init__(self, num_sides, size, orientation, location, color, border_size) -> None:
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()
    
class Run():
    def __init__(self, num_sides = random.randint(3, 5), 
                size = random.randint(50, 150),
                orientation = random.randint(0, 90), 
                location = [random.randint(-300, 300), 
                            random.randint(-200, 200)], 
                color = (random.randint(0, 255), random.randint(0, 255),
                        random.randint(0, 255)),
                border_size = random.randint(1, 10), 
                polygon = "polygon", number = random.randint(2, 5)) -> None:
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
        self.polygon = polygon
        self.number = number
    
    def draw(self):
        if self.polygon == "polygon":
            polydraw = Polygon(self.num_sides, self.size, self.orientation,
                            self.location, self.color, self.border_size)
        elif self.polygon == "Embedded":
            polydraw = EmbeddedPolygon(self.num_sides, self.size, 
                                    self.orientation, self.location, 
                                    self.color, self.border_size, self.number)
        polydraw.draw()
    
class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, 
                border_size, number) -> None:
        super().__init__(num_sides, size, orientation, location, color,
                        border_size)
        self.number = number
                
    def draw(self):
        for _ in range(self.number):
            polydraw = Polygon(self.num_sides, self.size, self.orientation,
                            self.location, self.color, self.border_size)
            polydraw.draw()
            reduction_ratio = 0.618
            
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= reduction_ratio
            turtle.penup()
            
#choice 1-9
num = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
lisPE = ['polygon', 'Embedded']

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def rd(text):
    if text == "num_sides":
        return random.randint(3, 5)
    elif text == "size":
        return random.randint(50, 150)
    elif text == "orientation":
        return random.randint(0, 90)
    elif text == "location":
        return [random.randint(-300, 300), random.randint(-200, 200)]
    elif text == "color":
        return get_new_color()
    elif text == "border":
        return random.randint(1, 10)
    
if num == 1:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = 3, size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"))
        triA.draw()
elif num == 2:
    for i in range(random.randint(20, 35)):
        sqr = Run(num_sides = 4, size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"))
        sqr.draw()
elif num == 3:
    for i in range(random.randint(20, 35)):
        pent = Run(num_sides = 5, size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"))
        pent.draw()
elif num == 4:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = rd("num_sides"), size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"))
        triA.draw()
elif num == 5:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = 3, size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"), polygon = "Embedded")
        triA.draw()
elif num == 6:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = 4, size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"), polygon = "Embedded")
        triA.draw()
elif num == 7:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = 5, size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"), polygon = "Embedded")
        triA.draw()
elif num == 8:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = rd("num_sides"), size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"), polygon = "Embedded")
        triA.draw()
elif num == 9:
    for i in range(random.randint(20, 35)):
        triA = Run(num_sides = rd("num_sides"), size = rd("size"),
                orientation = rd("orientation"),location = rd("location"),
        color = rd("color"), border_size = rd("border"),
        polygon = random.choice(lisPE))
        triA.draw()
turtle.done()