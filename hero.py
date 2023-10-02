import random
import time

# Constants
LEVEL_TO_INDEX = {"Bronze": 0, "Silver": 1, "Gold": 2}
separator_width = 30

# Helper functions


def print_header(title):
    header = f" {title} ".center(separator_width, "-")
    print(header)


def print_spin_results(results, normal=True):
    if normal:
        print_header("SPIN RESULTS")
    else:
        print_header("FINAL SPIN RESULTS")
    print("| Column 1 | Column 2 | Column 3 | Column 4 | Player Wheel |")
    print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^13}|".format(
        results['column1'], results['column2'], results['column3'], results['column4'], results['player_wheel']))
    print("------------------------------------------")


# --------------------------------------------
#           Hero classes
# --------------------------------------------


class Hero:
    def __init__(self, symbol, owner=None):
        self.symbol = symbol
        self.energy = 0
        self.xp = 0
        self.level = "Bronze"  # can be Bronze, Silver, or Gold
        self.energy_requirements = []
        self.owner = owner
        self.reached_max_level = False

    def act_on_bulwark(self, player):
        # This will take care of the damage to the bulwark.
        player.bulwark_strength -= self.bulwark_damage[LEVEL_TO_INDEX[self.level]]
        if player.bulwark_strength < 0:
            player.bulwark_strength = 0
        print(
            f"{self.name} dealt {self.bulwark_damage[LEVEL_TO_INDEX[self.level]]} damage to the bulwark!")

    def act_on_crown(self, player):
        # This will deal damage directly to the crown.
        player.crown_health -= self.crown_damage[LEVEL_TO_INDEX[self.level]]
        if player.crown_health < 0:
            player.crown_health = 0
        print(
            f"{self.name} dealt {self.crown_damage[LEVEL_TO_INDEX[self.level]]} damage to the crown!")

    def gain_xp(self, amount):
        print(f"Gaining {amount} XP for {self.name} with symbol {self.symbol}")
        self.xp += amount

    def gain_energy(self, amount):
        self.energy += amount
        required_energy = self.energy_requirements[LEVEL_TO_INDEX[self.level]]
        print(
            f"Gaining {amount} energy for {self.name} with symbol {self.symbol}")
        if self.energy >= required_energy:
            self.energy = 0
            return True
        else:
            print(f"{self.name} doesn't have enough energy to act!")
            return False

    def level_up(self):
        if self.xp >= 6 and self.level == "Bronze":
            self.level = "Silver"
            print(f"{self.name} has leveled up to {self.level}")
            self.xp = 0
        elif self.xp >= 6 and self.level == "Silver":
            self.level = "Gold"
            print(f"{self.name} has leveled up to {self.level}")
            self.xp = 0
        elif self.xp >= 6 and self.level == "Gold":
            self.xp = 0
            print("Max Level Reached instead deal +2 damage to crown")
            self.reached_max_level = True

    def bonus_act(self, target):
        self.reached_max_level = False
        target.crown_health -= 2
        if target.crown_health < 0:
            target.crown_health = 0
        print(f"{self.name} dealt 2 damage to the crown!")


class Warrior(Hero):
    def __init__(self, symbol, owner=None):
        super().__init__(symbol, owner)
        self.name = "Warrior"
        self.crown_damage = [3, 5, 7]
        self.bulwark_damage = [3, 5, 5]
        self.energy_requirements = [3, 3, 3]

    def act(self, target):
        self.gain_xp(2)
        if target.bulwark_strength > 0:
            self.act_on_bulwark(target)
        else:
            self.act_on_crown(target)


class Mage(Hero):
    def __init__(self, symbol, owner=None):
        super().__init__(symbol, owner)
        self.name = "Mage"
        self.crown_damage = [2, 3, 3]
        self.bulwark_damage = [2, 3, 5]
        self.energy_requirements = [5, 4, 4]

    def act(self, target):
        self.gain_xp(2)
        if target.bulwark_strength > 0:
            self.act_on_bulwark(target)
        else:
            self.act_on_crown(target)
        # Second Attack
        self.act_on_crown(target)


class Archer(Hero):
    def __init__(self, symbol, owner=None):
        super().__init__(symbol, owner)
        self.name = "Archer"
        self.crown_damage = [3, 4, 6]
        self.bulwark_damage = [1, 2, 3]
        self.energy_requirements = [4, 3, 3]

    def act(self, target):
        self.gain_xp(2)
        if target.bulwark_strength > 0:
            if target.bulwark_strength <= 2:
                self.act_on_crown(target)
            else:
                self.act_on_bulwark(target)
        else:
            self.act_on_crown(target)


