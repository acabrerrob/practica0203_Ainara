subjectsList = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
grades = []

for subject in subjectsList:
    grade = float (input(f'Introduzca la nota de {subject} '))

    grades.append(grade)

count = 0

for grade in grades :
        print (f'En {subjectsList[count]} has sacado {grade}')
        count +=1
