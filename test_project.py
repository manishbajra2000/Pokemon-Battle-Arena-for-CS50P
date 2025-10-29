from project import get_pokemon, simulate_battle, calculate_damage, hp_bar

#----- mock data -----
pikachu = {
    "name": "pikachu",
    "hp": 35,
    "attack": 55,
    "defence": 40,
    "types": ["electric"],
    "moves": ["thunder-shock", "quick-attack", "tackle"]
}

squirtle = {
    "name": "squirtle",
    "hp": 44,
    "attack": 48,
    "defence": 65,
    "types": ["water"],
    "moves": ["tackle", "bubble"]
}


#----- tests -----
def test_get_pokemon():
    result = get_pokemon("pikachu")
    assert result is not None
    assert "name" in result
    assert "hp" in result
    assert "attack" in result
    assert "defence" in result
    assert "types" in result
    assert "moves" in result
    assert isinstance(result["hp"], int)
    assert isinstance(result["attack"], int)
    assert isinstance(result["defence"], int)
    assert isinstance(result["types"], list)
    assert isinstance(result["moves"], list)
    assert len(result["moves"]) > 0


def test_calculate_damage():
    damage = calculate_damage(pikachu, squirtle, "thunderbolt")
    assert damage > 0


def test_hp_bar_colors():
    full = hp_bar(100, 100)
    mid = hp_bar(50, 100)
    low = hp_bar(10, 100)
    assert "█" in full
    assert "█" in mid
    assert "█" in low
    assert len(full) > 0