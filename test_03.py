import string
step = 4
keys = list(string.ascii_lowercase) 
values = list(string.ascii_lowercase[step:] + string.ascii_lowercase[:step]) 
d = dict (zip(keys, values))
print ('Зашифрованное слово: ', d['h'], d['e'], d['l'], d['l'], d['o'])
