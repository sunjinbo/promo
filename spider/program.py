import time


class Program:
    def __init__(self, start, end, program_name):
        self.start_time = time.mktime(time.strptime(start, "%Y-%m-%d %H:%M"))
        self.end_time = time.mktime(time.strptime(end, "%Y-%m-%d %H:%M"))
        self.program_name = program_name

    def update(self, start, end, program_name):
        self.start_time = time.mktime(time.strptime(start, "%Y-%m-%d %H:%M"))
        self.end_time = time.mktime(time.strptime(end, "%Y-%m-%d %H:%M"))
        self.program_name = program_name

    def is_playing(self, current):
        current_time = time.mktime(time.strptime(current, "%Y-%m-%d %H:%M"))
        start_ticker = self.start_time.time()
        end_ticker = self.end_time.time()
        current_ticker = current_time.time()
        if start_ticker < current_ticker and end_ticker > current_ticker:
            return True
        else:
            return False

    def get_start_time(self):
        return time.strftime("%Y-%m-%d %H:%M", time.localtime(self.start_time))

    def get_end_time(self):
        return time.strftime("%Y-%m-%d %H:%M", time.localtime(self.end_time))

    def get_program_name(self):
        return self.program_name
