# ============================================================
#  💰 MoneyTrack — Sistema de Educação Financeira
#  Interface refinada: dashboard, transações, categorias, relatórios
#
#  Autor: Seu Nome
#  Repositório: https://github.com/seu-usuario/moneytrack
# ============================================================

import tkinter as tk
from tkinter import ttk
from datetime import datetime

# ============================================================
# 🎨 DESIGN TOKENS
# ============================================================
class Tema:
    CORES = {
        "sidebar":        "#0f172a",
        "sidebar_hover":  "#1e293b",
        "sidebar_ativo":  "#3b82f6",
        "sidebar_texto":  "#94a3b8",
        "bg":             "#f8fafc",
        "card":           "#ffffff",
        "borda":          "#e2e8f0",
        "texto":          "#0f172a",
        "texto_claro":    "#64748b",
        "texto_muted":    "#94a3b8",
        "azul":           "#3b82f6",
        "azul_light":     "#dbeafe",
        "verde":          "#10b981",
        "verde_light":    "#d1fae5",
        "vermelho":       "#ef4444",
        "vermelho_light": "#fee2e2",
        "amarelo":        "#f59e0b",
        "roxo":           "#8b5cf6",
        "rosa":           "#ec4899",
    }
    ESPACO = {"xs": 4, "sm": 8, "md": 16, "lg": 24, "xl": 32}
    FONTES = {
        "h1":   ("Segoe UI", 22, "bold"),
        "h2":   ("Segoe UI", 15, "bold"),
        "h3":   ("Segoe UI", 12, "bold"),
        "body": ("Segoe UI", 10),
        "small":("Segoe UI", 9),
        "tiny": ("Segoe UI", 8),
        "kpi":  ("Segoe UI", 24, "bold"),
    }


C = Tema.CORES
E = Tema.ESPACO
F = Tema.FONTES


