import pytest
from Classroom import *
from Student import *
# import grade_book


# def test_init():
#     """Tests if Classroom obeject can be created."""
#     name = "Economics"
#     meet_times = [("Tuesday", "2:30 PM"), ("Thursday", "2:30 PM")]
#     roster = {"Nick": Student("Nick"), "Tom": Student("Tom"),
#               "Jane": Student("Jane")}
#     assert name
#     assert meet_times
#     assert roster
#     return Classroom(name, meet_times, roster)

name = "Economics"
meet_times = [("Tuesday", "2:30 PM"), ("Thursday", "2:30 PM")]
roster = {"Nick": Student("Nick"), "Tom": Student("Tom"),
          "Jane": Student("Jane")}

economics = Classroom(name, meet_times, roster)


def test_add_student():
    assert economics.add_student("Tom") == False
    economics.add_student("Lisa")
    assert economics.roster["Lisa"].name == "Lisa"


def test_remove_student():

    pass


def test_add_assignment():
    pass


def test_remove_assignment():
    pass


def test_grade_assignment():
    pass


def test_grade_individual_assignment():
    pass


def test_return_student_grade():
    pass


def test_return_meet_times():
    pass


def test_return_roster():
    pass


def test_return_assignments():
    pass


def test_return_assignment_grades():
    pass
