numbers = []

while True:
    lotteryNumber = int (input('Introduzca el número de  lotería ganador, si desea el resultado introduzca 0: '))

    numbers.append(lotteryNumber)

    if lotteryNumber == 0 :
        break

numbers.sort()

print(numbers)