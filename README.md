# 📦 Estoque de Produtos

Sistema simples de gerenciamento de estoque desenvolvido com **Python** seguindo a metodologia **TDD (Test-Driven Development)**.

> Atividade prática da disciplina **Engenharia de Software (DEC000095)**

> Autor: **David Júnio Mariano dos Santos**

---

## 📋 Sobre o Projeto

Este projeto implementa um CRUD de produtos em estoque (criar, listar, buscar, atualizar e remover) com foco em qualidade de código, cobertura de testes e documentação. Foi desenvolvido como atividade prática da disciplina de Engenharia de Software.

### Funcionalidades

- ✅ Adicionar produto (nome, quantidade, preço)
- ✅ Listar todos os produtos
- ✅ Buscar produto por ID
- ✅ Buscar produto por nome (parcial, case-insensitive)
- ✅ Atualizar nome, quantidade e/ou preço
- ✅ Remover produto
- ✅ Validação de dados com mensagens de erro claras

---

## 🛠️ Tecnologias

| Ferramenta | Uso |
|---|---|
| Python 3.10+ | Linguagem principal |
| pytest | Framework de testes unitários |
| pytest-cov | Relatório de cobertura de testes |
| Sphinx | Geração de documentação HTML |
| sphinx-rtd-theme | Tema da documentação |

---

## 📁 Estrutura do Projeto

```
Estoque-Produtos-TDD/
├── estoque/
│   ├── __init__.py        # Exportações do pacote
│   ├── produto.py         # Classe Produto (modelo)
│   └── estoque.py         # Classe Estoque (serviço CRUD)
├── tests/
│   ├── __init__.py
│   └── test_estoque.py    # Testes unitários (TDD)
├── docs/
│   ├── conf.py            # Configuração do Sphinx
│   ├── index.rst          # Índice da documentação
│   └── modules.rst        # Referência dos módulos
├── pytest.ini             # Configuração do pytest
├── requirements.txt       # Dependências
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/davidmarianosantos/Estoque-Produtos-TDD.git
cd Estoque-Produtos-TDD


# Crie e ative um ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Executar os Testes

```bash
# Todos os testes com relatório de cobertura
pytest

# Apenas os testes, sem cobertura
pytest --no-cov

# Testes de uma classe específica
pytest tests/test_estoque.py::TestEstoqueAdicionar -v
```

Saída esperada:

```
tests/test_estoque.py::TestProduto::test_criar_produto_valido PASSED
tests/test_estoque.py::TestProduto::test_quantidade_negativa_levanta_erro PASSED
...
============= 22 passed in 0.12s =============

---------- coverage ----------
estoque/produto.py    100%
estoque/estoque.py    100%
```

---

## 📖 Documentação do Código

A documentação é gerada automaticamente pelo **Sphinx** a partir das docstrings do código.

### Gerar e visualizar

```bash
cd docs

# Gerar HTML
sphinx-build -b html . _build/html

# Abrir no navegador
# Linux
xdg-open _build/html/index.html

# macOS
open _build/html/index.html

# Windows
start _build/html/index.html
```

A documentação ficará disponível em `docs/_build/html/index.html`.

---

## 🧪 Metodologia TDD

O desenvolvimento seguiu rigorosamente o ciclo **Red → Green → Refactor**:

1. **RED** — Escrever um teste que descreve o comportamento desejado. O teste falha porque o código ainda não existe.
2. **GREEN** — Implementar o mínimo de código necessário para o teste passar.
3. **REFACTOR** — Melhorar o código (clareza, performance, design) sem quebrar os testes.

Cada método testado possui um comentário `[RED→GREEN]` na sua docstring indicando essa origem.

---

## 💡 Exemplo de Uso

```python
from estoque import Estoque

# Criar estoque
e = Estoque()

# Adicionar produtos
notebook = e.adicionar("Notebook Dell", 10, 3500.00)
mouse    = e.adicionar("Mouse Logitech", 50, 89.90)

# Listar
for p in e.listar():
    print(p)

# Buscar
p = e.buscar_por_id(1)
print(p.nome)  # Notebook Dell

# Atualizar preço
e.atualizar(1, preco=3299.00)

# Remover
e.remover(2)
```

---

## 📄 Licença

Projeto acadêmico desenvolvido para a disciplina **Engenharia de Software (DEC000095)**.

Autor: **David Júnio Mariano dos Santos** — uso livre para fins educacionais.
