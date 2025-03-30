class Student:
    all_students = []

    # Write your code here.

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        # Write your code here.

    # Write your code here.

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            ValueError("New grade not in accepted range of [0-100]")
        self._grade = new_grade

    @staticmethod
    def calculate_average_student(students):
        res = 0
        if not students:
            return -1
        for student in students:
            res += student.grade
        return res / len(students)

    def get_best_student(cls):
        best_student = None
        for student in cls.all_students:
            if best_student == None and best_student.grade < student.grade:
                best_student = student
        return best_student