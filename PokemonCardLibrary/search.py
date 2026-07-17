def search_name(cards, keyword):
        # カードをカード名(ポケモンの名前等)で検索する
        return [card for card in cards if keyword.lower() in card.name.lower()]

def search_type(cards, card_type):
        # カードをタイプで検索する
        return [card for card in cards if card.type.lower() == card_type.lower()]

def search_rarity(cards, rarity):
        # カードをレアリティで検索する
        return [card for card in cards if rarity.lower() == card.rarity.lower()]

def search_pack(cards, pack):
        # カードをパック名で検索する
        return [card for card in cards if card.pack.lower() == pack.lower()]

def search_card_number(cards, card_number):
        # カード番号でカードを検索する
        return [card for card in cards if card.card_number.lower() == card_number.lower()]