class Engineer(Hero):
    def __init__(self, symbol, owner=None):
        super().__init__(symbol, owner)
        self.name = "Engineer"
        self.crown_damage = [1, 2, 4]
        self.bulwark_damage = [3, 5, 5]
        self.energy_requirements = [4, 4, 3]

    def act(self, target):
        self.gain_xp(2)
        self.owner.award_bulwark(2)
        if target.bulwark_strength > 0:
            self.act_on_bulwark(target)
        else:
            self.act_on_crown(target)


class Assassin(Hero):
    def __init__(self, symbol, owner=None):
        super().__init__(symbol, owner)
        self.name = "Assassin"
        self.crown_damage = [1, 2, 2]
        self.delay = [1, 1, 2]
        self.energy_requirements = [3, 3, 3]

    def act(self, opponent):
        self.gain_xp(2)
        # Determine target hero
        target_hero = self.determine_target(opponent.heroes)
        energy_amount = self.delay[LEVEL_TO_INDEX[self.level]]
        # Reduce the energy of the target hero
        target_hero.energy -= energy_amount  # Or any other value you see fit

        # Deal damage to the crown
        self.act_on_crown(opponent)
        # Output for testing
        print(f"{self.name} attacked Enemy {target_hero.name}, reducing its energy.")

    def determine_target(self, opponent_heroes):
        # Get the hero with the least amount of energy left before acting.
        target = min(
            opponent_heroes, key=lambda hero: hero.energy_requirements[LEVEL_TO_INDEX[hero.level]] - hero.energy)
        return target


class Priest(Hero):
    def __init__(self, symbol, owner=None):
        super().__init__(symbol, owner)
        self.name = "Priest"
        self.healing = [1, 2, 2]
        self.grant_energy = [2, 2, 3]
        self.energy_requirements = [4, 3, 3]

    def act(self, target):
        self.gain_xp(2)
        self.heal_crown(self.owner)
        self.give_energy_to_fellow(self.owner)

    def heal_crown(self, player):
        amount_healed = self.healing[LEVEL_TO_INDEX[self.level]]
        player.crown_health += amount_healed
        if player.crown_health > 12:
            player.crown_health = 12

        print(f"{self.name} healed the crown by {amount_healed} points!")

    def give_energy_to_fellow(self, player):
        amount_granted = self.grant_energy[LEVEL_TO_INDEX[self.level]]
        # Determine the fellow hero (not the priest)
        fellow_hero = next(hero for hero in player.heroes if hero != self)
        fellow_hero.gain_energy(amount_granted)


# --------------------------------------------
#           Player and Wheel classes
# --------------------------------------------


class Player:
    def __init__(self, hero1=None, hero2=None):
        self.heroes = [hero1, hero2]
        self.crown_health = 10
        self.bulwark_strength = 0

    def spin_wheel(self, wheel):
        final_spin_results = {}

        column_map = {"1": "column1", "2": "column2",
                      "3": "column3", "4": "column4", "5": "player_wheel"}

        locked_wheels = {}  # Locked columns from previous spins

        for spin_number in range(3):
            print(f"\nSpin number {spin_number + 1}")
            spin_results = {}

            for column in wheel.wheels.keys():
                if column in locked_wheels:  # if column was locked before
                    spin_results[column] = locked_wheels[column]
                else:
                    spin_results[column] = wheel.spin()[column]

            # Check if it's the third spin, and if so, don't allow locking wheels.
            if spin_number == 2:
                # print("This is your final spin result!")
                break
            else:
                print_spin_results(spin_results)
                lock_decision = input(
                    "Which wheels would you like to lock? (comma separated, e.g., 1,2,3,4,5 or 'all' or 'none')")

                if lock_decision == "all":
                    locked_wheels.update(spin_results)
                elif lock_decision != "none":
                    for wheel_number in lock_decision.split(","):
                        if wheel_number in column_map:
                            column_name = column_map[wheel_number]
                            locked_wheels[column_name] = spin_results[column_name]

        final_spin_results.update(spin_results)
        # Add the final locked results
        final_spin_results.update(locked_wheels)
        print_spin_results(final_spin_results, normal=False)
        print()
        return final_spin_results

    def award_xp(self, spin_result):
        for _, panel in spin_result.items():
            if panel[-1] == "+":
                if "S" in panel:
                    self.heroes[0].gain_xp(1)
                elif "D" in panel:
                    self.heroes[1].gain_xp(1)

    def award_bulwark(self, amount):
        self.bulwark_strength += amount
        if self.bulwark_strength > 5:
            self.bulwark_strength = 5
        return self.bulwark_strength


