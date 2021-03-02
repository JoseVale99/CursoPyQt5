
# Exmaple I *args

def my_sum(*args):
    """my_sum () toma todos los parámetros que se proporcionan
     en la entrada y los empaqueta en un solo objeto iterable llamado args.
    """
    sum = 0
    for values in args:
        sum += values
    print("La suma es: ",sum)    

my_sum(1,2,3,4)

# Permite ver la documentación de nuestra función
print(my_suma.__doc__)

# Example II - **Kwargs

def Suma_Kwargs(**kwargs):
    print(kwargs)

Suma_Kwargs(a=4,b=5,c=6)

def Suma_Kwargs2(**kwargs):
    suma = 0
    for values in kwargs.values():
        suma += values
    print("suma ",suma)

Suma_Kwargs2(a=4,b=5,c=6)        






