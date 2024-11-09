# OO code using turtle graphics
**What I've done**  
I create 3 classes `polygon`, `EmbeddedPolygon` and `Run`
  - *`Polygon`*
    - Mostly I copy code from original such as turtle setupl. What I'm doing is just set `__init__` variable.
  - *`EmbeddedPolygon`*
    - Like `Polygon` but this is a subclass of `Polygon`. I've add the `super()` to call the same variable as `Polygon` class. I add `draw(self)` which copy from the original as well
  - *`Run`*
    - I set the default value of variable that will be used to be a random same as original code and I add 2 variable name `polygon` and `number`. `polygon` it's used to check that what you want to run is `"polygon"` or `"Embedded"` the default input is `"polygon"`. And `number` is used to set the number of embedded which default value is set to 2 to 5.
  
**How to run my program**  
Basicly if you run `$ py polygon_art.py` you will get the question `Which art do you want to generate? Enter a number between 1 to 9 inclusive: `  which give you a triangle, square , pentagon and a random polygon that have both normal and embedded form.  
**Problem and Issue**  
  - This program isn't running well on shell because at most I coded out of classes.
  - My code have many arguments and instance attributes.
  - At first I have no idea what I'm doing, so I ask two TA's to have me pass this assignment.
