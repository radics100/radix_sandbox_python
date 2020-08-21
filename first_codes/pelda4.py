x = [1, 'two', 3.0, [4, 'four'], 5]
y= [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(id(x))
print(id(y))

if isinstance(y, tuple):
    print("tuple")
elif isinstance(y, list):
    print('list')
else:
    print('nope')
    



print(type(x))

    

