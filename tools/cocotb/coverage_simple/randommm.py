# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
from adder_model import adder_model
import random
from cocotb_coverage import crv
from cocotb_coverage.coverage import *
# from cocotb_coverage.crv import *

class Point(crv.Randomized):
    def __init__(self, x, y):
        crv.Randomized.__init__(self)
        self.x = x
        self.y = y
        self.b = True

        self.add_rand("x", list(range(-10, 10)))
        self.add_rand("y", list(range(-10, 10)))
        self.add_rand("b", [True,False])
        # constraining the space so that x < y
        self.add_constraint(lambda b,x,y: x < y and b)

p = Point(0,0)
p.randomize()  # randomize object

print(p.x)
print(p.y)
print(p.b)
