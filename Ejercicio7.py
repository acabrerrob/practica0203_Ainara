alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet2 = []

for character in alphabet :
    if alphabet.index(character) % 3 != 0 :
        alphabet2.append(character)

print (alphabet2)