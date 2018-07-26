import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def titleList(listOfNames):
    return [name.title() for name in listOfNames]


def gen_pairs(listOfNames):
    firstNames = [name.split()[0] for name in listOfNames]
    while True:
        name1, name2 = None, None
        while name1 == name2:
            name1 = random.choice(firstNames)
            name2 = random.choice(firstNames)
        yield print(f"{name1} is paired with {name2}")


def main():
    titleNames = titleList(NAMES)
    pairs = gen_pairs(titleNames)
    for _ in range(10):
        next(pairs)


if __name__ == '__main__':
    main()
