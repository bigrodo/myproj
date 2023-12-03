# Создание класса 'Tomato'
class Tomato:
    # Статическое свойство states, содержащее все стадии созревания помидора
    states = ['отсутсвует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index):
        # Два динамических свойства: _index (передается параметром) и _state (принимает первое значение из списка states).
        self._index = index
        self._state = self.states[0]

    def grow(self):
        # Метод grow() переводит томат на следующую стадию созревания.
        if self._state != self.states[-1]:
            current_state_index = self.states.index(self._state)
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        # Метод is_ripe() проверяет, что томат созрел.
        return self._state == self.states[-1]


# Класс TomatoBush
class TomatoBush:
    def __init__(self, tomato_count):
        # Метод init() принимает количество томатов и на его основе создает список объектов класса Tomato.
        self.tomatoes = [Tomato(index) for index in range(1, tomato_count + 1)]

    def grow_all(self):
        # Метод grow_all() переводит все объекты из списка томатов на следующий этап созревания.
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Метод all_are_ripe() возвращает True, если все томаты из списка стали спелыми.
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Метод give_away_all() очищает список томатов после сбора урожая.
        self.tomatoes.clear()


# Класс Gardener
class Gardener:
    def __init__(self, name, plant):
        # Два динамических свойства: name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush).
        self.name = name
        self._plant = plant

    def work(self):
        # Метод work() заставляет садовника работать, что позволяет растению становиться более зрелым.
        self._plant.grow_all()

    def harvest(self):
        # Метод harvest() проверяет, все ли плоды созрели. Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение.
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Не все плоды созрели, подождите еще немного.")

    @staticmethod
    def knowledge_base():
        # Статический метод knowledge_base() выводит в консоль справку по садоводству.
        print("Справка по садоводству:")
        print("1. Регулярно ухаживайте за томатами.")
        print("2. Удобряйте кусты по необходимости.")
        print("3. Проверяйте состояние плодов и собирайте урожай вовремя.")


# Тесты:
# 1) Вызов справки по садоводству.
Gardener.knowledge_base()

# 2) Создание объектов классов TomatoBush и Gardener.
tomato_bush = TomatoBush(5)
gardener = Gardener("Maxim", tomato_bush)

# 3) Уход за кустом с помидорами.
gardener.work()

# 4) Попытка собрать урожай, когда томаты еще не дозрели.
gardener.harvest()

# Продолжение ухода за кустом.
gardener.work()
gardener.work()

# 5) Сбор урожая.
gardener.harvest()

