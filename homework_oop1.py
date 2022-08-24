import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_average = 0

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and ((course in self.courses_in_progress) or (course in self.finished_courses)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def average_func(self):
        list_grades = []
        for course, rates in self.grades.items():
            list_grades += rates
        self.grade_average = statistics.mean(list_grades)  
        return self.grade_average

    def __lt__(self, other):
        return self.grade_average < other.grade_average

    def __eq__(self, other):
        return self.grade_average == other.grade_average
                         
    def __str__(self) -> str:
        self.average_func()  
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Cредняя оценка за домашние задания: {self.grade_average}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''  


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
        self.grade_average = 0

    def average_func(self):
        list_grades = []
        for course, rates in self.grades.items():
            list_grades += rates
        self.grade_average = statistics.mean(list_grades)  
        return self.grade_average

    def __lt__(self, other):
        return self.grade_average < other.grade_average

    def __eq__(self, other):
        return self.grade_average == other.grade_average


    def __str__(self) -> str:
        self.average_func()
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Cредняя оценка за лекции: {self.grade_average}'''



class Reviewer(Mentor):   
    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'''
Имя: {self.name}
Фамилия: {self.surname} '''


def compare_student(student1, student2):
    if isinstance(student1,Student) and isinstance(student2,Student):
        student1.average_func()
        student2.average_func()
        if student1 == student2:
            print(f'Средняя оценка студанта {student1.name} {student1.surname} и средняя оценка студента {student2.name} {student2.surname} равны')
        elif student1 < student2:
            print(f'Средняя оценка студанта {student1.name} {student1.surname} ниже средней оценки студента {student2.name} {student2.surname}')
        else:
            print(f'Средняя оценка студанта {student1.name} {student1.surname} выше средней оценки студента {student2.name} {student2.surname}')
    else:
        return 'Ошибка'   

def compare_lector(lecturer1, lecturer2):
    if isinstance(lecturer1,Lecturer) and isinstance(lecturer2,Lecturer):
        lecturer1.average_func()
        lecturer2.average_func()
        if lecturer1 == lecturer2:
            print(f'Средняя оценка лектора {lecturer1.name} {lecturer1.surname} и средняя оценка лектора {lecturer2.name} {lecturer2.surname} равны')
        elif lecturer1 < lecturer2:
            print(f'Средняя оценка лектора {lecturer1.name} {lecturer1.surname} ниже средней оценки лектора {lecturer2.name} {lecturer2.surname}')
        else:
            print(f'Средняя оценка лектора {lecturer1.name} {lecturer1.surname} выше средней оценки лектора {lecturer2.name} {lecturer2.surname}')
                
    else:
        return 'Ошибка'
 
def rating_homework(course,list_student=[]):
    rating_list = []
    for person in list_student:
        if isinstance(person,Student) and course in person.grades.keys():
            rating_list += person.grades[course] 
    if len(rating_list) == 0:
        return 'Нет оценок за домашние задания по этому курсу'
    else:
        return f'Средняя оценка за домашние задания по курсу {course}: {statistics.mean(rating_list)} баллов'

def rating_lecture(course,list_lecturer=[]):
    rating_list = []
    for person in list_lecturer:
        if isinstance(person,Lecturer) and course in person.grades.keys():
            rating_list += person.grades[course]    
    if len(rating_list) == 0:
        return 'Нет оценок за лекции по этому курсу'
    else:
        return f'Средняя оценка за лекции по курсу {course}: {statistics.mean(rating_list)} баллов'
        



best_student1 = Student('Ruoy', 'Eman', 'Male')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']

best_student2 = Student('Mary', 'Lu', 'Feale')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.courses_in_progress += ['English']
best_student2.finished_courses += ['Spanish']

 
cool_mentor1 = Reviewer('Some', 'Buddy')
cool_mentor1.courses_attached += ['Python']

cool_mentor2 = Reviewer('Tim', 'Sun')
cool_mentor2.courses_attached += ['Python']
cool_mentor2.courses_attached += ['Git']


mentor_lect1 = Lecturer('Bill','Ray')
mentor_lect1.courses_attached += ['Python']

mentor_lect2 = Lecturer('Tom','Jons')
mentor_lect2.courses_attached += ['Git']
mentor_lect2.courses_attached += ['Python']

best_student1.rate_lect(mentor_lect1, 'Python', 7)
best_student1.rate_lect(mentor_lect1, 'Python', 5)
best_student1.rate_lect(mentor_lect1, 'Python', 10)

best_student2.rate_lect(mentor_lect1, 'Python', 6)
best_student2.rate_lect(mentor_lect1, 'Python', 8)
best_student2.rate_lect(mentor_lect1, 'Python', 9)

best_student2.rate_lect(mentor_lect2, 'Python', 9)
best_student2.rate_lect(mentor_lect2, 'Python', 4)
best_student2.rate_lect(mentor_lect2, 'Python', 5)

cool_mentor1.rate_stud(best_student2, 'Python', 9)
cool_mentor1.rate_stud(best_student2, 'Python', 10)
cool_mentor1.rate_stud(best_student2, 'Python', 10)

cool_mentor2.rate_stud(best_student1, 'Git', 9)
cool_mentor2.rate_stud(best_student1, 'Git', 8)
cool_mentor2.rate_stud(best_student1, 'Git', 10)



print(best_student1)
print(best_student2)

print(cool_mentor1)
print(cool_mentor2)

print(mentor_lect1)
print(mentor_lect2)

compare_student(best_student1, best_student2)
compare_lector(mentor_lect1,mentor_lect2)

print(rating_homework('Python',[best_student1, best_student2]))
print(rating_homework('Git',[best_student1, best_student2]))

print(rating_lecture('Python',[mentor_lect1, mentor_lect2]))
print(rating_lecture('Git',[mentor_lect1, mentor_lect2]))


