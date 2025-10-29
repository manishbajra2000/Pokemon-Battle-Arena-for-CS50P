import requests
import random
import time
import art
from colorama import Fore, Style

TYPE_ADVANTAGES = {
    "normal": [],
    "fire": ["grass", "bug", "ice", "steel"],
    "water": ["fire", "rock", "ground"],
    "electric": ["water", "flying"],
    "grass": ["water", "rock", "ground"],
    "ice": ["grass", "ground", "flying", "dragon"],
    "fighting": ["normal", "rock", "ice", "dark", "steel"],
    "poison": ["grass", "fairy"],
    "ground": ["fire", "electric", "rock", "poison", "steel"],
    "flying": ["grass", "fighting", "bug"],
    "psychic": ["fighting", "poison"],
    "bug": ["grass", "psychic", "dark"],
    "rock": ["fire", "ice", "flying", "bug"],
    "ghost": ["psychic", "ghost"],
    "dragon": ["dragon"],
    "dark": ["psychic", "ghost"],
    "steel": ["ice", "rock", "fairy"],
    "fairy": ["fighting", "dragon", "dark"],
}


def main():
    art.tprint("POKEMON BATTLE ARENA !!!", font="bulbhead")
    print("\nWelcome to the Pokémon Battle Simulator!\n")

    while True:
        p1_name = input("Enter first pokemon: ").strip().lower()
        p2_name = input("Enter second pokemon: ").strip().lower()
        print()
        p1 = get_pokemon(p1_name)
        p2 = get_pokemon(p2_name)
        if not p1 or not p2:
            print("Couldn't find that pokemon. Choose again!\n")
            continue
        break

    print(f"🔥🔥🔥 Battle: {p1['name'].title()} vs {p2['name'].title()} 🔥🔥🔥\n")
    print(f"{p1['name'].title()} HP{hp_bar(p1['hp'],p1['hp'])}{p1['hp']}")
    print(f"{p2['name'].title()} HP{hp_bar(p2['hp'],p2['hp'])}{p2['hp']}")
    print()
    winner = simulate_battle(p1, p2)

    print(f"🏆🔥 Winner: {winner['name'].title()} 🔥🏆\n")


def get_pokemon(pok_name):
    # Fetch pokemon data (name, hp, attack, defence, type) from PokeAPI.
    # Returns dict or None if not available
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pok_name}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        types = []
        for type in data["types"]:
            types.append(type["type"]["name"])

        all_moves = []
        for move in data["moves"]:
            all_moves.append(move["move"]["name"])

        moves = random.sample(all_moves, min(4, len(all_moves)))
        pokemon = {
            "name": data["name"],
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defence": data["stats"][2]["base_stat"],
            "types": types,
            "moves": moves,
        }
        # print(pokemon)
        return pokemon

    except Exception as e:
        print(f"Error fetching {pok_name}: {e}")
        return None


def simulate_battle(pok1, pok2):
    # turn-based battle
    # each pokemon attacks until one of them have hp <= 0
    # return the winner pokemon dict
    hp1 = pok1["hp"]
    hp2 = pok2["hp"]

    turn = 1
    while hp1 > 0 and hp2 > 0:
        print(f"### Turn {turn} ###\n")

        ### Pokemon1 turn

        ## show moves
        print(f"{pok1['name'].title()} moves:")
        for i in range(len(pok1["moves"])):
            print(f"{i+1}: {pok1['moves'][i]}")

        # get a move
        plays1 = input(f"\nWhat will {pok1['name'].title()} do? ").strip()
        if plays1 not in pok1["moves"]:
            print("Invalid move!!! You fumbled!")
            plays1 = random.choice(pok1["moves"])
        print(f"{pok1['name'].title()} used {plays1}! ⚔️")

        # calculate damage
        dmg1 = calculate_damage(pok1, pok2, plays1)
        hp2 -= dmg1
        hp_bar_1 = hp_bar(hp2, pok2["hp"])
        time.sleep(0.5)
        print(
            f"{pok1['name'].title()} dealt {dmg1} damage to {pok2['name'].title()}!\n"
        )
        time.sleep(0.5)
        print(f"{pok2['name'].title()} HP:{hp_bar_1}")

        # if fainted
        if hp2 <= 0:
            print("Oh, no...")
            time.sleep(0.5)
            print("It looks like...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print(f"{pok2['name'].title()} fainted! 💀")
            time.sleep(1)
            print()
            return pok1
        time.sleep(0.5)
        print()

        ### Pokemon2 turn

        ## show moves
        print(f"{pok2['name'].title()} moves:")
        for i in range(len(pok2["moves"])):
            print(f"{i+1}: {pok2['moves'][i]}")

        # get a move
        plays2 = input(f"\nWhat will {pok2['name'].title()} do? ").strip()
        if plays2 not in pok2["moves"]:
            print("Invalid move!!! You fumbled!")
            plays2 = random.choice(pok2["moves"])
        print(f"{pok2['name'].title()} used {plays2}! ⚔️")

        # calculate damage
        dmg2 = calculate_damage(pok2, pok1, plays2)
        hp1 -= dmg2
        hp_bar_2 = hp_bar(hp1, pok1["hp"])
        time.sleep(0.5)
        print(
            f"{pok2['name'].title()} dealt {dmg2} damage to {pok1['name'].title()}!\n"
        )
        time.sleep(0.5)
        print(f"{pok1['name'].title()} HP:{hp_bar_2}")

        # if fainted
        if hp1 <= 0:
            print("\nOh, no...")
            time.sleep(1)
            print("It looks like...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print(f"{pok1['name'].title()} fainted! 💀")
            time.sleep(1)
            print()
            return pok2
        time.sleep(0.5)
        print()

        # next turn
        turn += 1
        print()
        time.sleep(0.5)


def calculate_damage(attacker, defender, move):
    url_move = f"https://pokeapi.co/api/v2/move/{move}"
    response_move = requests.get(url_move)
    response_move.raise_for_status()
    data_move = response_move.json()

    move_type = data_move["type"]["name"]
    move_power = data_move["power"] or 40

    # basic pokemon battle formula: ((attact_stat / defend_stat) * power) * random factor
    base_damage = ((attacker["attack"] / defender["defence"]) * (move_power / 2)) + 2
    random_factor = random.uniform(0.85, 1.15)
    damage = base_damage * random_factor

    # apply type advantage
    defender_type = defender["types"][0]
    if defender_type in TYPE_ADVANTAGES[move_type]:
        damage *= 1.5
        time.sleep(0.5)
        print(Fore.CYAN + "It's super effective!" + Style.RESET_ALL)
    if move_type in TYPE_ADVANTAGES[defender_type]:
        damage *= 0.5
        time.sleep(0.5)
        print(Fore.MAGENTA + "It's not very effective..." + Style.RESET_ALL)

    return round(damage)


def hp_bar(current_hp, max_hp, length=20):
    # returns visual colored HP Bar as a string
    ratio = max(0, current_hp) / max_hp
    filled_length = int(length * ratio)
    empty_length = length - filled_length

    if ratio > 0.6:
        color = Fore.GREEN
    elif ratio > 0.3:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    return f"{color}{'█'*filled_length}{'-'*empty_length}{Style.RESET_ALL}"


if __name__ == "__main__":
    main()
