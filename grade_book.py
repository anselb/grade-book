from Classroom import *
from Student import *


def valid_response(response):
    if response == "yes" or response == "no":
        return True
    else:
        return False


# def new_class(name, meet_times, roster):
#     """Create a new class. Makes sure info is correct before submission."""
#     okay = True
#     response = ""
#     while okay:
#         print("What is the class name?")
#         name = input()
#         while not valid_response(response):
#             print("Are you okay with " + name +
#                   "? This information cannot be changed later.")
#             response = input()
#         if response == "yes":
#             okay = False
#     okay = True
#     response = ""
"""
For each of the three function groups, it will print a list of prompts for what
the user can do while the input in not equal to a prompt option. After
inputting a valid option, the coresponding class methods and their prompt(s)
for input will be called.
"""


def roster_functions(class_name):
    action = ""
    while action != "add" and action != "remove" and action != "roster":
        print("add new student: add\nremove student: remove")
        print("view roster: roster")
        action = input()

    if action == "add":
        print("Who would you likd to add?")
        student_name = input()
        class_name.add_student(student_name)
    if action == "remove":
        print("Who would you likd to remove?")
        student_name = input()
        class_name.remove_student(student_name)
    if action == "roster":
        class_name.return_roster()


def assignment_functions(class_name):
    action = ""
    while action != "create" and action != "delete" and action != "list" and \
            action != "class" and action != "ind":
        print("create assignment: create\ndelete assignment: delete")
        print("view assignment list: list\ngrade assignment for class: class")
        print("grade assignment for individual: ind")
        action = input()

    if action == "create":
        print("What is the assignment name?")
        assignment_name = input()
        print("What is the max possible assignment score?")
        assignment_score = int(input())
        class_name.add_assignment(assignment_name, assignment_score)
    if action == "delete":
        print("Which assignment would you like to delete?")
        assignment_name = input()
        class_name.remove_assignment(assignment_name)
    if action == "list":
        class_name.return_assignments()
    if action == "class":
        print("Which assignment would you like to grade?")
        assignment_name = input()
        class_name.grade_assignment(assignment_name)
    if action == "ind":
        print("Which assignment would you like to grade?")
        assignment_name = input()
        print("Who would you like to grade the assignment for?")
        student_name = input()
        class_name.grade_individual_assignment(student_name, assignment_name)


def information_functions(class_name):
    action = ""
    while action != "times" and action != "scores" and action != "single":
        print("view meet times: times\nview scores for an assignment: scores")
        print("view single student's score: single")
        action = input()

    if action == "times":
        class_name.return_meet_times()
    if action == "scores":
        print("Which assignment would you like to see the score of?")
        assignment_name = input()
        class_name.return_assignment_grades(assignment_name)
    if action == "single":
        print("Whose score woud you like to see?")
        student_name = input()
        class_name.return_student_grade(student_name)


def grade_book():
    """Start the grade book program."""
    # more_classes = True
    # classes = {}
    # while more_classes:
    #     new_class()
    #     print("Would you like to make another class right now?")
    name = "economics"
    meet_times = [("Tuesday", "2:30 PM"), ("Thursday", "2:30 PM")]
    roster = {"Nick": Student("Nick"), "Tom": Student("Tom"),
              "Jane": Student("Jane")}
    economics = Classroom(name, meet_times, roster)
    on = True
    while on:
        action = ""
        while action != "roster" and action != "assignment" and \
                action != "info":
            print("If you would like to modify or view the roster, "
                  "type: roster")
            print("If you would like to add, remove, grade or view "
                  "assignments, type: assignment")
            print("If you would like to see the grades, meet times, roster, "
                  "or assignment list, type: info ")
            action = input()

        if action == "roster":
            roster_functions(economics)
        if action == "assignment":
            assignment_functions(economics)
        if action == "info":
            information_functions(economics)


grade_book()
