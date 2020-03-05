class Matrix:
    def __init__(self, matrix_string):
        self.matrix_by_row = list(map(lambda row: list(map(int, row.split(' '))), matrix_string.splitlines()))

        row_length = len(self.matrix_by_row[0])
        columns_matrix = []
        for idx in range(0, row_length):
            column = [row[idx] for row in self.matrix_by_row]
            columns_matrix.append(column)

        self.matrix_by_column = columns_matrix

    def row(self, index):
        return self.matrix_by_row[index - 1]

    def column(self, index):
        return self.matrix_by_column[index - 1]
