
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result_stud = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {round((Student.average_stud(self)), 1)} \n Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses}'
        return result_stud

    def average_stud(self):
        for course, grades in self.grades.items():
            return sum(grades) / len(grades)

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.grades_lec = {}

    def average_lec(self):
        for course, grades_lec in self.grades_lec.items():
            return sum(grades_lec) / len(grades_lec)


    def average_grade_to_course(self, course):
        if course in self.courses_attached:
            for grades_lec in self.grades_lec.values():
                return sum(grades_lec) / len(grades_lec)
        else:
            return 'Лектор не преподает на этом курсе'

    def __str__(self):
        result_lec = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {round((Lecturer.average_lec(self)), 1)}'
        return result_lec

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


student_one = Student('Ruoy', 'Eman', 'man')
student_one.courses_in_progress += ['Python', 'GIT']
student_one.finished_courses += ['Введение в программирование']

Reviewer_one = Reviewer('Some', 'Buddy')
Reviewer_one.courses_attached += ['Python', 'GIT']

Reviewer_one.rate_hw(student_one, 'Python', 5)
Reviewer_one.rate_hw(student_one, 'Python', 7)
Reviewer_one.rate_hw(student_one, 'Python', 9)
Reviewer_one.rate_hw(student_one, 'GIT', 8)
Reviewer_one.rate_hw(student_one, 'GIT', 9)
Reviewer_one.rate_hw(student_one, 'GIT', 10)


lecturer_one = Lecturer('Some', 'Buddy')
lecturer_one.courses_attached += ['Python', 'GIT']
student_one.rate_l(lecturer_one, 'Python', 8)
student_one.rate_l(lecturer_one, 'Python', 9)
student_one.rate_l(lecturer_one, 'Python', 10)
student_one.rate_l(lecturer_one, 'GIT', 8)
student_one.rate_l(lecturer_one, 'GIT', 7)
student_one.rate_l(lecturer_one, 'GIT', 6)

print(lecturer_one)
print(student_one)
