formatter = "{} {} {} {}" #Esta línea es una variable que contiene llaves que se usarán mas adelante para colocar elementos dentro, ya sean strings, integers. Hay un elemento por cada llave.

#A continuación usaremos una "función" para convertir la variable "formatter" en otros elementos. El formatter.format() toma el string formatter de la primera linea y luego llama a la función format y pasa al formato 4 argumentos, por las 4 {} de la variable formatter. El resultado de llamar la función format en formatter es un nuevo string que tiene las {} reemplazadas con 4 variables. Esto es lo que print imprime al final.
print(formatter.format(1, 2, 3, 4)) #estos son los elementos en este caso, integers
print(formatter.format("one", "two", "three", "four")) #En este caso un string, cada string abarca todo lo que esté dentro de "" ya sea 1 o más palabras.
print(formatter.format(True, False, False, True)) #Los elementos también pueden ser booleans.
print(formatter.format(formatter, formatter, formatter, formatter)) #Estos elementos inclusive pueden ser variables, en este caso usamos la misma variable "formatter".
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) #Este es un ejemplo de que en cada espacio pueden ir variables palabras.
