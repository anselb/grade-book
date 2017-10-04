import pytest
from Classroom import *
from Student import *
# import grade_book


def test_init():
    name = "economics"
    meet_times = [("Tuesday", "2:30 PM"), ("Thursday", "2:30 PM")]
    roster = {"Nick": Student("Nick"), "Tom": Student("Tom"),
              "Jane": Student("Jane")}
    economics = Classroom(name, meet_times, roster)
    assert name
    assert meet_times
    assert roster


def stuff():
    pass
