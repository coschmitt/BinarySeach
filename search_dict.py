from sqlalchemy import create_engine, select, Table, MetaData, Column
from itertools import permutations


engine = create_engine("mysql+pymysql://root:{password}@localhost:3306/entries")

metadata = MetaData()

entries = Table('entries', metadata, autoload=True, autoload_with=engine)
stmt = select([entries.columns.word])
result = engine.execute(stmt).fetchall()


def find(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle][0]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint
    return None


def find_word(list, length=None):
    if not length:
        length = len(list)
    answers = []
    perm = permutations(list, length)

    for i in perm:
        word = ''.join(i)
        dictWord = find(result, word[0].upper() + word[1:len(word)])

        if dictWord is not None:
            answers.append(dictWord)
    return answers
