# storage.pyのテスト用ファイル
from PokemonCardLibrary.card import Card
from PokemonCardLibrary.storage import Storage

storage = Storage("test_cards.json")

cards = [
    Card("003_081", "M5", "カリキリ", "たね", 70, "草", "C", "アビスアイ", 1),
    Card("004_081", "M5", "ラランテス", "1進化", 260, "草", "RR", "アビスアイ", 1)
]

storage.save_cards(cards)

loaded_cards = storage.load_cards()

for card in loaded_cards:
    print(card)
    print(card.to_dict())

storage = Storage("not_exist.json")

cards = storage.load_cards()

print(cards)