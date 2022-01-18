from dataclasses import dataclass

# O decorator adiciona um construtor para a classe automaticamente, bem como outros métodos (__repr__, etc)
class User():
    def __init__(self, name, active, id = -1):
        self.__id = id
        self.__name = name
        self.__active = active

    def deactivate(self):
        self.__active = False

    def activate(self):
        self.__active = True
