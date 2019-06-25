from program import Program


class Schedule:
    def __init__(self):
        self.data = []

    def add(self, start_time, end_time, program_name):
        program = Program(start_time, end_time, program_name)
        self.data.append(program)

    def delete(self, program_name):
        sum = len(self.data)
        for i in range(sum):
            if self.data[i] == program_name:
                del self.data[i]
                break

    def update(self, start_time, end_time, program_name):
        sum = len(self.data)
        for i in range(sum):
            if self.data[i] == program_name:
                self.data[i].update(start_time, end_time, program_name)
                break

    def get_all(self):
        return self.data
