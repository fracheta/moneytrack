# 💰 MoneyTrack

> Sistema de educação financeira desenvolvido em Python com interface gráfica (Tkinter).

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 Sobre o projeto

O **MoneyTrack** é um sistema desktop criado como projeto acadêmico que integra três grandes áreas da computação:

- 🗄️ **Banco de Dados** — armazenamento das transações e categorias
- 📊 **Ciência de Dados** — geração de gráficos e indicadores financeiros
- 💻 **Programação e Desenvolvimento** — interface gráfica e lógica do sistema

O objetivo é **ajudar o usuário a controlar suas finanças pessoais**, registrando receitas e despesas, categorizando gastos e visualizando sua situação financeira por meio de dashboards e relatórios.

---

## ✨ Funcionalidades

- [x] Interface gráfica com navegação lateral (sidebar)
- [x] Dashboard com cards de indicadores (saldo, receitas, despesas)
- [x] Gráficos visuais (pizza e barras)
- [x] Tela de **Transações** com formulário completo (CRUD)
- [x] Tela de **Categorias** com cadastro e listagem
- [x] Tela de **Relatórios** com filtros e área para gráficos
- [ ] Integração com banco de dados (SQLite) — *em desenvolvimento*
- [ ] CRUD funcional — *em desenvolvimento*
- [ ] Gráficos reais com Matplotlib — *em desenvolvimento*

---

## 🧱 Tecnologias previstas

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.8+ |
| Interface | Tkinter / ttk |
| Banco de Dados | SQLite3 |
| Gráficos | Matplotlib |
| Dados | Pandas / NumPy |

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.8 ou superior instalado
- Tkinter (já vem com o Python na maioria das distribuições)

### Passos

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/moneytrack.git

# Entre na pasta
cd moneytrack

# (Opcional) crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instale as dependências (futuras)
pip install -r requirements.txt

# Execute
python moneytrack.py