class Wheel:
    def __init__(self, player_wheel_level="Copper"):
        self.wheels = {
            "column1": ["S", "D", "S", "S+", "D", "H", "DD+", "H"],
            "column2": ["S+", "D", "SS", "D+", "S", "H", "DD", "HH"],
            "column3": ["S+", "D", "D+", "S", "D", "HH", "SS", "HH"],
            "column4": ["S", "D", "S+", "D", "HH", "S", "D+", "HH"]
        }
        self.player_wheels = {
            "Copper": ["S", "D", "H", "Blank", "Blank", "S", "D", "Blank"],
            "Bronze": ["S", "D", "H", "Blank", "Blank", "S", "D", "HH"],
            "Silver": ["S", "D", "H", "Blank", "D", "SS+", "D", "HH"],
            "Gold": ["S", "DD+", "H", "S", "D", "SS+", "D", "HH"],
            "Diamond": ["S", "DD+", "HH", "SS", "DD", "SS+", "D", "HH"],
            "Platinum": ["S", "DD+", "HHH", "SS+", "DD+", "SS+", "D", "HH"]
        }
        self.wheels["player_wheel"] = self.player_wheels[player_wheel_level]

    def spin(self):
        result = {}
        for column, options in self.wheels.items():
            result[column] = random.choice(options)
        return result

# --------------------------------------------
#           Main game logic
# --------------------------------------------


