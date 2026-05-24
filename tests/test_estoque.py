"""
Testes unitários para o sistema de Estoque de Produtos.

Desenvolvidos seguindo a metodologia TDD (Test-Driven Development):
cada teste foi escrito *antes* da implementação correspondente,
guiando o design do código de produção.

Ciclo aplicado:
    1. RED   — escrever o teste que falha.
    2. GREEN — implementar o mínimo para o teste passar.
    3. REFACTOR — melhorar o código mantendo os testes verdes.
"""

import pytest
from estoque import Estoque, Produto


# ===========================================================================
# Fixtures
# ===========================================================================


@pytest.fixture
def estoque():
    """Retorna um Estoque vazio para uso nos testes."""
    return Estoque()


@pytest.fixture
def estoque_populado(estoque):
    """Retorna um Estoque com três produtos pré-cadastrados."""
    estoque.adicionar("Notebook Dell", 10, 3500.00)
    estoque.adicionar("Mouse Logitech", 50, 89.90)
    estoque.adicionar("Teclado Mecânico", 20, 250.00)
    return estoque


# ===========================================================================
# Produto — testes de criação e validação
# ===========================================================================


class TestProduto:
    """Testes da classe Produto."""

    def test_criar_produto_valido(self):
        """[RED→GREEN] Produto criado com atributos corretos."""
        p = Produto(1, "Caneta", 100, 1.50)
        assert p.id == 1
        assert p.nome == "Caneta"
        assert p.quantidade == 100
        assert p.preco == 1.50

    def test_quantidade_negativa_levanta_erro(self):
        """[RED→GREEN] Quantidade negativa deve levantar ValueError."""
        with pytest.raises(ValueError, match="Quantidade"):
            Produto(1, "Caneta", -1, 1.50)

    def test_preco_negativo_levanta_erro(self):
        """[RED→GREEN] Preço negativo deve levantar ValueError."""
        with pytest.raises(ValueError, match="Preço"):
            Produto(1, "Caneta", 10, -1.00)

    def test_produtos_com_mesmo_id_sao_iguais(self):
        """[RED→GREEN] Dois produtos com mesmo ID são considerados iguais."""
        p1 = Produto(1, "Caneta", 10, 1.50)
        p2 = Produto(1, "Lapiseira", 5, 3.00)
        assert p1 == p2

    def test_produtos_com_ids_diferentes_nao_sao_iguais(self):
        """[RED→GREEN] Produtos com IDs distintos não são iguais."""
        p1 = Produto(1, "Caneta", 10, 1.50)
        p2 = Produto(2, "Caneta", 10, 1.50)
        assert p1 != p2

    def test_repr_produto(self):
        """[RED→GREEN] Repr deve conter nome e id."""
        p = Produto(1, "Caneta", 10, 1.50)
        assert "Caneta" in repr(p)
        assert "1" in repr(p)


# ===========================================================================
# Estoque — CREATE
# ===========================================================================


class TestEstoqueAdicionar:
    """Testes da operação de adição (CREATE)."""

    def test_adicionar_produto_retorna_produto(self, estoque):
        """[RED→GREEN] adicionar() deve retornar o Produto criado."""
        p = estoque.adicionar("Notebook", 5, 3000.00)
        assert isinstance(p, Produto)
        assert p.nome == "Notebook"

    def test_adicionar_produto_atribui_id_automatico(self, estoque):
        """[RED→GREEN] IDs devem ser auto-incrementados a partir de 1."""
        p1 = estoque.adicionar("Produto A", 1, 10.00)
        p2 = estoque.adicionar("Produto B", 1, 10.00)
        assert p1.id == 1
        assert p2.id == 2

    def test_adicionar_nome_vazio_levanta_erro(self, estoque):
        """[RED→GREEN] Nome vazio deve levantar ValueError."""
        with pytest.raises(ValueError, match="Nome"):
            estoque.adicionar("   ", 10, 5.00)

    def test_adicionar_quantidade_negativa_levanta_erro(self, estoque):
        """[RED→GREEN] Quantidade negativa deve levantar ValueError."""
        with pytest.raises(ValueError):
            estoque.adicionar("Produto", -1, 5.00)

    def test_adicionar_preco_negativo_levanta_erro(self, estoque):
        """[RED→GREEN] Preço negativo deve levantar ValueError."""
        with pytest.raises(ValueError):
            estoque.adicionar("Produto", 10, -5.00)


# ===========================================================================
# Estoque — READ
# ===========================================================================


