from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, first, second):
        self.matrix1 = first
        self.matrix2 = second


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

    def __add__(self, other):
        lists = []
        if self.size() != other.size():
            raise MatrixError(self, other)
        for i in range(len(self.lists)):
            lists.append([])
            for j in range(len(self.lists[0])):
                lists[i].append(self.lists[i][j] + other.lists[i][j])
        return Matrix(lists)

    def __mul__(self, other):
        lists = []
        for i in range(len(self.lists)):
            lists.append([])
            for j in range(len(self.lists[0])):
                lists[i].append(self.lists[i][j] * other)
        return Matrix(lists)

    __rmul__ = __mul__

    def transpose(self):
        result = []
        for i in range(self.size()[1]):
            result.append([])
            for j in range(self.size()[0]):
                result[i].append(self.lists[j][i])
        self.lists = result
        return Matrix(result)

    @staticmethod
    def transposed(matrix):
        result = []
        for i in range(matrix.size()[1]):
            result.append([])
            for j in range(matrix.size()[0]):
                result[i].append(matrix.lists[j][i])
        return Matrix(result)


exec(stdin.read())
