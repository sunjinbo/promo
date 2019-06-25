class Station:
    def __init__(self, name):
        self.name = name
        self.promo = {}

    def add(self, weekday, schedule):
        if weekday in self.promo:
            del self.promo[weekday]
        self.promo[weekday] = schedule
