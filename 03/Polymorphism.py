from abc import abstractmethod


class Animal(object):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def voice(self):
        raise NotImplementedError


class Cat(Animal):
    @property
    def name(self) -> str:
        return 'cat'

    def voice(self):
        print('Meow!')


class Dog(Animal):
    @property
    def name(self) -> str:
        return 'dog'

    def voice(self):
        print('Woof!')


class AnimalFactory(object):
    def __init__(self):
        self.__animals = [Cat(), Dog()]

    def get_animal(self, name: str) -> Animal | None:
        for a in self.__animals:
            if a.name is name:
                return a
        else:
            return None


if __name__ == '__main__':
    factory = AnimalFactory()

    animal: Animal = factory.get_animal('cat')
    print(animal.name)
    animal.voice()
