# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
# sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
# has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
# cada una de las correspondientes notas introducidas por el usuario.
subjectsList = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
grades = []
for subject in subjectsList:
    grade = float (input(f'Introduzca la nota de {subject}'))

    grades.append(grade)


for grade in grades :
        print (f'En {subjectsList} has sacado {grade}')
# print('En ', subjectsList[0], 'has sacado ', grades[0])
# print('En ', subjectsList[1], 'has sacado ', grades[1])
# print('En ', subjectsList[2], 'has sacado ', grades[2])
# print('En ', subjectsList[3], 'has sacado ', grades[3])
# print('En ', subjectsList[4], 'has sacado ', grades[4])
