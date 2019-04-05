print("How old are you?", end=' ') #Le dice a la función print no terminar la linea con un caracter de nueva línea sino terminar como lo indica entre los ' '.
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.") #Uso de f para reconocer las variables dentro de las {}.
