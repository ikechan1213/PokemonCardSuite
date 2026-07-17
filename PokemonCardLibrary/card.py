class Card:
    def __init__(self, card_number, packid, name, evolution, hp, type, rarity, pack, count):
        self.card_number = card_number
        self.packid = packid
        self.name = name
        self.evolution = evolution
        self.hp = hp
        self.type = type
        self.rarity = rarity
        self.pack = pack
        self.count = count

# カードオブジェクトを辞書に変換して返す
    def to_dict(self):
        return {
            "card_number": self.card_number,
            "packid": self.packid,
            "name": self.name,
            "evolution": self.evolution,
            "hp": self.hp,
            "type": self.type,
            "rarity": self.rarity,
            "pack": self.pack,
            "count": self.count
        }

# 辞書をカードオブジェクトに変換して返す(逆変換)
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["card_number"],
            data["packid"],
            data["name"],
            data["hp"],
            data["type"],
            data["rarity"],
            data["pack"],
            data["count"],
            data["evolution"]
        )
    #　プリントデバッグ用にカード番号とカード名を表示する
    def __str__(self):
        return f"{self.card_number} {self.name}"
    
    def __repr__(self):
        return f"Card({self.card_number}, {self.name})"