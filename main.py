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
cohort1.students.append(student1)
cohort1.students.append(student2)
cohort2.students.append(student3)
cohort3.students.append(student4)

mo = Instructor('mo', 'money', 'Moooo', 'smart')
willy = Instructor('willy', 'metcalf', 'wizzle', 'raves')
william = Instructor('William', 'green', 'wgreen', 'being late')

cohort1.instructors.append(mo)
cohort2.instructors.append(willy)
cohort3.instructors.append(william)

mo.assign_exercise(student1, nutshell)
mo.assign_exercise(student1, reactnutshell)
mo.assign_exercise(student2, bangazon)
mo.assign_exercise(student3, trestlebridge)
mo.assign_exercise(student4, trestlebridge)

students = []
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)

exercises = []
exercises.append(nutshell)
exercises.append(reactnutshell)
exercises.append(bangazon)
exercises.append(trestlebridge)

for student in students:
  print(f'{student.first_name} {student.last_name} is working on:')
  for exercise in student.exercises:
    print(f'{exercise.name}')
  print()
  