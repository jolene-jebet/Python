#!/usr/bin/env python3

class Superhero:
    def __init__(self, name, power_level=50):
        self.name = name
        self.power_level = power_level
        self.energy = 100
    
    def move(self):
        return f"{self.name} moves with agility!"
    
    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} uses their power!"
        return f"{self.name} is too tired!"
    
    def __str__(self):
        return f"{self.name} (Power: {self.power_level})"

class FlyingHero(Superhero):
    def move(self):
        return f"{self.name} soars through the sky! ✈️"
    
    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} attacks from the air! 💨"
        return f"{self.name} needs to land!"

class SpeedHero(Superhero):
    def move(self):
        return f"{self.name} runs at super speed! 💨"
    
    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} creates speed vortexes! ⚡"
        return f"{self.name} is moving slowly!"

class StrengthHero(Superhero):
    def move(self):
        return f"{self.name} leaps buildings! 🏢"
    
    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} lifts massive objects! 💪"
        return f"{self.name} is too weak!"

def main():
    # Create heroes
    heroes = [
        FlyingHero("Sky Guardian", 75),
        SpeedHero("Lightning Bolt", 70),
        StrengthHero("Titan Force", 85)
    ]
    
    print("🦸 Superhero Team:")
    for hero in heroes:
        print(f"• {hero}")
    
    print("\n🎭 Movement Demo (Polymorphism):")
    for hero in heroes:
        print(f"• {hero.move()}")
    
    print("\n⚡ Power Demo:")
    for hero in heroes:
        print(f"• {hero.use_power()}")

if __name__ == "__main__":
    main()