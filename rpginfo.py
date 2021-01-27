class RPGInfo():
    command = {"north" : "go north",
               "south" : "go south",
               "east"  : "go east",
               "west"  : "go west",
               "talk"  : "talk to something",
               "fight" : "have a fight an enemy",
               "info"  : "get information about the room",
               "feed"  : "feed an something",
               "hug"   : "hug something",
               "steal" : "steal something",
               "take"  : "take something",
               "help"  : "Shows a list of commands and what items you have"}
    
    storage = "walking chest"
    
    def __init__(self, game_title):
        self.title = game_title
        
    def welcome(self):
        print(f"Welcome to {self.title}")

    @classmethod    
    def rules(cls):
        print(f"\nYou need to defeat all enemies and collect all of the items, store your items in the {cls.storage}")

    @classmethod
    def commands(cls):
        print(f"To help you in your adventure, these are the commands you can use")
        for action in cls.command:
            print(f"{action:7} :- {cls.command[action]}")
    
        
    @staticmethod
    def info():
        print(f"Made using the RPi/FL OOP RPG game creater")
        
    @classmethod
    def credits(cls):
        print(f"Thank you for playing")
        print(f"Created by {cls.author}")