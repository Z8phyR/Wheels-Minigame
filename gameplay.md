# Wheels Game Mechanics

**Setup:**

- Players start with two figurines: Warrior and Mage.
- They choose between Casual (randomized Champion figurines, 10 Gold reward) or Championship (set Champion figurines, rewards include new figurines or better wheels).
- Six total figurines and six player wheel levels: Copper, Bronze, Silver, Gold, Diamond, and Platinum.

**Gameplay:**

1. Players pick two figurines, designating one as Squares and the other as Diamonds.
2. Players see the Champion's chosen figurines.
3. Rounds involve spinning wheels (up to three times). The goal is to lock in desired panels. Spinning results in Squares, Diamonds, Hammers, or blanks (on lower level wheels).
   - **Squares & Diamonds:** Grant energy for Heroes to act.
   - **Hammers:** Build Bulwark, a defensive shield.
4. Some Square and Diamond panels have stars, granting 1 XP to associated Heroes. Heroes also gain 2 XP after acting. At 6 XP, Heroes either upgrade (Silver then Gold rank) or send a bomb. Gold rank Heroes send bombs at 6 XP.

**Hero Mechanics:**

- Heroes gain energy from final wheel spins. Need 3+ symbols for energy, calculated as (symbols - 2).
- Heroes can act by attacking or other special actions. They can upgrade, thereby altering their effectiveness and energy requirements.
  **Priest:** Gives energy instead of attacking.
  **Assassin:** Damages enemy's Crown directly.
  **Engineer:** Targets Bulwark primarily.
  **Archer:** Targets Crown primarily.

**Bulwark Mechanics:**

- Built from Hammers, provides protection for the Crown.
- Maximum height/health is 5.
- Engineer can also build Bulwark.
- Attacks need to surpass Bulwark's height to damage the Crown, or use special means (Assassin, Mage, or bombs).

**Winning:**

- Reduce opponent Crown's HP to zero.
- Both players start with 10 Crown HP.
- If both players reach 0 HP in a round, it's a tie.
- Only Priests can heal the Crown (up to 12 HP).

**Turn Order:**

1. Grant XP from panels.
2. Add Hammers.
3. Add energy.
4. Assassin acts.
5. Priest acts (heals, then gains XP).
6. Engineer acts.
7. Deploy bombs.
8. Remaining Heroes act.
9. Priest grants energy.
10. Heroes act from priest's energy.
11. Deploy bombs if applicable.
12. Check for 0 Crown HP.

**Wheel Mechanics:**

- Wheels have 8 panels.
- Players have four consistent wheels and one varying wheel.
- Champions' wheels are randomized.
- Wheel 5 varies by player's level, with outcomes improving at higher levels.

## Heroes

### Warrior

| Level  | Figurine       | Energy to Act |
| ------ | -------------- | ------------- |
| Bronze | Warrior Bronze | 3             |
| Silver | Warrior Silver | 3             |
| Gold   | Warrior Gold   | 3             |

**Description**: A steady and moderately fast damage dealer. Since damage doesn't carry over, this one is easily blocked by the Bulwark.

|        | Crown | Bulwark |
| ------ | ----- | ------- |
| Bronze | 3     | 3       |
| Silver | 5     | 5       |
| Gold   | 7     | 5       |

---

### Mage

| Level  | Figurine    | Energy to Act |
| ------ | ----------- | ------------- |
| Bronze | Mage Bronze | 5             |
| Silver | Mage Silver | 4             |
| Gold   | Mage Gold   | 4             |

**Description**: Attacks twice. The first fireball is at ground level and easily blocked by the Bulwark, while the second fireball flies at a height of 6 units, guaranteeing a hit on the Crown even if the Bulwark is maxed out.

|        | Crown | Bulwark |
| ------ | ----- | ------- |
| Bronze | 2     | 2       |
| Silver | 3     | 3       |
| Gold   | 3     | 5       |

---

### Archer

| Level  | Figurine      | Energy to Act |
| ------ | ------------- | ------------- |
| Bronze | Archer Bronze | 4             |
| Silver | Archer Silver | 3             |
| Gold   | Archer Gold   | 3             |

**Description**: Strong against Crown, weak against Bulwark. The arrow flies at a height of 3 units, hitting the Crown when the Bulwark is at 2 or less.

|        | Crown | Bulwark |
| ------ | ----- | ------- |
| Bronze | 3     | 1       |
| Silver | 4     | 2       |
| Gold   | 6     | 3       |

---

### Engineer

| Level  | Figurine        | Energy to Act |
| ------ | --------------- | ------------- |
| Bronze | Engineer Bronze | 4             |
| Silver | Engineer Silver | 4             |
| Gold   | Engineer Gold   | 3             |

**Description**: Strong against Bulwark, weak against Crown. As a bonus, the engineer raises its team Bulwark by 2 units whenever it acts.

|        | Crown | Bulwark |
| ------ | ----- | ------- |
| Bronze | 1     | 3       |
| Silver | 2     | 5       |
| Gold   | 4     | 5       |

---

### Assassin

| Level  | Figurine        | Energy to Act |
| ------ | --------------- | ------------- |
| Bronze | Assassin Bronze | 3             |
| Silver | Assassin Silver | 3             |
| Gold   | Assassin Gold   | 3             |

**Description**: Specialist Hero. Attacks delay the opponent's Hero with the least amount of energy left before acting. Also deals low damage to the Crown directly, disregarding Bulwark.

|        | Delay | Crown |
| ------ | ----- | ----- |
| Bronze | 1     | 1     |
| Silver | 1     | 2     |
| Gold   | 2     | 2     |

---

### Priest

| Level  | Figurine      | Energy to Act |
| ------ | ------------- | ------------- |
| Bronze | Priest Bronze | 4             |
| Silver | Priest Silver | 3             |
| Gold   | Priest Gold   | 3             |

**Description**: Support Hero. Heals its team's Crown, and gives energy to its fellow Hero.

|        | Healing | Energy |
| ------ | ------- | ------ |
| Bronze | 1       | 2      |
| Silver | 2       | 2      |
| Gold   | 2       | 3      |

---
