class Employee:
    def __init__(self, fn, sn, sl):
        self.first_name = fn
        self.second_name = sn
        self.salary = sl

    def give_raise(self, bonus=5000):
        self.salary += bonus
