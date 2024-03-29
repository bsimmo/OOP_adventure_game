class Character():
    """
    This class represents a Character, it is initialised by passing a name and description
    The properties conversation and and Item object can be set.

    """
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self._item = None

    """ Displays to the user a discription of the character"""
    def describe(self):
        print(f"{self.name} is here! {self.description}")

        if self._item is not None:
            print(f"They have a {self._item.name}")

    """ A function for setting what this character will say when talked to """
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def get_conversation(self):
        return self.conversation

    """ A method for returning and setting the Item the character is holding"""       
    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, item_name):
        self._item = item_name

    """If character has a conversation, display the result to the user"""    
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    """A standard character does not want to fight, polymorphed for a Enemy"""
    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True
    
    """If you try to steal of a normal character, it has to be the eexact item ot the player dies
        True/False returned to denote if succesful"""
    def steal(self, steal_item):
        if steal_item == self._item.name:
            print(f"You steal from {self.name}")
            #self._item = None
            return True
        else:
            # player dies if they try to steal a wrong item.
            print(f"You died trying to steal, they do not have a {steal_item}")
            return False



"""
The name of this new class is Enemy.
Putting Character inside the brackets tells Python that the Enemy class will inherit all of the methods from Character.
Character is called the superclass of Enemy, and Enemy is a subclass of Character.
Enemy can have it's weakness property set
"""
class Enemy(Character):
    #making the __init__ here stops it using the one from Character class
    def __init__(self, char_name, char_description):
        #so we need to tell it we still want to with super().
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness_name):
        self.weakness = weakness_name
        
    def get_weakness(self):
        return self.weakness
    
    """ A player fights an enemy to remove it from the game, they have to use the correct item or they die
       True/False returned to denote if succesful"""
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer")
            return False    

"""
An Animal class to create friendly creature to interact with
Poperties, huggable, the food they need and teh sound they make and corresponding functions to set and get these
"""
class Animal(Character):
    #making the __init__ here stops it using the one from Character class
    def __init__(self, char_name, char_description):
        #so we need to tell it we still want to with super().
        super().__init__(char_name, char_description)
        self.huggable = False
        self.hug_sound = None
        self.food = None
    
    def set_huggable(self, is_huggable):
        self.huggable = is_huggable
        
    def get_huggable(self):
        return self.huggable
    
    def set_hug_sound(self, sound):
        self.hug_sound = sound
        
    def get_hug_sound(self):
        return self.hug_sound
    
    def set_food(self, food):
        self.food = food
        
    def get_food(self):
        return self.food
    
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} cannot talk")

    """play a sound if hugged, if properties allow, 
    Retruen True/False to denote if hugged"""
    def hug(self):
        if self.huggable is not None:
            print(f"[{self.name}]: {self.hug_sound}")
            return True
        else:
            print(f"{self.name} does not like hugs")
            return False

    """A method to feed the animal, see if they like the food or not hungry
       True/False returned to denote if fed""" 
    def feed(self, food_item):
        if self.food is not None:
            if food_item == self.food:
                print(f"You fed {self.name} with {food_item}, {self.name} likes it a lot")
                return True
            else:
                print(f"{self.name} looks at you in disgust.")
                return False
        else:
            print(f"{self.name} is not hungry.")
            return False
        