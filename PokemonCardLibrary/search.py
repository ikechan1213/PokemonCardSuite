def search_name(self, keyword):
        # カードをカード名(ポケモンの名前等)で検索する
        return [card for card in self.cards if keyword.lower() in card.name.lower()]
    
def search_type(self, card_type):
        # カードをタイプで検索する
        return [card for card in self.cards if card_type.lower() in card.type.lower()]
    
def search_rarity(self, rarity):
        # カードをレアリティで検索する
        return [card for card in self.cards if rarity.lower() in card.rarity.lower()]
    
def search_pack(self, pack):
        # カードをパック名で検索する
        return [card for card in self.cards if card.pack.lower() == pack.lower()]
    
def search_card_number(self, card_number):
        # カード番号でカードを検索する
        return [card for card in self.cards if card.card_number.lower() == card_number.lower()]