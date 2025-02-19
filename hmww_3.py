class Computer:
    def __init__(self,  memory, cpu):
        self.__memory = memory
        self.__cpu = cpu

    def __str__(self):
        return f'CPU {self.__cpu} memory {self.__memory}'



    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    @property
    def cpu (self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__memory = value

    def make_computation(self):
        return self.__memory * self.__cpu

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

class Phone:

    def __init__(self,sim_card_list):
        self.__sim_card_list = sim_card_list

    def __str__(self):
        return f'sim_card_list {self.__sim_card_list}'

    @property
    def sim_card_list(self):
        return  self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_num):
        if sim_card_number ==1:
            return (f'звонок идет на номер {call_to_num} с сим карты {sim_card_number}'
                    f'- {self.__sim_card_list[0]}')

        elif sim_card_number ==2:
            return (f'звонок идет на номер {call_to_num} с сим карты {sim_card_number}'
                    f'- {self.__sim_card_list[1]}')

class Smartphone(Computer,Phone):
    def __init__(self, memory ,cpu ,sim_card_list):
        Computer.__init__(self, memory, cpu)
        Phone.__init__(self.sim_card_list)


    def use_gps(self,location):
        return (f"чтобы дойти до {location}, сядтье на автобус 51\n"
              f"выйти на остановке 'Третьяковской'\n"
              f"пройти на восток по улице 'Койбагарова' \n"
              f"на перекрестке пройти налево. Вы подошли до пункта назначения {location}")


    def __str__(self):
        return  super().__str__() + f' ,sim_card_list: {self.sim_card_list}'

acer = Computer(64,16)
nokia = Phone(['Beeline', 'MegaCom'])
pocox3 = Smartphone(32,8,['0','MegaCom'])
iphone = Smartphone(42, 21,['Beeline', 'MegaCom'])

print(acer)
print(nokia)
print(pocox3)
print(iphone)

print(pocox3.use_gps('School #37'))
print(acer.make_computation())
print(nokia.call(1,992372878))
print(nokia.call(2, 99255436))

print(acer>iphone)
print(acer<pocox3)
print(acer>=pocox3)
print(acer<=pocox3)
print(acer!=iphone)
print(acer==pocox3)

