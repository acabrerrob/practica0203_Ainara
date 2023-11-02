# Escribir un programa que pregunte al usuario los números ganadores
# de la lotería primitiva, los almacene en una lista y los muestre por
# pantalla ordenados de menor a mayor.
  
numbers = []
lotteryNumber = int (input('Introduzca el número de lotería ganador: '))

numbers.append(lotteryNumber)
print(numbers.sort())