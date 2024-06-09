def character_count(word):
    character_statistics = {}
    for character in word:
        if character in character_statistics:
            character_statistics[character] += 1
        else:
            character_statistics[character] = 1
    return character_statistics

if __name__ == "__main__":
    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count("smiles"))