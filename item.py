class Item():
    def __init__(self, item_name, item_mass = None, item_material = None ):
        self._name = item_name
        self._description = None
        self._mass = item_mass
        self._material = item_material
    
    def __eq__(self, other):
        return self._name == other
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, item_name):
        self._name = item_name
        
    @property
    def description(self):
        return self._description
    
    @name.setter
    def description(self, item_description):
        self._description = item_description

    @property
    def mass(self):
        return self._mass

    @name.setter
    def mass(self, item_mass):
        self._mass = item_mass    

    @property
    def material(self):
        return self._material

    @name.setter    
    def material(self, item_material):
        self._material = item_material

    def get_details(self):
        print(f"You see the {self._name}, it is {self._mass} and looks to be made from {self._material}.")
        print(f"It is {self._description}.")
