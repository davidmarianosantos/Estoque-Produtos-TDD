"""
Módulo de modelo de Produto.

Define a classe :class:`Produto`, que representa um item no estoque.
"""


class Produto:
    """Representa um produto no estoque.

    Attributes:
        id (int): Identificador único do produto.
        nome (str): Nome do produto.
        quantidade (int): Quantidade disponível em estoque.
        preco (float): Preço unitário do produto.

    Example:
        >>> p = Produto(1, "Caneta", 100, 1.50)
        >>> p.nome
        'Caneta'
    """

    def __init__(self, id: int, nome: str, quantidade: int, preco: float):
        """Inicializa um Produto.

        Args:
            id (int): Identificador único.
            nome (str): Nome do produto.
            quantidade (int): Quantidade em estoque.
            preco (float): Preço unitário.

        Raises:
            ValueError: Se quantidade ou preço forem negativos.
        """
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")

        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __repr__(self) -> str:
        return (
            f"Produto(id={self.id}, nome='{self.nome}', "
            f"quantidade={self.quantidade}, preco={self.preco:.2f})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Produto):
            return False
        return self.id == other.id
