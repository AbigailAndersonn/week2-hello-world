# Abigail Anderson

print('Hello world!')

print('Choose a language and I will greet you in that language!')
print('1. Spanish')
print('2. French')
print('3. Japanese')

choice = int(input()) # user inputs number 1, 2, or 3

if choice == 1:
  print('Hola!')
elif choice == 2:
  print('Bonjour!')
elif choice == 3:
  print('Konnichiwa!')   # program greets user with language choosen as input
