import json
import os

from PokemonCardLibrary.card import Card

FILE_NAME = "cards.json"


def load_cards():
    """cards.jsonからカード一覧を読み込む"""

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Card.from_dict(card) for card in data]


def save_cards(cards):
    """カード一覧をcards.jsonへ保存"""

    data = [card.to_dict() for card in cards]

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)