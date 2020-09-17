from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

nutshell = Exercise('nutshell', 'JavaScript') 
reactnutshell = Exercise('reactshell', 'react') 
bangazon = Exercise('bangazon', 'C#/.Net') 
trestlebridge = Exercise('TrestleBridge Farms', 'C#') 

cohort1 = Cohort('Day Cohort 37')
cohort2 = Cohort('Day Cohort 38')
cohort3 = Cohort('Evening Cohort 13')

student1 = Student('james', 'Nitz', 'jnitz')
student2 = Student('Slick', 'bigman', 'slickyb')
student3 = Student('kevin', 'penny', 'keveloper')
student4 = Student('slab', 'onDeck', 'bruh')

mo = Instructor('mo', 'money', 'Moooo', 'smart')
willy = Instructor('willy', 'metcalf', 'wizzle', 'raves')
william = Instructor('William', 'green', 'wgreen', 'being late')

cohort1.students.append(student1)
cohort2.students.append(student2)
cohort3.students.append(student3)
cohort3.students.append(student4)

cohort1.instructors.append(mo)
cohort2.instructors.append(willy)
cohort3.instructors.append(william)

william.assign_exercise(student1, bangazon)
william.assign_exercise(student1, nutshell)

mo.assign_exercise(student2, nutshell)
mo.assign_exercise(student2, reactnutshell)

willy.assign_exercise(student3, trestlebridge)
willy.assign_exercise(student3, reactnutshell)

william.assign_exercise(student4, bangazon)
william.assign_exercise(student4, trestlebridge)

all_students = [student1, student2, student3, student4]
all_exercises = [nutshell, reactnutshell, bangazon, trestlebridge]

for student in all_students:
  report = f'{student.first_name} is working on '
  student_working_exercises = set(student.exercises)
  exercises = set(all_exercises)
  exercise_list = list(student_working_exercises.intersection(exercises))
  for exercise in exercise_list:
    report += f'{exercise.name}, '
  report = report[slice(-2)] + f'.'
  print(report)
  print('')
  print('')
