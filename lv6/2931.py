word = input()

newWord = word.replace('dz=', '!').replace('c=', '@').replace('c-', '#').replace('d-','$').replace('s=', '%').replace('z=', '^').replace('lj', '&').replace('nj', '*')

print(len(newWord))