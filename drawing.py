from turtle import (
    forward, 
    right,
)
from superturtle.stroke import (
    dots, 
)

def square(side_length):
    for side in range(4):
        forward(side_length)
        right(90)

with dots():
    square(100)

input("Press enter to continue...")
