from base import Assert_tag
from .User import Person


class Elevator:

    def validate_inv(self, person: "Person"):
        a = {i.inv.__class__.__name__ for i in person.using_inv}

        if "Sanki" in a:
            return True
        if "Luji" in a and "Palki" in a:
            return True
        if "Snowboard" in a:
            return True
        return False


    def go_ride(self, person: Person):
        if self.validate_inv(person):
            for i in person.using_inv:
                i.inv.use_it()
            print(f'{person} ridden')
