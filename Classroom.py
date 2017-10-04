import Student


class Classroom(object):
    """Classroom Object."""
    def __init__(self, name, meet_times, roster):
        """Initialize new classroom."""
        # name is a string
        self.name = name
        # meet_times is an array of tuples
        self.meet_times = meet_times
        # roster is a dictionary of student objects
        self.roster = roster
        # assignments is an array of assignments
        self.assignments = {}

    def add_student(self, student_name):
        """Adds new student."""
        self.roster[student_name] = Student(student_name)
        for assignment in self.assignments:
            self.roster[student_name].scores[assignment_name] = -1
        print("Added " + student_name + " to " + self.name + " roster.")

    def remove_student(self, student_name):
        """Removes a student based on input name."""
        if student_name in self.roster:
            del self.roster[student_name]
            print("Removed " + student_name + " from " +
                  self.name + " roster.")
        else:
            print("Could not find student " + student_name + ".")

    def add_assignment(self, assignment_name, assignment_score):
        """Adds an assignment."""
        if assignment_name in self.assignments:
            print("There is already an assignment named " + assignment_name)
            return
        self.assignments[assignment_name] = assignment_score
        for student in self.roster:
            self.roster[student].scores[assignment_name] = -1
        print("Added " + assignment_name + " to " +
              self.name + " assignments.")

    def grade_assignment(self, assignment_name):
        """Grades an assignment for the whole roster."""
        if assignment_name in self.assignments:
            for student in self.roster:
                print("What score did " + student + " get?")
                self.roster[student].scores[assignment_name] = float(input())
            print("Graded " + assignment_name + " in " + self.name + ".")
        else:
            print("Could not find " + assignment_name + ".")

    def grade_individual_assignment(self, student_name, assignment_name):
        """Grades an assignment for a student."""
        if assignment_name in self.assignments:
            if student_name in self.roster:
                print("What score did " + student_name + " get?")
                self.roster[student_name].scores[assignment_name] = \
                    float(input())
                print("Graded " + assignment_name + " for " +
                      student_name + ".")
            else:
                print("Could not find " + student_name + ".")
        else:
            print("Could not find " + assignment_name + ".")

    def remove_assignment(self, assignment_name):
        """Removes an assignment and all student scores."""
        del self.assignments[assignment_name]
        print("Removed " + assignment_name + " from " +
              self.name + " assignments.")

    def return_student_grade(self, student_name):
        """Returns student's grade in class."""
        if student_name in self.roster:
            student_points = 0
            total_points = 0
            excused_assignments = 0
            for assignment in self.assignments:
                if self.roster[student_name].scores[assignment] >= 0:
                    student_points += \
                        self.roster[student_name].scores[assignment]
                    total_points += self.assignments[assignment]
                else:
                    excused_assignments += 1
            print(student_name + " has a score of " +
                  str(student_points / total_points) +
                  " with " + str(excused_assignments) + " excused assignments "
                  " in " + self.name + ".")
        else:
            print("Could not find " + student_name + ".")

    def return_meet_times(self):
        """Returns meet times."""
        for (meet_day, meet_time) in self.meet_times:
            print(meet_day + " at " + meet_time)

    def return_roster(self):
        """Returns class roster."""
        for student in self.roster:
            print(student)

    def return_assignments(self):
        """Returns list of assignments."""
        for assignment in self.assignments:
            print(assignment + " has a possible score of: " +
                  str(self.assignments[assignment]))

    def return_assignment_grades(self, assignment_name):
        """Returns assignment grades for all students."""
        if assignment_name in self.assignments:
            for student in self.roster:
                print(student + ": " +
                      str(self.roster[student].scores[assignment_name]))
        else:
            print("Could not find " + assignment_name + ".")
