# Card.pyのテスト用ファイル

from PokemonCardLibrary.card import Card

card = Card(
    card_number="003_081",
    packid="M5",
    name="カリキリ",
    hp=70,
    type="草",
    rarity="C",
    pack="アビスアイ",
    count=1,
    evolution="たね"
)

print("----------")
print(card)
print("----------")
print(repr(card))
print("----------")
print(card.to_dict())
print("----------")