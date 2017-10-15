import pytest
from classroom import Classroom
from student import Student
# from student import Student
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


def setup():
    "Creates a new class with predefined inputs and returns the class"
    name = "Economics"
    meet_times = [("Tuesday", "2:30 PM"), ("Thursday", "2:30 PM")]
    roster = {"Nick": Student("Nick"), "Tom": Student("Tom"),
              "Jane": Student("Jane")}

    economics = Classroom(name, meet_times, roster)
    return economics


def test_add_student():
    """Test to see if student is added and if student name is already added."""
    economics = setup()
    assert economics.add_student("Tom") == False
    economics.add_student("Lisa")
    assert economics.roster["Lisa"].name == "Lisa"


def test_remove_student():
    """Test to see if student exists and can be removed."""
    pass


def test_add_assignment():
    """Test to see if assignment already exists and if assignment is created"""
    pass


def test_remove_assignment():
    """Test to see if assignment exists and can be removed."""
    pass


def test_grade_assignment():
    """Test to see if assignment exists, can be graded, and if grade is a
        number."""
    pass


def test_grade_individual_assignment():
    """Make sure assignment and student exist, then grade assignment for
        student."""
    pass


def test_return_student_grade():
    """Return a student's grade precentage in a class."""
    pass


def test_return_meet_times():
    """Make sure all meet times are returned."""
    pass


def test_return_roster():
    """Make sure all students in the roster are returned."""
    pass


def test_return_assignments():
    """Make sure all of the assignments are returned."""
    pass


def test_return_assignment_grades():
    """Make sure assignment exists, then return all grades for assignment."""
    pass
