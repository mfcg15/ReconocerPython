num1 = 42 #declaramos una variable de tipo int 
num2 = 2.3 #declaramos una variable de tipo float 
boolean = True #declaramos una variable de tipo boolean
string = 'Hello World' #declaramos una variable de tipo string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declaramos un lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declaramos un diccionario
fruit = ('blueberry', 'strawberry', 'banana') #declaramos una tupla
print(type(fruit)) #imprimimos en consola el tipo de variable que es "fruit"
print(pizza_toppings[1]) #imprimimos en consola el valor que se encuentra en la posicion 1 de la lista "pizza_toppings"
pizza_toppings.append('Mushrooms') #agregamos un nuevo valor a la lista "pizza_toppings"
print(person['name']) #imprimimos en consola el valor que se encuentra en el key "name"
person['name'] = 'George' #Modificamos el valor que se encuentra en el key "name"
person['eye_color'] = 'blue' #Modificamos el valor que se encuentra en el key "eye_color"
print(fruit[2])#imprimimos en consola el valor que se encuentra en la posicion 2 de la tupla "fruit"

if num1 > 45: #este if evalua si el valor de la variable num1 es mayor a 45, entonces imprime  "It's greater" si no "It's lower"
    print("It's greater")
else:
    print("It's lower")


if len(string) < 5:  
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

"""
#este if anidado evalua si el cantidad de caracteres que tiene el string si es menor a 5, imprime "It's a short word!" , si es mayor que 15
imrprime "It's a long word!" si no cumple con las otras dos condiciones entonces imprime "Just right!"
"""

for x in range(5): #este for imprime numeros del 0 al 4
    print(x)

for x in range(2,5): #este for imprime numeros del 2 al 4
    print(x)

for x in range(2,10,3): #este for imprime numeros del 2 al 9 pero de 3 en 3 
    print(x)

x = 0 #declaramos esta variable x en 0 para recorrer en el bucle while
while(x < 5): #este bucle while recorrera hasta el valor de x sea menor que 5 
    print(x) #imprimimos en consola el valor de la varible x 
    x += 1 #amentamos su valor de uno en uno 

pizza_toppings.pop() #quitamos el ultimo valor de la lista "pizza_toppings"
pizza_toppings.pop(1) #quitamos el valor que se encuentra en la posicion 1 de la lista "pizza_toppings"

print(person) #imprimimos en consola todo el diccionario person
person.pop('eye_color') #quitamos el key eye_color en el diccionario person
print(person) #imprimimos en consola todo el diccionario person

for topping in pizza_toppings: # recorrera toda la lista pizza_toppings
    if topping == 'Pepperoni': #si encuentra el valor Pepperoni continuara con el bucle pero no ejecura nada 
        continue
    print('After 1st if statement') #imprime en consola el mensaje.
    if topping == 'Olives':  #si encuentra el valor Olives sale del bucle
        break

def print_hello_ten_times(): # Define la funcion sin parametros y emprime en consola "Hello" 10 veces. 
    for num in range(10):
        print('Hello')

print_hello_ten_times() #Llamamos a la funcion "print_hello_ten_times()"

def print_hello_x_times(x): #Define la funcion con parametro y emprime en consola "Hello" la cantidad de veces que se el valor del parametro. 
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #Llamamos a la funcion "print_hello_x_times" con parametro 4 

def print_hello_x_or_ten_times(x = 10): #Define la funcion con parametro con valor 10 y emprime en consola "Hello" el valor del paramtro, es decir 10 veces.
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #Llamamos a la funcion "print_hello_ten_times() sin parametro, por lo que repite el valor predefinido"
print_hello_x_or_ten_times(4) #Llamamos a la funcion "print_hello_ten_times() con parametro 4, por lo que repite el valor mandado"


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)