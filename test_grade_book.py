import pytest
from classroom import Classroom
from student import Student
from unittest.mock import patch
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
    economics = setup()
    assert economics.remove_student("Lisa") == False
    economics.remove_student("Tom")
    assert "Tom" not in economics.roster


def test_add_assignment():
    """Test to see if assignment already exists and if assignment is created"""
    economics = setup()
    economics.add_assignment("test", 100)
    assert "test" in economics.assignments
    assert economics.add_assignment("test", 100) == False


def test_remove_assignment():
    """Test to see if assignment exists and can be removed."""
    economics = setup()
    assert economics.remove_assignment("test") == False
    economics.add_assignment("test", 100)
    assert "test" in economics.assignments
    economics.remove_assignment("test")
    assert "test" not in economics.assignments


def test_grade_assignment():
    """Test to see if assignment exists, can be graded, and if grade is a
        number."""
    economics = setup()
    assert economics.grade_assignment("test") == False
    economics.add_assignment("test", 100)
    with patch('classroom.input', return_value='90'):
        economics.grade_assignment("test")
    assert economics.roster["Tom"].scores["test"] == 90


def test_grade_individual_assignment():
    """Make sure assignment and student exist, then grade assignment for
        student."""
    economics = setup()
    assert economics.grade_individual_assignment("Tom", "test") == False
    economics.add_assignment("test", 100)
    assert economics.grade_individual_assignment("James", "test") == False
    with patch('classroom.input', return_value='70'):
        economics.grade_individual_assignment("Tom", "test")
    assert economics.roster["Tom"].scores["test"] == 70


def test_return_student_grade(capfd):
    """Return a student's grade precentage in a class."""
    economics = setup()
    economics.add_assignment("test 1", 100)
    economics.add_assignment("test 2", 100)
    economics.add_assignment("test 3", 100)
    economics.roster["Tom"].scores["test 1"] = 70
    economics.roster["Tom"].scores["test 2"] = 90
    assert economics.return_student_grade("Joe") == False
    not_out, err = capfd.readouterr()
    economics.return_student_grade("Tom")
    out, err = capfd.readouterr()
    assert out == ("Tom has a score of 80.0 with 1 excused assignments in"
                   " Economics.\n")


def test_return_meet_times(capfd):
    """Make sure all meet times are returned."""
    economics = setup()
    economics.return_meet_times()
    out, err = capfd.readouterr()
    assert out == ("Tuesday at 2:30 PM\nThursday at 2:30 PM\n")


def test_return_roster(capfd):
    """Make sure all students in the roster are returned."""
    economics = setup()
    economics.return_roster()
    out, err = capfd.readouterr()
    assert out == ("Nick\nTom\nJane\n")


def test_return_assignments(capfd):
    """Make sure all of the assignments are returned."""
    economics = setup()
    economics.add_assignment("test 1", 100)
    economics.add_assignment("test 2", 100)
    economics.add_assignment("test 3", 100)
    not_out, err = capfd.readouterr()
    economics.return_assignments()
    out, err = capfd.readouterr()
    assert out == ("test 1 has a possible score of: 100\n"
                   "test 2 has a possible score of: 100\n"
                   "test 3 has a possible score of: 100\n")


def test_return_assignment_grades(capfd):
    """Make sure assignment exists, then return all grades for assignment."""
    economics = setup()
    assert economics.return_assignment_grades("test") == False
    economics.add_assignment("test", 100)
    economics.roster["Nick"].scores["test"] = 75
    economics.roster["Jane"].scores["test"] = 90
    not_out, err = capfd.readouterr()
    economics.return_assignment_grades("test")
    out, err = capfd.readouterr()
    assert out == ("Nick: 75\n"
                   "Tom: not graded\n"
                   "Jane: 90\n")