# ============================================================
# 🚀 APLICAÇÃO PRINCIPAL
# ============================================================
class MoneyTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 MoneyTrack — Educação Financeira")
        self.root.geometry("1300x780")
        self.root.minsize(1150, 700)
        self.root.configure(bg=C["bg"])

        # ────────────────────────────────────────────────────
        # TODO — Conexão com Banco de Dados
        # import sqlite3
        # self.conn = sqlite3.connect("moneytrack.db")
        # self.cursor = self.conn.cursor()
        # self._criar_tabelas()
        # ────────────────────────────────────────────────────

        self._configurar_estilos()
        self._criar_sidebar()
        self._criar_area_principal()
        self.mostrar_pagina("dashboard")

    # ========================================================
    # ESTILOS GLOBAIS
    # ========================================================
    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background=C["bg"])
        style.configure("Card.TFrame", background=C["card"])
        style.configure("TLabel", background=C["bg"], foreground=C["texto"], font=F["body"])
        style.configure("Card.TLabel", background=C["card"], foreground=C["texto"], font=F["body"])
        style.configure("Muted.TLabel", background=C["card"], foreground=C["texto_claro"], font=F["small"])

        # Treeview
        style.configure("Treeview",
                        background="white", fieldbackground="white",
                        foreground=C["texto"], rowheight=36,
                        font=F["body"], borderwidth=0)
        style.configure("Treeview.Heading",
                        background=C["bg"], foreground=C["texto_claro"],
                        font=("Segoe UI", 9, "bold"), borderwidth=0, relief="flat")
        style.map("Treeview.Heading", background=[("active", C["bg"])])
        style.map("Treeview",
                  background=[("selected", C["azul_light"])],
                  foreground=[("selected", C["texto"])])

        # Combobox
        style.configure("TCombobox", padding=6, font=F["body"],
                        fieldbackground="white", background="white")

    # ========================================================
    # SIDEBAR
    # ========================================================
    def _criar_sidebar(self):
        self.sidebar = tk.Frame(self.root, bg=C["sidebar"], width=240)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo
        logo = tk.Frame(self.sidebar, bg=C["sidebar"])
        logo.pack(fill="x", pady=(E["xl"], E["lg"]))
        tk.Label(logo, text="💰", bg=C["sidebar"], fg="white",
                 font=("Segoe UI", 22)).pack(padx=20, side="left")
        info = tk.Frame(logo, bg=C["sidebar"])
        info.pack(side="left")
        tk.Label(info, text="MoneyTrack", bg=C["sidebar"], fg="white",
                 font=("Segoe UI", 14, "bold")).pack(anchor="w")
        tk.Label(info, text="Educação Financeira", bg=C["sidebar"],
                 fg=C["sidebar_texto"], font=F["tiny"]).pack(anchor="w")

        # Label seção
        tk.Label(self.sidebar, text="MENU PRINCIPAL", bg=C["sidebar"],
                 fg=C["texto_muted"], font=("Segoe UI", 8, "bold")
                 ).pack(anchor="w", padx=24, pady=(E["md"], E["sm"]))

        # Botões
        self.nav_buttons = {}
        itens = [
            ("dashboard",  "📊", "Dashboard"),
            ("transacoes", "💸", "Transações"),
            ("categorias", "🏷️", "Categorias"),
            ("relatorios", "📈", "Relatórios"),
        ]
        for chave, icone, texto in itens:
            btn = self._criar_nav_button(chave, icone, texto)
            self.nav_buttons[chave] = btn

        # Rodapé
        rodape = tk.Frame(self.sidebar, bg=C["sidebar"])
        rodape.pack(side="bottom", fill="x", pady=E["md"])
        tk.Frame(rodape, bg="#1e293b", height=1).pack(fill="x", padx=20, pady=(0, 12))
        tk.Label(rodape, text="v1.0 · Projeto Acadêmico", bg=C["sidebar"],
                 fg=C["texto_muted"], font=F["tiny"]).pack(padx=20, anchor="w")

    def _criar_nav_button(self, chave, icone, texto):
        wrapper = tk.Frame(self.sidebar, bg=C["sidebar"], height=44)
        wrapper.pack(fill="x", padx=12, pady=2)
        wrapper.pack_propagate(False)

        btn = tk.Button(wrapper, text=f"  {icone}   {texto}",
                        bg=C["sidebar"], fg=C["sidebar_texto"],
                        activebackground=C["sidebar_hover"],
                        activeforeground="white",
                        relief="flat", bd=0, anchor="w", padx=14,
                        font=("Segoe UI", 10), cursor="hand2",
                        command=lambda c=chave: self.mostrar_pagina(c))
        btn.pack(fill="both", expand=True)

        btn.bind("<Enter>", lambda e: self._hover_nav(btn, True))
        btn.bind("<Leave>", lambda e: self._hover_nav(btn, False))
        return btn

    def _hover_nav(self, btn, entrar):
        if btn.cget("bg") != C["sidebar_ativo"]:
            btn.configure(bg=C["sidebar_hover"] if entrar else C["sidebar"],
                          fg="white" if entrar else C["sidebar_texto"])

    # ========================================================
    # ÁREA PRINCIPAL
    # ========================================================
    def _criar_area_principal(self):
        self.area = tk.Frame(self.root, bg=C["bg"])
        self.area.pack(side="left", fill="both", expand=True)

        # Topbar
        topbar = tk.Frame(self.area, bg=C["card"], height=64,
                          highlightbackground=C["borda"], highlightthickness=1)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)

        tk.Label(topbar, text="Sistema de Gestão Financeira",
                 bg=C["card"], fg=C["texto"], font=F["h3"]
                 ).pack(side="left", padx=E["lg"])
        tk.Label(topbar, text="🔔", bg=C["card"], fg=C["texto_claro"],
                 font=("Segoe UI", 14)).pack(side="right", padx=(0, 10))
        tk.Label(topbar, text=datetime.now().strftime("%d de %B de %Y"),
                 bg=C["card"], fg=C["texto_claro"], font=F["small"]
                 ).pack(side="right", padx=10)

        # Área de conteúdo dinâmico
        self.conteudo = tk.Frame(self.area, bg=C["bg"])
        self.conteudo.pack(fill="both", expand=True)

    # ========================================================
    # NAVEGAÇÃO
    # ========================================================
    def mostrar_pagina(self, nome):
        for w in self.conteudo.winfo_children():
            w.destroy()

        for k, b in self.nav_buttons.items():
            if k == nome:
                b.configure(bg=C["sidebar_ativo"], fg="white")
            else:
                b.configure(bg=C["sidebar"], fg=C["sidebar_texto"])

        {
            "dashboard":  self._pagina_dashboard,
            "transacoes": self._pagina_transacoes,
            "categorias": self._pagina_categorias,
            "relatorios": self._pagina_relatorios,
        }[nome]()

    # ========================================================
    # 🧩 COMPONENTES REUTILIZÁVEIS
    # ========================================================
    def _header_pagina(self, parent, titulo, subtitulo):
        head = tk.Frame(parent, bg=C["bg"])
        head.pack(fill="x", padx=E["xl"], pady=(E["lg"], E["md"]))
        tk.Label(head, text=titulo, bg=C["bg"], fg=C["texto"], font=F["h1"]
                 ).pack(anchor="w")
        tk.Label(head, text=subtitulo, bg=C["bg"], fg=C["texto_claro"], font=F["body"]
                 ).pack(anchor="w", pady=(2, 0))

    def _card(self, parent, **kwargs):
        """Card branco com borda sutil."""
        return tk.Frame(parent, bg=C["card"],
                        highlightbackground=C["borda"],
                        highlightthickness=1, **kwargs)

    def _card_kpi(self, parent, icone, titulo, valor, variacao=None, cor=None):
        card = self._card(parent)
        inner = tk.Frame(card, bg=C["card"])
        inner.pack(fill="both", expand=True, padx=E["md"], pady=E["md"])

        # Topo: ícone + título
        top = tk.Frame(inner, bg=C["card"])
        top.pack(fill="x")

        icon_box = tk.Frame(top, bg=C["azul_light"], width=40, height=40)
        icon_box.pack(side="left")
        icon_box.pack_propagate(False)
        tk.Label(icon_box, text=icone, bg=C["azul_light"],
                 font=("Segoe UI", 16)).pack(expand=True)

        info = tk.Frame(top, bg=C["card"])
        info.pack(side="left", padx=(E["sm"], 0))
        tk.Label(info, text=titulo, bg=C["card"], fg=C["texto_claro"],
                 font=F["small"]).pack(anchor="w")

        # Valor principal
        valor_lbl = tk.Label(inner, text=valor, bg=C["card"],
                             fg=cor or C["texto"], font=F["kpi"])
        valor_lbl.pack(anchor="w", pady=(E["sm"], 0))

        # Variação
        if variacao:
            v_frame = tk.Frame(inner, bg=C["card"])
            v_frame.pack(anchor="w", pady=(2, 0))
            cor_var = C["verde"] if variacao.startswith("+") else C["vermelho"]
            tk.Label(v_frame, text=variacao, bg=C["card"], fg=cor_var,
                     font=("Segoe UI", 9, "bold")).pack(side="left")
            tk.Label(v_frame, text=" vs. mês anterior", bg=C["card"],
                     fg=C["texto_muted"], font=F["tiny"]).pack(side="left")

        return card

    def _card_grafico(self, parent, titulo, subtitulo=None):
        card = self._card(parent)
        header = tk.Frame(card, bg=C["card"])
        header.pack(fill="x", padx=E["md"], pady=(E["md"], E["sm"]))
        tk.Label(header, text=titulo, bg=C["card"], fg=C["texto"],
                 font=F["h3"]).pack(anchor="w")
        if subtitulo:
            tk.Label(header, text=subtitulo, bg=C["card"], fg=C["texto_claro"],
                     font=F["tiny"]).pack(anchor="w", pady=(2, 0))
        return card

    def _btn(self, parent, texto, cor, comando=None, variant="solid"):
        if variant == "solid":
            bg, fg, hover = cor, "white", cor
        elif variant == "outline":
            bg, fg, hover = C["card"], cor, C["bg"]
        else:  # ghost
            bg, fg, hover = C["card"], C["texto_claro"], C["bg"]

        btn = tk.Button(parent, text=texto, bg=bg, fg=fg,
                        activebackground=hover, activeforeground=fg,
                        relief="flat", bd=0, padx=18, pady=9,
                        font=("Segoe UI", 10, "bold"), cursor="hand2",
                        command=comando)
        return btn

    def _input(self, parent, width=20, placeholder=""):
        wrapper = tk.Frame(parent, bg="white",
                           highlightbackground=C["borda"], highlightthickness=1)
        wrapper.pack_propagate(False)
        wrapper.configure(height=38, width=width * 8)

        entry = tk.Entry(wrapper, font=F["body"], bg="white", fg=C["texto"],
                         relief="flat", insertbackground=C["texto"],
                         bd=0)
        entry.pack(fill="both", expand=True, padx=10, pady=8)
        return wrapper, entry

    def _combo(self, parent, valores, width=15):
        cb = ttk.Combobox(parent, values=valores, state="readonly",
                          width=width, font=F["body"])
        return cb

    def _label_campo(self, parent, texto):
        return tk.Label(parent, text=texto, bg=C["card"], fg=C["texto_claro"],
                        font=("Segoe UI", 9, "bold"))

    # ========================================================
    # 📊 PÁGINA: DASHBOARD
    # ========================================================
    def _pagina_dashboard(self):
        frame = tk.Frame(self.conteudo, bg=C["bg"])
        frame.pack(fill="both", expand=True)
        self._header_pagina(frame, "Dashboard", "Acompanhe sua saúde financeira em tempo real")

        # ── CARDS DE KPI ─────────────────────────────────
        kpis = tk.Frame(frame, bg=C["bg"])
        kpis.pack(fill="x", padx=E["xl"])
        cards_def = [
            ("💰", "Saldo Total",   "R$ 3.450,00", "+12,5%", C["azul"]),
            ("📈", "Receitas",      "R$ 5.000,00", "+8,2%",  C["verde"]),
            ("📉", "Despesas",      "R$ 1.550,00", "-3,1%",  C["vermelho"]),
        ]
        for i, (ic, tit, val, var, cor) in enumerate(cards_def):
            card = self._card_kpi(kpis, ic, tit, val, var, cor)
            card.grid(row=0, column=i, sticky="nsew",
                      padx=(0 if i == 0 else E["sm"], 0 if i == 2 else E["sm"]))
            kpis.columnconfigure(i, weight=1)

        # ── GRÁFICOS ─────────────────────────────────────
        graficos = tk.Frame(frame, bg=C["bg"])
        graficos.pack(fill="x", padx=E["xl"], pady=E["md"])
        graficos.columnconfigure(0, weight=1)
        graficos.columnconfigure(1, weight=1)

        card_pizza = self._card_grafico(graficos, "Gastos por categoria",
                                        "Distribuição do mês atual")
        card_pizza.configure(height=300)
        card_pizza.grid(row=0, column=0, sticky="nsew", padx=(0, E["sm"]))
        card_pizza.pack_propagate(False)
        self._grafico_donut(card_pizza)

        card_barras = self._card_grafico(graficos, "Evolução mensal",
                                         "Receitas vs. Despesas (últimos 6 meses)")
        card_barras.configure(height=300)
        card_barras.grid(row=0, column=1, sticky="nsew", padx=(E["sm"], 0))
        card_barras.pack_propagate(False)
        self._grafico_barras(card_barras)

        # ── ÚLTIMAS TRANSAÇÕES ───────────────────────────
        recentes = self._card(frame)
        recentes.pack(fill="both", expand=True, padx=E["xl"], pady=(0, E["lg"]))

        header_rec = tk.Frame(recentes, bg=C["card"])
        header_rec.pack(fill="x", padx=E["md"], pady=(E["md"], E["sm"]))
        tk.Label(header_rec, text="Últimas transações", bg=C["card"],
                 fg=C["texto"], font=F["h3"]).pack(side="left")
        tk.Label(header_rec, text="Ver todas →", bg=C["card"],
                 fg=C["azul"], font=F["small"], cursor="hand2"
                 ).pack(side="right")

        cols = ("Data", "Descrição", "Categoria", "Tipo", "Valor")
        tree = ttk.Treeview(recentes, columns=cols, show="headings", height=5)
        larguras = {"Data": 100, "Descrição": 300, "Categoria": 160,
                    "Tipo": 100, "Valor": 130}
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=larguras[c],
                        anchor="e" if c == "Valor" else "w")
        tree.pack(fill="both", expand=True, padx=E["md"], pady=(0, E["md"]))

        # TODO — SELECT * FROM transacoes ORDER BY data DESC LIMIT 5
        dados = [
            ("01/11/2024", "Salário mensal",    "Salário",     "🟢 Receita", "+ R$ 5.000,00"),
            ("03/11/2024", "Supermercado",      "Alimentação", "🔴 Despesa", "− R$ 450,00"),
            ("05/11/2024", "Combustível",       "Transporte",  "🔴 Despesa", "− R$ 200,00"),
            ("08/11/2024", "Cinema com amigos", "Lazer",       "🔴 Despesa", "− R$ 60,00"),
            ("10/11/2024", "Freelance design",  "Extra",       "🟢 Receita", "+ R$ 800,00"),
        ]
        for d in dados:
            tree.insert("", "end", values=d)

    # ── Gráfico Donut (moderno) ─────────────────────────
    def _grafico_donut(self, parent):
        # TODO — substituir por matplotlib com dados do BD
        wrapper = tk.Frame(parent, bg=C["card"])
        wrapper.pack(fill="both", expand=True, padx=E["md"], pady=(0, E["md"]))

        # Canvas do donut
        canvas = tk.Canvas(wrapper, bg=C["card"], highlightthickness=0,
                           width=200, height=200)
        canvas.pack(side="left", padx=(E["md"], E["md"]))

        dados = [
            ("Moradia",     35, C["azul"]),
            ("Alimentação", 25, C["verde"]),
            ("Transporte",  15, C["amarelo"]),
            ("Lazer",       15, C["vermelho"]),
            ("Outros",      10, C["roxo"]),
        ]

        start = 90
        for _, pct, cor in dados:
            extent = -pct * 3.6
            canvas.create_arc(15, 15, 185, 185, start=start, extent=extent,
                              fill=cor, outline=C["card"], width=3)
            start += extent

        # Furo central (donut)
        canvas.create_oval(60, 60, 140, 140, fill=C["card"], outline=C["card"])

        # Texto central
        canvas.create_text(100, 90, text="Total", fill=C["texto_claro"],
                           font=("Segoe UI", 9))
        canvas.create_text(100, 110, text="R$ 1.550", fill=C["texto"],
                           font=("Segoe UI", 13, "bold"))

        # Legenda
        legenda = tk.Frame(wrapper, bg=C["card"])
        legenda.pack(side="left", fill="y", pady=E["md"])
        for nome, pct, cor in dados:
            linha = tk.Frame(legenda, bg=C["card"])
            linha.pack(anchor="w", pady=5)
            dot = tk.Frame(linha, bg=cor, width=10, height=10)
            dot.pack(side="left", padx=(0, 10))
            dot.pack_propagate(False)
            tk.Label(linha, text=nome, bg=C["card"], fg=C["texto"],
                     font=F["small"], width=12, anchor="w").pack(side="left")
            tk.Label(linha, text=f"{pct}%", bg=C["card"], fg=C["texto_claro"],
                     font=("Segoe UI", 9, "bold")).pack(side="left")

    # ── Gráfico de Barras ───────────────────────────────
    def _grafico_barras(self, parent):
        # TODO — substituir por matplotlib com dados do BD
        wrapper = tk.Frame(parent, bg=C["card"])
        wrapper.pack(fill="both", expand=True, padx=E["md"], pady=(0, E["md"]))

        # Área do gráfico com baseline
        area = tk.Frame(wrapper, bg=C["card"])
        area.pack(fill="both", expand=True)

        dados = [
            ("Jun", 0.45, 0.30),
            ("Jul", 0.60, 0.42),
            ("Ago", 0.50, 0.38),
            ("Set", 0.75, 0.55),
            ("Out", 0.65, 0.48),
            ("Nov", 0.85, 0.35),
        ]
        altura_max = 170

        # Barras agrupadas
        for mes, rec, desp in dados:
            col = tk.Frame(area, bg=C["card"])
            col.pack(side="left", expand=True, fill="both", padx=4)
            col_area = tk.Frame(col, bg=C["card"], height=altura_max)
            col_area.pack(fill="x")
            col_area.pack_propagate(False)

            # Container das duas barras
            barras = tk.Frame(col_area, bg=C["card"])
            barras.pack(fill="both", expand=True, padx=6)

            h_rec = int(altura_max * rec)
            h_desp = int(altura_max * desp)

            b1 = tk.Frame(barras, bg=C["verde"])
            b1.place(relx=0.25, rely=1.0, anchor="s", relwidth=0.35, height=h_rec)

            b2 = tk.Frame(barras, bg=C["vermelho"])
            b2.place(relx=0.75, rely=1.0, anchor="s", relwidth=0.35, height=h_desp)

            tk.Label(col, text=mes, bg=C["card"], fg=C["texto_claro"],
                     font=F["tiny"]).pack(pady=(6, 0))

        # Legenda
        leg = tk.Frame(wrapper, bg=C["card"])
        leg.pack(fill="x", pady=(E["sm"], 0))
        for cor, label in [(C["verde"], "Receitas"), (C["vermelho"], "Despesas")]:
            item = tk.Frame(leg, bg=C["card"])
            item.pack(side="left", padx=(0, E["md"]))
            dot = tk.Frame(item, bg=cor, width=10, height=10)
            dot.pack(side="left", padx=(0, 6))
            dot.pack_propagate(False)
            tk.Label(item, text=label, bg=C["card"], fg=C["texto_claro"],
                     font=F["tiny"]).pack(side="left")

    # ========================================================
    # 💸 PÁGINA: TRANSAÇÕES
    # ========================================================
    def _pagina_transacoes(self):
        frame = tk.Frame(self.conteudo, bg=C["bg"])
        frame.pack(fill="both", expand=True)
        self._header_pagina(frame, "Transações", "Registre e gerencie suas receitas e despesas")

        # ── FORMULÁRIO ───────────────────────────────────
        form_card = self._card(frame)
        form_card.pack(fill="x", padx=E["xl"], pady=(0, E["md"]))

        form_head = tk.Frame(form_card, bg=C["card"])
        form_head.pack(fill="x", padx=E["md"], pady=(E["md"], E["sm"]))
        tk.Label(form_head, text="➕ Nova transação", bg=C["card"],
                 fg=C["texto"], font=F["h3"]).pack(anchor="w")

        form_inner = tk.Frame(form_card, bg=C["card"])
        form_inner.pack(fill="x", padx=E["md"], pady=(0, E["md"]))

        linha = tk.Frame(form_inner, bg=C["card"])
        linha.pack(fill="x")

        campos = [
            ("Data",        12, "entry"),
            ("Descrição",   32, "entry"),
            ("Categoria",   18, "combo"),
            ("Tipo",        14, "combo"),
            ("Valor (R$)",  14, "entry"),
        ]
        entradas = {}
        for i, (label, largura, tipo) in enumerate(campos):
            col = tk.Frame(linha, bg=C["card"])
            col.pack(side="left", padx=(0 if i == 0 else E["sm"], 0))

            self._label_campo(col, label).pack(anchor="w", pady=(0, 4))

            if tipo == "combo":
                valores = (["Salário", "Alimentação", "Transporte",
                            "Lazer", "Moradia", "Saúde", "Outros"]
                           if label == "Categoria"
                           else ["Receita", "Despesa"])
                w = self._combo(col, valores, width=largura)
                w.pack(ipady=3)
                entradas[label] = w
            else:
                wrapper, entry = self._input(col, width=largura)
                wrapper.pack()
                if label == "Data":
                    entry.insert(0, datetime.now().strftime("%d/%m/%Y"))
                entradas[label] = entry

        # Botões
        acoes = tk.Frame(form_inner, bg=C["card"])
        acoes.pack(fill="x", pady=(E["md"], 0))
        self._btn(acoes, "➕  Adicionar", C["verde"],
                  self._salvar_transacao).pack(side="left", padx=(0, E["sm"]))
        self._btn(acoes, "Limpar", C["texto_claro"], variant="outline",
                  ).pack(side="left")

        # ── TABELA ───────────────────────────────────────
        tabela_card = self._card(frame)
        tabela_card.pack(fill="both", expand=True, padx=E["xl"], pady=(0, E["lg"]))

        topo = tk.Frame(tabela_card, bg=C["card"])
        topo.pack(fill="x", padx=E["md"], pady=(E["md"], E["sm"]))
        tk.Label(topo, text="Histórico de transações", bg=C["card"],
                 fg=C["texto"], font=F["h3"]).pack(side="left")

        self._btn(topo, "🗑️  Excluir", C["vermelho"], variant="outline",
                  ).pack(side="right", padx=(E["sm"], 0))
        self._btn(topo, "✏️  Editar", C["azul"], variant="outline",
                  ).pack(side="right")

        cols = ("ID", "Data", "Descrição", "Categoria", "Tipo", "Valor")
        tree = ttk.Treeview(tabela_card, columns=cols, show="headings", height=10)
        larguras = {"ID": 60, "Data": 110, "Descrição": 280,
                    "Categoria": 160, "Tipo": 110, "Valor": 130}
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=larguras[c],
                        anchor="e" if c == "Valor" else "w")

        scroll = ttk.Scrollbar(tabela_card, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.pack(side="left", fill="both", expand=True,
                  padx=(E["md"], 0), pady=(0, E["md"]))
        scroll.pack(side="right", fill="y", padx=(0, E["md"]), pady=(0, E["md"]))

        # TODO — SELECT * FROM transacoes
        for d in [
            (1, "01/11/2024", "Salário mensal",    "Salário",     "🟢 Receita", "R$ 5.000,00"),
            (2, "03/11/2024", "Supermercado",      "Alimentação", "🔴 Despesa", "R$ 450,00"),
            (3, "05/11/2024", "Combustível",       "Transporte",  "🔴 Despesa", "R$ 200,00"),
            (4, "08/11/2024", "Cinema com amigos", "Lazer",       "🔴 Despesa", "R$ 60,00"),
            (5, "10/11/2024", "Freelance design",  "Extra",       "🟢 Receita", "R$ 800,00"),
        ]:
            tree.insert("", "end", values=d)

    # ========================================================
    # 🏷️ PÁGINA: CATEGORIAS
    # ========================================================
    def _pagina_categorias(self):
        frame = tk.Frame(self.conteudo, bg=C["bg"])
        frame.pack(fill="both", expand=True)
        self._header_pagina(frame, "Categorias", "Organize suas transações por tipo de gasto")

        # ── FORMULÁRIO ───────────────────────────────────
        form_card = self._card(frame)
        form_card.pack(fill="x", padx=E["xl"], pady=(0, E["md"]))
        inner = tk.Frame(form_card, bg=C["card"])
        inner.pack(fill="x", padx=E["md"], pady=E["md"])

        tk.Label(inner, text="➕ Nova categoria", bg=C["card"],
                 fg=C["texto"], font=F["h3"]).pack(anchor="w", pady=(0, E["md"]))

        linha = tk.Frame(inner, bg=C["card"])
        linha.pack(fill="x")

        # Nome
        col1 = tk.Frame(linha, bg=C["card"])
        col1.pack(side="left", padx=(0, E["sm"]))
        self._label_campo(col1, "Nome da categoria").pack(anchor="w", pady=(0, 4))
        wrapper, e_nome = self._input(col1, width=30)
        wrapper.pack()

        # Tipo
        col2 = tk.Frame(linha, bg=C["card"])
        col2.pack(side="left", padx=(0, E["sm"]))
        self._label_campo(col2, "Tipo").pack(anchor="w", pady=(0, 4))
        self._combo(col2, ["Receita", "Despesa"], width=15).pack(ipady=3)

        # Cor
        col3 = tk.Frame(linha, bg=C["card"])
        col3.pack(side="left")
        self._label_campo(col3, "Cor").pack(anchor="w", pady=(0, 4))
        self._combo(col3, ["🔵 Azul", "🟢 Verde", "🔴 Vermelho",
                           "🟡 Amarelo", "🟣 Roxo", "🩷 Rosa"],
                    width=14).pack(ipady=3)

        self._btn(inner, "➕  Adicionar categoria", C["verde"],
                  self._salvar_categoria).pack(anchor="w", pady=(E["md"], 0))

        # ── TABELA ───────────────────────────────────────
        tabela_card = self._card(frame)
        tabela_card.pack(fill="both", expand=True, padx=E["xl"], pady=(0, E["lg"]))
        tk.Label(tabela_card, text="Categorias cadastradas", bg=C["card"],
                 fg=C["texto"], font=F["h3"]
                 ).pack(anchor="w", padx=E["md"], pady=(E["md"], E["sm"]))

        cols = ("ID", "Nome", "Tipo", "Cor")
        tree = ttk.Treeview(tabela_card, columns=cols, show="headings", height=8)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=200 if c == "Nome" else 140)
        tree.pack(fill="both", expand=True, padx=E["md"], pady=(0, E["md"]))

        # TODO — SELECT * FROM categorias
        for cat in [
            (1, "Salário",     "Receita", "🔵 Azul"),
            (2, "Alimentação", "Despesa", "🟢 Verde"),
            (3, "Transporte",  "Despesa", "🟡 Amarelo"),
            (4, "Lazer",       "Despesa", "🔴 Vermelho"),
            (5, "Moradia",     "Despesa", "🟣 Roxo"),
        ]:
            tree.insert("", "end", values=cat)

    # ========================================================
    # 📈 PÁGINA: RELATÓRIOS
    # ========================================================
    def _pagina_relatorios(self):
        frame = tk.Frame(self.conteudo, bg=C["bg"])
        frame.pack(fill="both", expand=True)
        self._header_pagina(frame, "Relatórios", "Análises e insights sobre suas finanças")

        # ── FILTROS ──────────────────────────────────────
        filtros = self._card(frame)
        filtros.pack(fill="x", padx=E["xl"], pady=(0, E["md"]))
        inner = tk.Frame(filtros, bg=C["card"])
        inner.pack(fill="x", padx=E["md"], pady=E["md"])

        tk.Label(inner, text="Período:", bg=C["card"], fg=C["texto_claro"],
                 font=F["small"]).pack(side="left", padx=(0, E["sm"]))
        self._combo(inner, ["Últimos 7 dias", "Último mês",
                            "Últimos 3 meses", "Este ano"],
                    width=18).pack(side="left", ipady=3)
        self._btn(inner, "🔄  Atualizar", C["azul"]).pack(side="left", padx=E["sm"])
        self._btn(inner, "📥  Exportar", C["verde"], variant="outline",
                  ).pack(side="right")

        # ── GRÁFICOS ─────────────────────────────────────
        grid = tk.Frame(frame, bg=C["bg"])
        grid.pack(fill="both", expand=True, padx=E["xl"], pady=(0, E["lg"]))
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        grid.rowconfigure(0, weight=1)
        grid.rowconfigure(1, weight=1)

        card1 = self._card_grafico(grid, "Receitas x Despesas", "Comparativo mensal")
        card1.grid(row=0, column=0, sticky="nsew", padx=(0, E["sm"]), pady=(0, E["sm"]))
        card1.pack_propagate(False)
        self._grafico_barras(card1)

        card2 = self._card_grafico(grid, "Distribuição por categoria", "Onde seu dinheiro foi")
        card2.grid(row=0, column=1, sticky="nsew", padx=(E["sm"], 0), pady=(0, E["sm"]))
        card2.pack_propagate(False)
        self._grafico_donut(card2)

        card3 = self._card_grafico(grid, "Evolução do saldo", "Linha do tempo financeira")
        card3.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(E["sm"], 0))
        card3.pack_propagate(False)

        tk.Label(card3, text="📈  Gráfico de linha gerado com Matplotlib",
                 bg=C["card"], fg=C["texto_muted"],
                 font=("Segoe UI", 10, "italic")).pack(expand=True)

    # ========================================================
    # 🔌 AÇÕES (CRUD) — placeholders
    # ========================================================
    def _salvar_transacao(self):
        # TODO — INSERT INTO transacoes (data, descricao, categoria_id, tipo, valor)
        # self.cursor.execute(...); self.conn.commit()
        # self._atualizar_tabelas()
        print("[TODO] Salvar transação no banco")

    def _salvar_categoria(self):
        # TODO — INSERT INTO categorias (nome, tipo, cor)
        print("[TODO] Salvar categoria no banco")


# ============================================================
# 🏁 PONTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyTrackApp(root)
    root.mainloop()
