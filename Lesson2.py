class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born.')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if type(age) is int and age > 0:
            self.__age = age
        else:
            raise ValueError('age must be positive integer')

    def get_age(self):
        return self.__age

    def info(self):
        return f'{self.__name} is {self.__age} years old. Birth year: {2025 - self.__age}.'

    def make_voice(self):
        pass

class Fish(Animal):
    def __init__(self, name, age):
        super(Fish, self).__init__(name, age)


class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)

    def make_voice(self):
        print('Meow')


class Dog(Animal):
    def __init__(self, name, age, commands):
        # super().__init__(name, age)
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f' Commands: {self.__commands}.'

    def make_voice(self):
        print('Woof')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f' Wins: {self.__wins}.'

    def make_voice(self):
        print('Rrr woof')


# some_animal = Animal('Anim', 2)
# some_animal.set_age(3)
# print(some_animal.get_name())
# print(some_animal.info())

fish = Fish('Nemo', 1)

cat = Cat('Tom', 3)
# print(cat.info())

dog = Dog('Snoopy', 5, 'Sit')
dog.commands = 'Sit, run'
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('Reks', 2, 'Fight', 14)
# print(fighting_dog.info())

animals = [fish, cat, dog, fighting_dog]
for animal in animals:
    print(animal.info())
    animal.make_voice()