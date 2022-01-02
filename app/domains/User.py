from dataclasses import dataclass

# O decorator adiciona um construtor para a classe automaticamente, bem como outros métodos (__repr__, etc)
@dataclass
class User(object):
    id: int
    name: str
    active: bool = True