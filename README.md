# Pokémon Battle Simulator
#### Video Demo:  https://youtu.be/pxU8-dgARfU?si=t3f_T8ujinHXD4Ga
#### Description:
Welcome to **Pokémon Battle Arena**, a command-line Pokémon battle simulator written in Python!  
Choose any two Pokémon, select their moves, and watch them fight turn-by-turn — complete with type advantages, real damage calculation, colorful HP bars, and dramatic battle commentary.

This project was built as my **CS50P Final Project**.

---

## 🧩 Features

✅ Fetches real Pokémon data (stats, types, and moves) from [PokeAPI](https://pokeapi.co/)  
✅ Implements a **turn-based battle system**  
✅ Includes **type effectiveness** (super effective / not very effective)  
✅ Displays **colored HP bars** that dynamically change color as health decreases  
✅ Adds **dramatic messages and pauses** for immersive gameplay  
✅ Fully tested with **pytest** for reliability  

---

## 🧠 How It Works

1. The user enters two Pokémon names.
2. The program fetches their stats, types, and random moves from the [PokeAPI](https://pokeapi.co/).
3. Players take turns choosing a move.  
   Each attack uses the formula:

   ```
   damage = ((attack / defence) * (move_power / 2)) + 2
   ```

   A random factor (0.85–1.15×) adds unpredictability, and **type advantages** (1.5× or 0.5×) apply automatically.

4. HP bars update live after each attack.
5. The battle continues until one Pokémon faints!

---

## 🧰 Requirements

Install the dependencies first:

```bash
pip install requests art colorama pytest
```

---

## ▶️ How to Run

Run the simulator:

```bash
python project.py
```

Example gameplay:

```
POKEMON BATTLE ARENA !!!
Welcome to the Pokémon Battle Simulator!

Enter first Pokémon: pikachu
Enter second Pokémon: squirtle

🔥🔥🔥 Battle: Pikachu vs Squirtle 🔥🔥🔥

### Turn 1 ###
Pikachu used thunder-shock! ⚔️
It's super effective! ⚡
Squirtle HP: ████████---------
```

---

## ⚔️ Battle Mechanics

- **Move Selection:** Each Pokémon has 4 random moves from its full move list.
- **Damage Variation:** Random multiplier between 0.85–1.15 for realism.
- **Type System:** 1.5× damage for super effective moves, 0.5× for not very effective ones.
- **HP Bar:** Green → Yellow → Red based on remaining HP.
- **Battle Messages:** Delayed text using `time.sleep()` for dramatic pacing.

---

## 🧪 Testing

All tests are included in `test_project.py`.  
Run them with:

```bash
pytest test_project.py -v
```

### Tests Included

| Function | Description |
|-----------|--------------|
| `test_get_pokemon()` | Ensures valid Pokémon data fetched from API |
| `test_calculate_damage()` | Verifies damage returns a positive integer |
| `test_hp_bar_colors()` | Confirms HP bar renders correctly at all levels |

Example Output:
```
================ test session starts ================
collected 3 items
test_project.py::test_get_pokemon PASSED
test_project.py::test_calculate_damage PASSED
test_project.py::test_hp_bar_colors PASSED
================ 3 passed in 1.22s ==================
```

---

## 📁 Project Structure

```
📁 pokemon-battle-arena/
├── project.py          # main battle simulator
├── test_project.py     # pytest test suite
├── requirements.txt    # list of dependencies
└── README.md           # project documentation
```

---

## ⚙️ Technical Details

- **Language:** Python 3  
- **API:** [PokeAPI](https://pokeapi.co/)  
- **Libraries Used:**
  - `requests` → Fetch Pokémon data  
  - `art` → ASCII banner for intro  
  - `colorama` → Colorful HP bars and text  
  - `pytest` → Automated testing  

---

## 🏆 Example Battle

```
### Turn 1 ###
Pikachu used thunder-shock! ⚔️
It's super effective! ⚡
Squirtle HP: ████████---------
Squirtle used tackle! 💥
Pikachu HP: ██████------------
```

```
Oh, no...
It looks like...
Squirtle fainted! 💀
🏆🔥 Winner: Pikachu 🔥🏆
```

---

## 💡 Future Upgrades

✨ Add critical hits and status effects  
✨ Implement AI-controlled CPU opponents  
✨ Create a multiplayer mode  
✨ Display Pokémon sprites using Pillow  
✨ Log battles to a text file or card image  

---

## 📜 Academic Honesty Note

This project was completed as part of **CS50’s Introduction to Programming with Python (CS50P)**.  
All work presented here is my own, and no code was copied from unauthorized sources.

---

## 👨‍💻 Author

**Manish Bajracharya**  
CS50P Final Project — *Pokémon Battle Arena*  
📧 
