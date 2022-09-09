class Character:
    def __init__(self, name, synonyms, health, location, **kwargs):
        self.name = name
        self.synonyms = synonyms
        self.health = health
        self.location = location

        
class Player(Character):
    def __init__(self, name, synonyms, health, inventory, location, **kwargs):
        super().__init__(name, synonyms, health, location)
        self.name = name
        self.synonyms = synonyms
        self.health = health
        self.inventory = inventory
        self.location = location
        
class Npc(Character):
    def __init__(self, name, synonyms, health, inventory, location, description, **kwargs):
        super().__init__(name, synonyms, health, location)
        self.name = name
        self.synonyms = synonyms
        self.health = health
        self.inventory = inventory
        self.location = location
        self.description = description
