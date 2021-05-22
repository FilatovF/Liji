from .base import Base


class Person:

    def __init__(self, first_name):
        self.first_name = first_name
        self.using_inv = []

    def take_inv(self, base):
        base: "Base"
        from lift import Elevator
        while not Elevator().validate_inv(self):
            cur_inv = base.give_inv(self)
            if cur_inv is None:
                break
            self.using_inv.append(cur_inv)
