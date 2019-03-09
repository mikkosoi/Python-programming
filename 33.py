# -*- coding: UTF-8 -*-

class Dog:

    def __init__(self, name, sound, walking_speed, running_speed):
        self.name = name
        self.sound = sound
        self.walking_speed = walking_speed
        self.running_speed = running_speed

    def walk(self):
        print "Dog walks with speed %d km/h" % self.walking_speed

    def run(self):
        print "Dog runs with speed %d km/h" % self.running_speed

    def bark(self):
        return "Dog barks with sound %s" % self.sound

    def print_name(self):
        return "Dog is known as %s" % self.name


Mauri = Dog("Mauri", "Woof", 10, 25)
print  Mauri.print_name()
print Mauri.bark()
Mauri.run()

Esko = Dog("Esko", "Arf arf",5,43)
print Esko.print_name()
Esko.walk()
