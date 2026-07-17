from PokemonCardLibrary.card import Card
from PokemonCardLibrary.database import Database

# Database作成
db = Database()

# -------------------------
# テスト用カード作成
# -------------------------

card1 = Card(
    "999_001",
    "TEST",
    "ピカチュウ",
    "たね",
    60,
    "雷",
    "C",
    "テストパック",
    1
)

card2 = Card(
    "999_002",
    "TEST",
    "ライチュウ",
    "1進化",
    120,
    "雷",
    "U",
    "テストパック",
    2
)

# -------------------------
# 追加テスト
# -------------------------

print("=== add_card ===")

db.add_card(card1)
db.add_card(card2)

for card in db.get_all_cards():
    print(card)

# -------------------------
# 検索テスト
# -------------------------

print("\n=== search_name ===")

for card in db.search_name("ピカ"):
    print(card)

print("\n=== search_type ===")

for card in db.search_type("雷"):
    print(card)

print("\n=== search_rarity ===")

for card in db.search_rarity("C"):
    print(card)

print("\n=== search_pack ===")

for card in db.search_pack("テストパック"):
    print(card)

print("\n=== search_card_number ===")

for card in db.search_card_number("999_001"):
    print(card)

# -------------------------
# 更新テスト
# -------------------------

print("\n=== update_card ===")

updated = Card(
    "999_001",
    "TEST",
    "ピカチュウEX",
    "たね",
    200,
    "雷",
    "RR",
    "テストパック",
    5
)

db.update_card(updated)

for card in db.get_all_cards():
    print(card)

# -------------------------
# 削除テスト
# -------------------------

print("\n=== delete_card ===")

db.delete_card("999_002")
db.delete_card("999_001")
for card in db.get_all_cards():
    print(card)