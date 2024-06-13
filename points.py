from fractions import *
import math


class Equation:
    def __init__(self, slope, yintercept, xintercept, formula, x, y, frac):
        self.slope = slope
        self.xintercept = xintercept
        self.yintercept = yintercept
        self.formula = formula
        self.x = x
        self.y = y
        self.frac = frac

    def getformula(self, slope, x, yintercep):
        print(f'y = {self.formula}')
        self.formula = (self.slope * self.x) + self.yintercept

    def getyintercept(self, slope, x, y):
        self.yintercept = ((self.x / self.y) * self.x) + math.fabs(self.y)

    def getxintercept(self, yintercept, slope):
        self.xintercept = math.fabs(self.yintercept) / self.slope

