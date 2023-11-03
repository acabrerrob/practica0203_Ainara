word = input("Ingresa una palabra: ")

vocals = ["a","e","i","o","u"]

for vocal in vocals:
    letterCount = word.count(vocal)
    print(f"El numero de veces que aparece la letra {vocal} es de: {letterCount}")