class Student(object):
    """Student Object."""
    def __init__(self, name):
        """Initialize new student."""
        # name is a string
        self.name = name
        # scores is a dictionary of assignments and their max possible scores
        self.scores = {}
