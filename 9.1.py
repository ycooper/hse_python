from sys import stdin
import copy


class Matrix:
    def __init__(self, input_list):
        self.lists = copy.deepcopy(input_list)

    def __str__(self):
        result = ""
        for l in self.lists:
            result += "\t".join(map(str, l)) + "\n"
        return result[:-1]

    def size(self):
        return len(self.lists), len(self.lists[0])


exec(stdin.read())
