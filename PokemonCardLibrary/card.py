class Card:
    def __init__(self, card_number, packid, name, hp, type, rarity, pack, count, evolution):
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