class TestEstoqueListar:
    """Testes das operações de leitura (READ)."""

    def test_listar_estoque_vazio(self, estoque):
        """[RED→GREEN] Estoque vazio deve retornar lista vazia."""
        assert estoque.listar() == []

    def test_listar_retorna_todos_os_produtos(self, estoque_populado):
        """[RED→GREEN] listar() deve retornar os 3 produtos cadastrados."""
        assert len(estoque_populado.listar()) == 3

    def test_buscar_por_id_existente(self, estoque_populado):
        """[RED→GREEN] Busca por ID existente deve retornar o produto."""
        p = estoque_populado.buscar_por_id(1)
        assert p is not None
        assert p.nome == "Notebook Dell"

    def test_buscar_por_id_inexistente_retorna_none(self, estoque):
        """[RED→GREEN] Busca por ID inexistente deve retornar None."""
        assert estoque.buscar_por_id(999) is None

    def test_buscar_por_nome_case_insensitive(self, estoque_populado):
        """[RED→GREEN] Busca por nome deve ser case-insensitive."""
        resultado = estoque_populado.buscar_por_nome("notebook")
        assert len(resultado) == 1
        assert resultado[0].nome == "Notebook Dell"

    def test_buscar_por_nome_retorna_multiplos(self, estoque):
        """[RED→GREEN] Busca pode retornar vários produtos."""
        estoque.adicionar("Mouse sem fio", 10, 80.00)
        estoque.adicionar("Mouse com fio", 15, 50.00)
        resultado = estoque.buscar_por_nome("mouse")
        assert len(resultado) == 2

    def test_buscar_por_nome_sem_resultado(self, estoque_populado):
        """[RED→GREEN] Busca sem resultado deve retornar lista vazia."""
        assert estoque_populado.buscar_por_nome("xyzabc") == []


# ===========================================================================
# Estoque — UPDATE
# ===========================================================================


class TestEstoqueAtualizar:
    """Testes da operação de atualização (UPDATE)."""

    def test_atualizar_nome(self, estoque_populado):
        """[RED→GREEN] Deve atualizar apenas o nome."""
        p = estoque_populado.atualizar(1, nome="Notebook Lenovo")
        assert p.nome == "Notebook Lenovo"

    def test_atualizar_quantidade(self, estoque_populado):
        """[RED→GREEN] Deve atualizar apenas a quantidade."""
        p = estoque_populado.atualizar(2, quantidade=100)
        assert p.quantidade == 100

    def test_atualizar_preco(self, estoque_populado):
        """[RED→GREEN] Deve atualizar apenas o preço."""
        p = estoque_populado.atualizar(3, preco=299.90)
        assert p.preco == 299.90

    def test_atualizar_multiplos_campos(self, estoque_populado):
        """[RED→GREEN] Deve atualizar nome e preço simultaneamente."""
        p = estoque_populado.atualizar(1, nome="Notebook HP", preco=2999.00)
        assert p.nome == "Notebook HP"
        assert p.preco == 2999.00

    def test_atualizar_id_inexistente_levanta_keyerror(self, estoque):
        """[RED→GREEN] Atualizar produto inexistente deve levantar KeyError."""
        with pytest.raises(KeyError):
            estoque.atualizar(999, nome="X")

    def test_atualizar_nome_vazio_levanta_erro(self, estoque_populado):
        """[RED→GREEN] Nome vazio na atualização deve levantar ValueError."""
        with pytest.raises(ValueError, match="Nome"):
            estoque_populado.atualizar(1, nome="  ")

    def test_atualizar_quantidade_negativa_levanta_erro(self, estoque_populado):
        """[RED→GREEN] Quantidade negativa na atualização deve levantar ValueError."""
        with pytest.raises(ValueError):
            estoque_populado.atualizar(1, quantidade=-5)


# ===========================================================================
# Estoque — DELETE
# ===========================================================================


class TestEstoqueRemover:
    """Testes da operação de remoção (DELETE)."""

    def test_remover_produto_existente(self, estoque_populado):
        """[RED→GREEN] remover() deve retornar o produto removido."""
        p = estoque_populado.remover(1)
        assert p.nome == "Notebook Dell"

    def test_remover_diminui_lista(self, estoque_populado):
        """[RED→GREEN] Após remoção, listar() deve ter um item a menos."""
        estoque_populado.remover(1)
        assert len(estoque_populado.listar()) == 2

    def test_remover_produto_inexistente_levanta_keyerror(self, estoque):
        """[RED→GREEN] Remover produto inexistente deve levantar KeyError."""
        with pytest.raises(KeyError):
            estoque.remover(999)

    def test_produto_removido_nao_aparece_na_busca(self, estoque_populado):
        """[RED→GREEN] Produto removido não deve ser encontrado por ID."""
        estoque_populado.remover(2)
        assert estoque_populado.buscar_por_id(2) is None
