types_of_people = 10
x = f"There are {types_of_people} types of people." #x es una variable string con variables incrustado

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #Otra vez variables incrustadas

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'") #Esto es un string con variables incrustadas

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" #se coloca {} para poder usar .format e incrustar la variable hilarious más adelante

print(joke_evaluation.format(hilarious)) #Utilizamos .format para incrustar al string la variable hilarious

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
