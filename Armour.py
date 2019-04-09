class Armour:

    def __init__(self, armour_material, armour_type):
        self.armour_material = armour_material
        self.armour_type = armour_type
        self.armour_level = self.get_armour_level()

    def get_armour_level(self):
        return self.armour_type.value + self.armour_material.value

    def to_string(self):
        return self.armour_material.name.capitalize() + " " + self.armour_type.name.lower()
