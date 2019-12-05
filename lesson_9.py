"""lst = [1,2,3]
for item in lst:
    print(item)
    print(item*100)
    input ()"""


"""for item in range (1,9,2):
    print (item)"""


"""import random
lst = []
for item in range(10):
    new_element = random.randint(0,9)
    lst.append(new_element)
print (lst)
lst.sort()
print (lst)"""


"""d = {980:'UAH', 840:'USD', 643:'RUB'}
for k, v in d.items ():
    print (f"{k}=>{v}")"""


"""f = open('text.txt')
persons = []
for line in f:
    new_line = line.split(';')
    d = {'name':new_line[0], 'price':new_line[1]}
    persons.append(d)
print (persons)"""


"""my_pass = ''
while my_pass != 'password':
    my_pass = input ('Введите пароль, пожалуйста: ')
print ('Поздравляю!')"""
