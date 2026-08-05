#Task: A-Z
#use loops and strings to return A-Z
'''
import string
print('A-Z in alphabets')
for i in string.ascii_uppercase:
    print(i)
def get_alphabet():
    result=""
    for i in range(26):
        result += chr(65 + i)+" "
    return result
print(get_alphabet())'''
#Hippopotamus
#observe +ve,+ve,-ve,-ve&+ve,-ve all possibilities
animal='Hippopotamus'
print(animal)
print(len(animal))
#positivity
print(animal[:])
print(animal[3:])
print(animal[:4])
#Negativity
print(animal[-4:])
print(animal[:-3])
#positivity,Negativity
print(animal[2:-4])
print(animal[-1:2])
print(animal[3::-2])

    
