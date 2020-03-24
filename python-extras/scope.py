def swap(x, y):
    x, y = y, x
    print(f'x -> {x}, y -> {y}')

def test_swap():
    x, y = 2, 3
    print(f'x -> {x}, y -> {y}')
    x, y = y, x
    print(f'x -> {x}, y -> {y}')
    x,y = swap(x, y)
    print(f'x -> {x}, y -> {y}')

a = 99
def scope():
    print(f'a -> {a}')
    a = 3
    print(f'a -> {a}')

def test_scope():
    global NICKLE, DIME, QUARTER
    print(f'a -> {a}')
    a = 4
    print(f'a -> {a}')
    scope()
    print(f'a -> {a}')


'''
Write your comments in this string


'''
