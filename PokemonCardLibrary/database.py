from .storage import load_cards, save_cards
from .search import search_name, search_type, search_rarity, search_pack, search_card_number

class Database:
    def __init__(self):
        self.cards = load_cards()

    def add_card(self, card):
        # カードをデータベースにカードを追加する
        for c in self.cards:
            if c.card_number == card.card_number:
                raise ValueError("このカードは既に登録されています。")
        self.cards.append(card)
        save_cards(self.cards)

    def update_card(self, card):
        # カード登録情報を更新する
        for c in self.cards:
            if c.card_number == card.card_number:
                break
        else:
            raise ValueError("指定されたカードは見つかりません。")
        self.cards = [c if c.card_number != card.card_number else card for c in self.cards]
        save_cards(self.cards)

    def delete_card(self, card_number):
        # カード登録情報を削除する
        #　カード番号が存在するか確認した後に削除処理をしてる
        for c in self.cards:
            if c.card_number == card_number:
                break
        else:
                raise ValueError("指定されたカードが見つかりません。")
        
        self.cards = [card for card in self.cards if card.card_number != card_number]
        save_cards(self.cards)
        return

    def get_all_cards(self):
        # カードをデータベースから取得する
        return self.cards.copy()
    
    # search.pyのsearch_nameを呼び出す
    def search_name(self, keyword):
        return search_name(self.cards, keyword)
    
    # search.pyのsearch_typeを呼び出す
    def search_type(self, card_type):
        return search_type(self.cards, card_type)
    
    # search.pyのsearch_rarityを呼び出す
    def search_rarity(self, rarity):
        return search_rarity(self.cards, rarity)
    
    # search.pyのsearch_packを呼び出す
    def search_pack(self, pack):
        return search_pack(self.cards, pack)
    
    # search.pyのsearch_card_numberを呼び出す
    def search_card_number(self,    card_number):
        return search_card_number(self.cards, card_number)