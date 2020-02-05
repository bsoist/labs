def swap(x, y):
    x, y = y, x

def test_swap():
    x, y = 2, 3
    print(f'x -> {x}, y -> {y}')
    x, y = y, x
    print(f'x -> {x}, y -> {y}')
    swap(x, y)
    print(f'x -> {x}, y -> {y}')

a = 99
def scope():
    print(f'a -> {a}')
    a = 3
    print(f'a -> {a}')

def test_scope():
    print(f'a -> {a}')
    a = 4
    print(f'a -> {a}')
    scope()
    print(f'a -> {a}')


'''
Write your comments in this string


'''
