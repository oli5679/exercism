class Garden(object):
    def __init__(self, diagram, students=None):
        first_row, second_row = diagram.split('\n')
        self.first_row = first_row
        self.second_row = second_row
        if students is None:
            self.students = ['Alice', 'Bob', 'Charlie', 'David',
                            'Eve', 'Fred', 'Ginny', 'Harriet',
                            'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            self.students = sorted(students)
    
    def plants(self, student):
        plant_map = {
            'G': 'Grass',
            'C': 'Clover', 
            'R': 'Radishes', 
            'V': 'Violets',
        }
        try:
            student_index = self.students.index(student)
        except Exception as e:
            raise Exception('Invalid student')
        
        plant_keys = [
            self.first_row[2*student_index],
            self.first_row[2*student_index +1],
            self.second_row[2*student_index], 
            self.second_row[2*student_index +1],
            ]

        return [plant_map[k] for k in plant_keys]