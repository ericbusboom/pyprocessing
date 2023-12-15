# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here

# The shoot_arrow function goes here

def setup():
    # Setup your game here
    size(400, 400)  # width and height of screen

def draw():
    # Things to do in every frame
    fill('cyan')  # Set the fill color for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height

    fill('darkgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

# Keep this to run your code
run(frame_rate=2)
