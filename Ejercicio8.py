word = input('Introduzca una palabra: ')
wordList = list(word)

wordList.reverse()

wordString = ''.join(wordList)

if wordString == word :
    print('Es palíndromo')
else :
    print('No es palíndromo')