class Game:
    def __init__(self):
        self.player = Player()
        self.npc = Player()
        self.player_hero1 = None
        self.player_hero2 = None
        self.npc_hero1 = None
        self.npc_hero2 = None
        self.wheel = Wheel()

    def calculate_resources(self, final_spin_result):
        def count_occurrences(symbol, sequence):
            return sum(1 for s in sequence if s.startswith(symbol))

        def compute_resource(symbol):
            count = count_occurrences(symbol, final_spin_result.values())
            double_symbol = symbol * 2
            triple_symbol = symbol * 3
            if double_symbol in final_spin_result.values():  # Double
                count += 1  # We add only one because the original two are already counted
            if triple_symbol in final_spin_result.values():  # Triple
                count += 2  # We add two because the original three are already counted

            # Minimum requirement of 3 of the type of resource for allocation
            return max(0, count - 2) if count >= 3 else 0

        squares_energy = compute_resource("S")
        diamonds_energy = compute_resource("D")
        hammers = compute_resource("H")

        return squares_energy, diamonds_energy, hammers

    def process_spin_result(self, player, result):
        # This will track XP earned during this call
        xp_earned = {"Square": 0, "Diamond": 0}

        # Process each column's result.
        for column, action in result.items():
            # If action has a '+' at the end, find the corresponding hero and update its XP.
            if action[-1] == "+":
                hero = None
                if "S" in action:
                    hero = player.heroes[0]
                elif "D" in action:
                    hero = player.heroes[1]

                if hero:
                    hero.gain_xp(1)
                    xp_earned[hero.symbol] += 1

        # Check if any hero levels up.
        for hero in player.heroes:
            hero.level_up()

        return xp_earned

    def select_heroes(self):
        hero_classes = {
            '1': Warrior,
            '2': Mage,
            '3': Engineer,
            '4': Assassin,
            '5': Priest
        }

        print("Choose your first hero:")
        for num, hero in hero_classes.items():
            print(f"{num}. {hero.__name__}")

        choice1 = input()
        while choice1 not in hero_classes:
            print("Invalid choice. Please choose again.")
            choice1 = input()

        # Remove the selected hero from available choices
        chosen_hero1 = hero_classes.pop(choice1)

        print("\nChoose your second hero:")
        for num, hero in hero_classes.items():
            print(f"{num}. {hero.__name__}")

        choice2 = input()
        while choice2 not in hero_classes:
            print("Invalid choice. Please choose again.")
            choice2 = input()

        chosen_hero2 = hero_classes[choice2]

        self.player_hero1 = chosen_hero1("Square", self.player)
        self.player_hero2 = chosen_hero2("Diamond", self.player)

    def assign_npc_heroes(self):
        available_heroes = [Warrior, Mage, Engineer, Assassin, Priest]
        npc_hero1 = random.choice(available_heroes)
        available_heroes.remove(npc_hero1)
        npc_hero2 = random.choice(available_heroes)
        self.npc_hero1 = npc_hero1("Square", self.npc)
        self.npc_hero2 = npc_hero2("Diamond", self.npc)

    def npc_turn(self):
        # Spin the wheel
        result = self.wheel.spin()
        print_spin_results(result)

        # Process XP, energy, and other resources for NPC based on the spin.
        self.process_spin_result(self.npc, result)
        squares_energy, diamonds_energy, hammers = self.calculate_resources(
            result)

        for hero in self.npc.heroes:
            if hero.reached_max_level:
                hero.bonus_act(self.player)

        # Award the NPC with resources
        if hammers:
            self.npc.award_bulwark(hammers)
            print(f"NPC's Bulwark increased by {hammers}")
        if squares_energy:
            if self.npc_hero1.gain_energy(squares_energy):
                self.npc_hero1.act(self.player)
        if diamonds_energy:
            if self.npc_hero2.gain_energy(diamonds_energy):
                self.npc_hero2.act(self.player)

        print(f"NPC's Crown Health: {self.npc.crown_health}")
        print(f"NPC's Bulwark Strength: {self.npc.bulwark_strength}")
        print()

    def game_start(self):
        print_header(
            "WELCOME TO THE GAME OF WHEELS")
        time.sleep(1)
        print("This game is inspired by the mini-game 'Wheels' from Sea of Stars")
        print(
            "The goal of the game is to destroy the enemy's crown before they destroy yours")
        print("Recreated by: Donovan Townes a.k.a Z8phyR")
        print("Have Fun!")
        time.sleep(2)
        print()
        while True:
            print_header("GAME START")
            self.select_heroes()
            self.assign_npc_heroes()

            print(
                f"Your heroes are {self.player_hero1.name} and {self.player_hero2.name}")
            print(
                f"NPC's heroes are {self.npc_hero1.name} and {self.npc_hero2.name}")

            self.player.heroes = [self.player_hero1, self.player_hero2]
            self.npc.heroes = [self.npc_hero1, self.npc_hero2]

            self.game_loop()

            play_again = input("Play again? (y/n)")
            if play_again != "y":
                print("Thanks for playing!")
                break

    def game_loop(self):
        while True:
            # Player's Turn
            input("Press Enter to spin the wheel!")

            final_spin_result = self.player.spin_wheel(self.wheel)
            time.sleep(1)
            print_header("SPIN RESULTS")

            # Adjust XP, energy, and other resources based on the spin.
            xp_earned = self.process_spin_result(
                self.player, final_spin_result)
            squares_energy, diamonds_energy, hammers = self.calculate_resources(
                final_spin_result)

            for hero in self.player.heroes:
                if hero.reached_max_level:
                    hero.bonus_act(self.npc)

            if hammers:
                self.player.award_bulwark(hammers)
                print(f"Bulwark increased by {hammers} ")
            if squares_energy:
                if self.player_hero1.gain_energy(squares_energy):
                    self.player_hero1.act(self.npc)
            if diamonds_energy:
                if self.player_hero2.gain_energy(diamonds_energy):
                    self.player_hero2.act(self.npc)

            # Simulate NPC Spin
            print()
            print_header("NPC TURN")
            self.npc_turn()
            print()

            # Print the results
            print_header("XP EARNED")
            print(f"Square: {xp_earned['Square']} XP")
            print(f"Diamond: {xp_earned['Diamond']} XP")
            print()

            print_header("HERO STATISTICS")
            print(
                f"Experience for {self.player_hero1.name}: {self.player_hero1.xp} XP")
            print(
                f"Experience for {self.player_hero2.name}: {self.player_hero2.xp} XP")
            print()

            print_header("HERO RANK")
            print(f"{self.player_hero1.name}: Rank {self.player_hero1.level}")
            print(f"{self.player_hero2.name}: Rank {self.player_hero2.level}")
            print()

            print_header("HERO ENERGY")
            print(f"{self.player_hero1.name}: {self.player_hero1.energy} energy")
            print(f"{self.player_hero2.name}: {self.player_hero2.energy} energy")
            print()

            print_header("PLAYER STATISTICS")
            print(f"Player's Crown Health: {self.player.crown_health}")
            print(f"Player's Bulwark Strength: {self.player.bulwark_strength}")
            print()

            print_header("END OF TURN")
            print()

            if self.npc.crown_health <= 0:
                print_header("YOU WIN!")
                break

            if self.player.crown_health <= 0:
                print_header("YOU LOSE!")
                break


if __name__ == "__main__":
    game = Game()
    game.game_start()
