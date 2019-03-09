# -*- coding: UTF-8 -*-
class Student:

    def __init__(self, name, age,student_id):
        self.age = age
        self.name = name
        self.student_id = student_id
        self.courselist = []

    def add_course(self, course):
        self.courselist.append(course)
        print "Course %s added for %s" % (course, self.name)

    def list_courses(self):
        if len(self.courselist) > 0:
            print "Here are your courses %s:" % self.name
            for i in self.courselist:
                print i
        else:
            print "No courses added yet, %s" % self.name


joe = Student("Joe", 25, "f1234")
josie = Student("Josie", 21, "f5678")
joe.list_courses()
joe.add_course("script programming")
joe.list_courses()
josie.add_course("network programming")
josie.add_course("mathematics 2")
josie.list_courses()
