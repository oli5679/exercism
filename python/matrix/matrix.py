class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [[int(c) for c in row.split(' ')] for row in matrix_string.split('\n')] 
        
        self.columns = list(map(list, zip(*self.rows)))  

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
