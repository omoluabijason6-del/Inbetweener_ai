from core.character_dna import CharacterDNA


class CharacterAgent:
    """
    Stores and manages Character DNA.
    """

    def __init__(self):
        self.name = "Character Agent"
        self.characters = {}

    def start(self):
        print("[Character] Ready.")

    def add_character(self, dna: CharacterDNA):
        self.characters[dna.name] = dna

        print(f"[Character] Loaded {dna.name}")

    def get_character(self, name):
        return self.characters.get(name)