<div align="center">

# 💰 MoneyTrack

### Educação financeira simples, visual e inteligente.

**Registre receitas · Controle despesas · Entenda seus gastos**

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6B6B?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557C?style=for-the-badge)](https://matplotlib.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)]()

<br>

[📸 Screenshots](#-screenshots) · [🚀 Começar](#-como-executar) · [🗺️ Roadmap](#%EF%B8%8F-roadmap) · [🤝 Contribuir](#-contribuindo)

</div>

---

## 📖 Sobre o projeto

**MoneyTrack** é um sistema desktop de educação financeira desenvolvido como projeto acadêmico de integração entre **Banco de Dados**, **Ciência de Dados** e **Desenvolvimento de Sistemas**.

O sistema permite que o usuário registre suas receitas e despesas, categorize seus gastos e visualize a evolução de sua vida financeira por meio de um dashboard moderno com gráficos e indicadores em tempo real.

> 💡 **Objetivo:** transformar dados brutos de transações em *insights visuais* que ajudem o usuário a tomar melhores decisões financeiras.

---

## ✨ Funcionalidades

<table>
<tr>
<td width="50%">

### 🎨 Interface
- [x] Layout moderno com sidebar
- [x] Dashboard com cards de KPI
- [x] Gráficos donut e barras
- [x] Navegação entre páginas sem recarregar
- [x] Design responsivo ao redimensionar
- [x] Paleta de cores consistente

</td>
<td width="50%">

### ⚙️ Funcionalidades
- [x] Cadastro de transações
- [x] Gestão de categorias
- [x] Cálculo automático de saldo
- [x] Filtros por período
- [ ] Persistência em SQLite — *em breve*
- [ ] Gráficos com Matplotlib — *em breve*

</td>
</tr>
</table>

---

## 🖼️ Screenshots

<div align="center">

| Dashboard | Transações |
|:---------:|:----------:|
| *Em breve* | *Em breve* |

| Categorias | Relatórios |
|:----------:|:----------:|
| *Em breve* | *Em breve* |

</div>

> 📌 Adicione imagens em `assets/` e substitua as tabelas acima.

---

## 🧱 Stack de tecnologias

<div align="center">

| Camada | Tecnologia | Uso |
|:------:|:----------:|:----|
| **Linguagem** | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Base do sistema |
| **Interface** | ![Tkinter](https://img.shields.io/badge/-Tkinter-FF6B6B?style=flat-square) | GUI desktop |
| **Banco de Dados** | ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white&style=flat-square) | Armazenamento local |
| **Gráficos** | ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square) | Visualizações |
| **Análise** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square) | Manipulação de dados |

</div>

---

## 🚀 Como executar

### 📋 Pré-requisitos

- **Python 3.8+** instalado ([download](https://python.org/downloads))
- **Tkinter** (já incluso no Python padrão)

### ⚡ Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/moneytrack.git

# 2. Entre na pasta
cd moneytrack

# 3. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute o sistema
python moneytrack.py
```

> ✅ **Nenhuma configuração adicional necessária.** O sistema roda out-of-the-box apenas com a interface visual.

---

## 📂 Estrutura do projeto

```
moneytrack/
│
├── 📄 moneytrack.py        # Aplicação principal (UI + lógica)
├── 📄 README.md            # Este arquivo
├── 📄 requirements.txt     # Dependências do projeto
├── 📄 LICENSE              # Licença MIT
├── 📄 .gitignore           # Arquivos ignorados pelo Git
│
└── 📁 assets/              # Imagens e recursos
    └── screenshots/        # (futuro) prints das telas
```

---

## 🗺️ Roadmap

<table>
<tr><td>✅</td><td>Estrutura visual completa (sidebar, dashboard, formulários)</td></tr>
<tr><td>✅</td><td>Sistema de navegação entre páginas</td></tr>
<tr><td>✅</td><td>Gráficos placeholder (donut + barras)</td></tr>
<tr><td>🔄</td><td><b>Integração com SQLite</b> — <i>em desenvolvimento</i></td></tr>
<tr><td>🔄</td><td><b>CRUD funcional</b> — <i>em desenvolvimento</i></td></tr>
<tr><td>⏳</td><td>Gráficos reais com Matplotlib</td></tr>
<tr><td>⏳</td><td>Exportação de relatórios (PDF / CSV)</td></tr>
<tr><td>⏳</td><td>Sistema de metas financeiras</td></tr>
<tr><td>⏳</td><td>Autenticação de usuários</td></tr>
</table>

---

## 🤝 Contribuindo

Contribuições tornam a comunidade open-source um lugar incrível! 🌟

1. **Fork** o projeto
2. Crie sua branch: `git checkout -b feature/nova-funcionalidade`
3. **Commit** suas mudanças: `git commit -m 'feat: adiciona nova funcionalidade'`
4. **Push** para a branch: `git push origin feature/nova-funcionalidade`
5. Abra um **Pull Request** 🎉

### 📝 Padrão de commits

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Documentação |
| `style:` | Formatação |
| `refactor:` | Refatoração |
| `test:` | Testes |

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [`LICENSE`](LICENSE) para mais informações.

---

<div align="center">

**Desenvolvido com ☕ e 🐍 como projeto acadêmico.**

*Integrando Banco de Dados · Ciência de Dados · Programação*

<br>

⭐ **Se este projeto te ajudou, deixe uma estrela!** ⭐

</div>
