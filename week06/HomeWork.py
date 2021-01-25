from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    '''
    variety: eat_meat, other, etc. .
    figure: big(2), middle(1), small(0).
    character: savage, other, etc. .
    '''
    def __init__(self, variety, figure, character):
        self.variety = 'other'
        self.figure = 0
        self.character = 'other'
    @property
    def is_beast(self):
        if self.variety == 'eat_meat' and self.figure >= 1 and self.character == 'savage':
            return True
        else:
            return False


class Cat(Animal):
    sound = 'miao~'
    def __init__(self, name, variety, figure, character):
        super().__init__(variety, figure, character)
        self.name = name
    @property
    def is_pet(self):
        if self.is_beast:
            return False
        else:
            return True
    # @classmethod
    # def get_sound_(cls):
    #     return cls.sound


class Dog(Animal):
    sound = 'woof~'
    def __init__(self, name, variety, figure, character):
        super().__init__(variety, figure, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_beast:
            return False
        else:
            return True


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
    def add_an_animal_type(self, animal_to_add=None):
        if not hasattr(self, animal_to_add.__class__.__name__):
            setattr(self, animal_to_add.__class__.__name__, 1)


if __name__ == "__main__":
    z = Zoo('时间动物园')

    cat1 = Cat('mimi', 'eat_meat', 0, 'other')

    z.add_an_animal_type(cat1)

    have_cat = hasattr(z, 'Cat')