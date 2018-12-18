'''
    On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 
 
    For some of these problems you will need to create a class; for others, you will need to use a library. 
    You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in o ne foldermr o
'''
import numpy as np
import random as r
import turtle
from SymPy import Polygon
from VPython import *
 
 
 
''' 1.
    Create a class, Point, that keeps track of two properties: x and y
    When a point is created, values for x and y should be provided.
 
    The methods for this class are as follows:
    rotate90: rotate the point 90° about the origin
    rotate180: rotate the point 180° about the origin
    rotaten90: rotate -90° about the origin
    translate: given 2 values, translate the point by the given amount.
    flip_horizontally: flip the point on the x-axis
    flip_vertically: flip the point on the y-axis
'''
 
class Point:
    def __init__(self):
        self.x = r.randrange(0, 100)
        self.y = r.randrange(0, 100)

    def rotate90(self):
        self.x, self.y = self.y, -self.x

    def rotate180(self):
        self.x *= -1
        self.y *= -1

    def rotaten90(self):
        self.x, self.y = -self.y, self.x
 
''' 2.
    Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
    When a Bicycle is created, cadence, gear, and speed are accepted as arguments.
 
    The methods for this class are as follows:
    set_gear: given a value, set the gear to that value
    set_cadence: given a value, set the cadence to that value
    apply_brake: given a value, decrease the speed of the bike by that value
    speed_up: given a value, increase the speed of the bike by that value
'''
class Bicycle:
    def__init__(self, cadnece, gear, speed):
        self.cadence = cadence
        self.gear = gear
        self.speed = speed

    def set_gear(self, inputgear):
        self.gear = inputgear

    def set_cadence(self, inputcadence):
        self.cadence = inputcadence

    def apply_break(self, inputbreak):
        self.speed -= inputbreak

    def speed_up(self, inputspeed):
        self.speed += inputspeed
 
 
 
 
''' 3.
    Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
    These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.
 
    The methods for the student class are as follows:
    study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
    sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
    class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
    take_test: Given a value (to adjust hours), this increases stress. 
    submit_paper: this decreases stress.
    eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
    sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
    new_day: resets the hours in a day.
 
    You may not let a student do more than 24 hours worth of activities in a given day. 
'''
 
 
class Student:
    def __init__(self):
        self._energy = 100
        self._hunger = 50
        self._stress = 0
        self._hours = 24

    @property
    def hours(self):
        return self._hours   

    @hours.setter
    def hours(self, value):
        value += self._hours
        if value > 100:
            self._hours = 100
        elif value < 0:
            self._hours = 0
        else:
            self._hours = value

    @hours.getter
    def stress(self):
        return self._hours

    @property
    def stress(self):
        return self._stress   

    @stress.setter
    def stress(self, value):
        value += self._stress
        if value > 100:
            self._stress = 100
        elif value < 0:
            self._stress = 0
        else:
            self._stress = value

    @stress.getter
    def stress(self):
        return self._stress

    @property
    def energy(self):
        return self._energy    

    @energy.setter
    def energy(self, value):
        value += self._energy
        if value > 100:
            self._energy = 100
        elif value < 0:
            self._energy = 0
        else:
            self._energy = value

    @energy.getter
    def energy(self):
        return self._energy

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        hunger = self._hunger + value
        if hunger > 100:
            self._hunger = 100
        elif hunger < 0:
            self._hunger = 0
        else:
            self._hunger = hunger

    @hunger.getter
    def hunger(self):
        return self._hunger

    def study(self, hours):
        self.hours -= hours
        self.energy -= hours
        self.hunger += hours

    def sports(self, hours):
        self.hours -= hours
        self.energy -= hours
        self.hunger += hours
        self.stress -= hours

    def take_test(self, hours):
        self.hours -= hours
        self.stress += hours

    def submit_paper(self):
        self.stress -= 10

    def take_class(self, hours):
        self.hours -= hours
        self.hunger += hours
        self.energy -= hours
        self.stress += hours

    def eat_meal(self, hours):
        self.hours -= hours
        self.hunger -= hours
        self.stress -= hours
        self.energy += hours

    def sleep(self, hours):
        self.stress -= hours
        self.energy += hours
        self.hunger += hours

    def new_day(self, hours):
        self.hours = 24
 
''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the valunes.
'''

numbers = np.array([20+i/4 for i in range(0, 4*(100-20)+1)])
numbers *= 4
 
''' 5.
    Use turtle to draw a star.
'''
from turtle import *
setpos(20,60)
pendown()
setpos(5,10)
setpos(40,40)
setpos(0,40)
setpos(35,10)
setpos(20,60)

''' 6.
    Use SymPy to determine the area of a triangle given points a, b and c.
'''
 
 
a, b, c = [r.randrange(100), r.randrange(100) for i in range(3)]
area = Polygon(a, b, c).area
 
''' 7. 
    Use VPython to build a 3D snowman.
'''
 
 ball1 = sphere(pos=(0, 0, 4), radius=4)
 ball2 = sphere(pos=(0, 0, 10), radius=2)
 ball3 = sphere(pos=(0, 0, 13), radius=1)
 
''' Sources:
    https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''
