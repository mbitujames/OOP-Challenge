class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.age = 0  # in virtual days
        self.health = 10  # 0-10 scale
        
    def eat(self, food="pet food"):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        self.health = min(10, self.health + 0.5)
        print(f"🍖 {self.name} ate some {food}. Yummy!")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        self.hunger = min(10, self.hunger + 1)
        self.age += 1  # each sleep counts as a day
        print(f"💤 {self.name} took a nap and feels refreshed!")
        
    def play(self, game="fetch"):
        if self.energy < 2:
            print(f"😴 {self.name} is too tired to play right now.")
            return
            
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"🎾 {self.name} played {game} with you! So fun!")
        
    def train(self, trick):
        if self.energy < 1:
            print(f"😴 {self.name} is too tired to learn right now.")
            return
            
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)
        print(f"🎓 {self.name} learned a new trick: {trick.upper()}!")
        
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet. Try training them!")
        else:
            print(f"🎪 {self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"  {i}. {trick.capitalize()}")
    
    def get_status(self):
        print(f"\n📊 {self.name}'s Status ({self.pet_type.capitalize()}):")
        print(f"🍽️  Hunger: {'♥' * self.hunger}{'♡' * (10 - self.hunger)}")
        print(f"⚡ Energy: {'♥' * self.energy}{'♡' * (10 - self.energy)}")
        print(f"😊 Happiness: {'♥' * self.happiness}{'♡' * (10 - self.happiness)}")
        print(f"🏥 Health: {'♥' * int(self.health)}{'♡' * (10 - int(self.health))}")
        print(f"📅 Age: {self.age} virtual days")
        
    # Extra creative methods
    def bathe(self):
        self.happiness = max(0, self.happiness - 1)
        self.health = min(10, self.health + 1)
        print(f"🚿 {self.name} got a bath! They're clean but not thrilled about it.")
        
    def exercise(self):
        if self.energy < 3:
            print(f"😴 {self.name} is too tired to exercise.")
            return
            
        self.energy = max(0, self.energy - 3)
        self.hunger = min(10, self.hunger + 2)
        self.health = min(10, self.health + 1)
        print(f"🏃 {self.name} went for a run! Getting stronger!")
        
    def celebrate_birthday(self):
        self.age += 365
        self.happiness = 10
        print(f"🎂 Happy Birthday {self.name}! 🎉")