#Ex 1:
def power(base: int, exponent=2):
    if exponent >= 0:
        return base**exponent
    return 1/base**-exponent

f1 = power

#Ex 2:
def scale(x, factor=1.2):
    return x*factor
h = 1
f2 = scale

def apply_all(funcs, value):
    list_of_values = []
    for f in funcs:
        list_of_values.append(f(value))
    return list_of_values
#Ex 3
def summarize(*number, **parameters):
    if number:
        somme = sum(number)
        moyenne = somme/len(number)

        for key, value in parameters.items():
            if value == True and type(value) == bool:
                return moyenne, somme
            if type(value) == int:
                return round(moyenne, value), round(somme, value)
    else:
        return "ERROR: Please enter a number"

print(summarize(2,3,4,5, precision= 4))
#Ex 4:
def append_item(lst, item):
    new_list = lst
    new_list.append(item)
    return new_list
def increment(n):
    n += 1
    return n

a = [1,2]
b = 5
print('a: ',a,',', 'b: ',b)
print(increment(b))
print(increment(b))
print('a: ',append_item(a,3),',', 'b: ',b)

#Ex 5:
counter = 0
def increase(n):
    global counter
    counter += n
    return counter
def local_increase(n):
    return counter + n

print(increase(5))
print(local_increase(5))
print(counter)
