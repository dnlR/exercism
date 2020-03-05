class Matrix:
    def __init__(self, matrix_string):
        raw_rows = matrix_string.splitlines()
        row_matrix = []
        col_matrix = []

        for raw_row in raw_rows:
            row = list(map(int, raw_row.split(' ')))
            row_list = []
            col_matrix_idx = 0
            for num in row:
                row_list.append(num)
                try:
                    col_matrix[col_matrix_idx].append(num)
                except IndexError:
                    col_matrix.append([])
                    col_matrix[col_matrix_idx] = [num]
                col_matrix_idx += 1
            row_matrix.append(row_list)
        self.matrix_by_row = row_matrix
        self.matrix_by_column = col_matrix

    def row(self, index):
        return self.matrix_by_row[index - 1]

    def column(self, index):
        return self.matrix_by_column[index - 1]
