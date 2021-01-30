def mymap(func, iterator):
    return (func(it) for it in iterator)

def func(x):
    return x

for i in mymap(func, [1,2,3]):
    print(i)