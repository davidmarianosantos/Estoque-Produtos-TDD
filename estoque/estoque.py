"""
Módulo de serviço de Estoque.

Contém a classe :class:`Estoque`, responsável por gerenciar
o ciclo de vida dos produtos (criar, listar, atualizar, remover).
"""

from typing import List, Optional
from .produto import Produto


class Estoque:
    """Gerencia o estoque de produtos em memória.

    Fornece operações CRUD completas sobre uma coleção de
    objetos :class:`Produto`.

    Attributes:
        _produtos (dict): Dicionário interno que mapeia id -> Produto.
        _proximo_id (int): Contador auto-incrementado para IDs.

    Example:
        >>> estoque = Estoque()
        >>> estoque.adicionar("Notebook", 10, 3500.00)
        Produto(id=1, nome='Notebook', quantidade=10, preco=3500.00)
    """

    def __init__(self):
        """Inicializa um Estoque vazio."""
        self._produtos: dict[int, Produto] = {}
        self._proximo_id: int = 1

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------

    def adicionar(self, nome: str, quantidade: int, preco: float) -> Produto:
        """Adiciona um novo produto ao estoque.

        Args:
            nome (str): Nome do produto.
            quantidade (int): Quantidade inicial.
            preco (float): Preço unitário.

        Returns:
            Produto: O produto recém-criado com ID atribuído.

        Raises:
            ValueError: Se nome for vazio, quantidade ou preço negativos.

        Example:
            >>> estoque = Estoque()
            >>> p = estoque.adicionar("Mouse", 50, 89.90)
            >>> p.id
            1
        """
        nome = nome.strip()
        if not nome:
            raise ValueError("Nome do produto não pode ser vazio.")

        produto = Produto(self._proximo_id, nome, quantidade, preco)
        self._produtos[self._proximo_id] = produto
        self._proximo_id += 1
        return produto

    # ------------------------------------------------------------------
    # READ
    # ------------------------------------------------------------------

    def listar(self) -> List[Produto]:
        """Retorna todos os produtos cadastrados.

        Returns:
            List[Produto]: Lista de produtos (pode ser vazia).

        Example:
            >>> estoque = Estoque()
            >>> estoque.listar()
            []
        """
        return list(self._produtos.values())

    def buscar_por_id(self, id: int) -> Optional[Produto]:
        """Busca um produto pelo seu ID.

        Args:
            id (int): Identificador do produto.

        Returns:
            Optional[Produto]: O produto encontrado ou ``None``.

        Example:
            >>> estoque = Estoque()
            >>> estoque.adicionar("Teclado", 20, 150.00)
            Produto(id=1, nome='Teclado', quantidade=20, preco=150.00)
            >>> estoque.buscar_por_id(1).nome
            'Teclado'
        """
        return self._produtos.get(id)

    def buscar_por_nome(self, nome: str) -> List[Produto]:
        """Busca produtos cujo nome contenha o termo informado (case-insensitive).

        Args:
            nome (str): Termo de busca.

        Returns:
            List[Produto]: Produtos cujo nome contém o termo.

        Example:
            >>> estoque = Estoque()
            >>> estoque.adicionar("Monitor Full HD", 5, 900.00)
            Produto(id=1, nome='Monitor Full HD', quantidade=5, preco=900.00)
            >>> estoque.buscar_por_nome("monitor")
            [Produto(id=1, nome='Monitor Full HD', quantidade=5, preco=900.00)]
        """
        termo = nome.strip().lower()
        return [p for p in self._produtos.values() if termo in p.nome.lower()]

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------

    def atualizar(
        self,
        id: int,
        nome: Optional[str] = None,
        quantidade: Optional[int] = None,
        preco: Optional[float] = None,
    ) -> Produto:
        """Atualiza os dados de um produto existente.

        Apenas os campos informados (não ``None``) são alterados.

        Args:
            id (int): ID do produto a atualizar.
            nome (Optional[str]): Novo nome, se informado.
            quantidade (Optional[int]): Nova quantidade, se informada.
            preco (Optional[float]): Novo preço, se informado.

        Returns:
            Produto: O produto atualizado.

        Raises:
            KeyError: Se o produto não for encontrado.
            ValueError: Se os novos valores forem inválidos.

        Example:
            >>> estoque = Estoque()
            >>> estoque.adicionar("Cadeira", 3, 450.00)
            Produto(id=1, nome='Cadeira', quantidade=3, preco=450.00)
            >>> estoque.atualizar(1, preco=499.90).preco
            499.9
        """
        produto = self._produtos.get(id)
        if produto is None:
            raise KeyError(f"Produto com id={id} não encontrado.")

        if nome is not None:
            nome = nome.strip()
            if not nome:
                raise ValueError("Nome não pode ser vazio.")
            produto.nome = nome

        if quantidade is not None:
            if quantidade < 0:
                raise ValueError("Quantidade não pode ser negativa.")
            produto.quantidade = quantidade

        if preco is not None:
            if preco < 0:
                raise ValueError("Preço não pode ser negativo.")
            produto.preco = preco

        return produto

    # ------------------------------------------------------------------
    # DELETE
    # ------------------------------------------------------------------

    def remover(self, id: int) -> Produto:
        """Remove um produto do estoque.

        Args:
            id (int): ID do produto a remover.

        Returns:
            Produto: O produto removido.

        Raises:
            KeyError: Se o produto não for encontrado.

        Example:
            >>> estoque = Estoque()
            >>> estoque.adicionar("Impressora", 2, 800.00)
            Produto(id=1, nome='Impressora', quantidade=2, preco=800.00)
            >>> estoque.remover(1).nome
            'Impressora'
            >>> estoque.listar()
            []
        """
        if id not in self._produtos:
            raise KeyError(f"Produto com id={id} não encontrado.")
        return self._produtos.pop(id)
