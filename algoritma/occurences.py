from typing import List


def occurences(input: List, query: List):
    return [input.count(x) for x in query] 


if __name__ == "__main__":
    INPUT = ['xc', 'dz', 'bbb', 'dz']
    QUERY = ['bbb', 'ac', 'dz']
    print(occurences(INPUT, QUERY))
