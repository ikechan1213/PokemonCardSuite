from PokemonCardLibrary.card import Card
from PokemonCardLibrary.database import load_cards, save_cards

# 保存済みカードを読み込む
cards = load_cards()

print("=== カード登録 ===")
card_number = (input("カード番号："))
packid = input("パックID：")
name = input("カード名：")
evolution = input("進化：")
hp = int(input("HP："))
type = input("タイプ：")
rarity = input("レアリティ：")
pack = input("パック名：")
count = int(input("所持枚数："))

card = Card(
    card_number=card_number,
    packid=packid,
    name=name,
    hp=hp,
    type=type,
    rarity=rarity,
    pack=pack,
    count=count,
    evolution=evolution
)

cards.append(card)

save_cards(cards)

print(f"\n{name} を登録しました！")