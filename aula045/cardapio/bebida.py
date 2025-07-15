from cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, ml):
        super().__init__(nome, preco)
        self.ml = ml