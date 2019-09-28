cars = 100 #Asignar el valor int 100 a la variable cars
space_in_a_car = 4.0 #Asignar el valor float 4.0 a la variable cars
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #hallar la variable cars_not_driven restando
                                 #cantidad de carros con los conductores
cars_driven = drivers #carros conducidos es igual a la cantidad de conductores
carpool_capacity = cars_driven * space_in_a_car #la capacidad de Carpool
#es igual a los carros conducidos multiplicado por el espacio que tiene el carro
average_passengers_per_car = passengers / cars_driven #pasajeros por carro es la
#cantidad de pasajeros entre los carros conducidos considerando cantidad igual
#de pasajeros por carro
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


cars = 100 #Asignar el valor int 100 a la variable cars
space_in_a_car = 4 #Asignar el valor int 4 a la variable cars
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
