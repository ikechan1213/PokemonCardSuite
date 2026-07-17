import json
import os
from PokemonCardLibrary.card import Card

# FILE_NAME = "cards.json"

class Storage:
    def __init__(self, file_name="cards.json"):
        self.file_name = file_name

    def load_cards(self):
        """cards.jsonからカード一覧を読み込む"""

        if not os.path.exists(self.file_name):
            return []

        with open(self.file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Card.from_dict(card) for card in data]


    def save_cards(self, cards):
        """カード一覧をcards.jsonへ保存"""

        data = [card.to_dict() for card in cards]

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)