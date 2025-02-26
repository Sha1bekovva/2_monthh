animals = ('tiger','cat','dog')
fruits = ('orange', 'tomato','apple','limon')

num = 0
while num < len(animals):
    for fruit in fruits:
        print(fruit)
    for animal in animals:
        print(animals)


    # print(f'{animal} loves {fruit}')

def counter(n):
    print(n)
    if n > 0:
        counter(n - 1)
