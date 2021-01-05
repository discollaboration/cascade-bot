
from discord.utils import get

def nameget(iterable, name):
    for item in iterable:
        if item.name == name:
            return item
    for item in iterable:
        if item.name.startswith(name):
            return item
    for item in iterable:
        if name in item.name:
            return item
    return None

def autoget(iterable, query):
    if type(query) == str:
        return nameget(iterable, name=query)
    elif type(query) == int:
        return get(iterable, id=query)
    return None