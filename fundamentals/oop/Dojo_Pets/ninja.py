from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet_food -= 10
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self

    def print_food_list(self):
        if self.pet_food < 0:
            print("hunt some squirrels or he will eat you")


travis = Pet("Travis", "Crocodile", "Back-Flip", 300, 200)
larry = Ninja("Larry", "Behemoth", 20, 30, travis)


larry.bathe().feed().feed().feed().feed().walk().print_food_list()

travis.print_life()

