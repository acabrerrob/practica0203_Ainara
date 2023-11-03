subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
grades = []

for subject in subjects:
    grade = float(input(f"Ingrese la nota que obtuvo en {subject}: "))
    grades.append(grade)
 

suspense = []

for position in range(len(subjects)):
    if grades[position] < 5:
        suspense.append(subjects[position])

if len(suspense) != 0 :
    print('Has de repetir las siguientes asignaturas: ' ) 
    print(suspense) 
else :
    print('Felicidades, aprobaste todo.')
