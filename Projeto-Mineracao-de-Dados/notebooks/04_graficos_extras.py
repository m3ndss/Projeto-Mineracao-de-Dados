# %% [markdown]
# # 04 - Gráficos extras para relatório e slides
# Rode DEPOIS dos notebooks 01, 02 e 03 (usa data/base_acidentes.pkl e figuras/regras_fatal.csv).
# Coloque este arquivo em notebooks/ e rode célula por célula no VS Code.
# Cada gráfico é pulado com aviso se a coluna não existir.

# %%
from pathlib import Path
import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sns

RAIZ = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DATA = RAIZ / "data"; FIG = RAIZ / "figuras"; FIG.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")
COR, COR_FATAL = "#2b6cb0", "#c53030"
base = pd.read_pickle(DATA / "base_acidentes.pkl")
base["fatal"] = base["mortos"] > 0
TAXA_GERAL = base["fatal"].mean() * 100
print(base.shape, "| taxa geral de acidentes com morte: %.1f%%" % TAXA_GERAL)

def salvar(nome):
    plt.tight_layout(); plt.savefig(FIG / nome, dpi=150); plt.show()

def tem(*cols):
    falta = [c for c in cols if c not in base.columns]
    if falta: print("[pulado] colunas ausentes:", falta)
    return not falta

# %% [markdown]
# ## 1. Taxa de acidentes com morte por categoria

# %%
def taxa_por(col, titulo, nome, n_min=200, top=10):
    if not tem(col): return
    t = base.groupby(col)["fatal"].agg(["mean", "size"])
    t = t[t["size"] >= n_min].sort_values("mean", ascending=False).head(top)
    t["mean"] *= 100
    plt.figure(figsize=(9, 4.5))
    ax = sns.barplot(x=t["mean"], y=t.index, color=COR_FATAL)
    ax.axvline(TAXA_GERAL, color="black", ls="--", lw=1, label=f"média geral {TAXA_GERAL:.1f}%")
    ax.legend(loc="lower right", fontsize=9)
    for i, (m, n) in enumerate(zip(t["mean"], t["size"])):
        ax.text(m, i, f" {m:.1f}%  (n={n:,})".replace(",", "."), va="center", fontsize=8)
    ax.set_xlim(0, t["mean"].max() * 1.35)
    plt.title(titulo); plt.xlabel("% de acidentes com pelo menos 1 morte"); plt.ylabel("")
    salvar(nome)

taxa_por("causa_acidente", "Causas mais letais", "x_taxa_fatal_causa.png")
taxa_por("tipo_acidente", "Tipos de acidente mais letais", "x_taxa_fatal_tipo.png")
taxa_por("condicao_metereologica", "Gravidade por condição meteorológica", "x_taxa_fatal_clima.png")
taxa_por("fase_dia", "Gravidade por fase do dia", "x_taxa_fatal_fase_dia.png")
taxa_por("tipo_pista", "Gravidade por tipo de pista", "x_taxa_fatal_pista.png")

# %% [markdown]
# ## 2. Quando acontece: dia da semana x hora

# %%
if tem("dia_semana", "horario"):
    h = pd.to_datetime(base["horario"].astype(str), format="%H:%M:%S", errors="coerce").dt.hour
    ordem = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    ds = base["dia_semana"].astype(str).str.lower().str.strip()
    ct = pd.crosstab(ds, h).reindex([d for d in ordem if d in set(ds)])
    plt.figure(figsize=(11, 3.8))
    sns.heatmap(ct, cmap="YlOrRd", cbar_kws={"label": "Nº de acidentes"})
    plt.title("Acidentes por dia da semana e hora"); plt.xlabel("Hora do dia"); plt.ylabel("")
    salvar("x_heatmap_dia_hora.png")

# %% [markdown]
# ## 3. Onde acontece: UFs com mais acidentes e com mais mortes

# %%
if tem("uf"):
    g = base.groupby("uf").agg(acidentes=("fatal", "size"), mortos=("mortos", "sum"))
    top = g.sort_values("acidentes", ascending=False).head(10)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    top["acidentes"].sort_values().plot.barh(ax=ax[0], color=COR); ax[0].set_title("Acidentes por UF (top 10)")
    g["mortos"].sort_values(ascending=False).head(10).sort_values().plot.barh(ax=ax[1], color=COR_FATAL); ax[1].set_title("Mortos por UF (top 10)")
    for a in ax: a.set_ylabel("")
    salvar("x_uf_acidentes_mortos.png")

# %% [markdown]
# ## 4. Evolução mensal

# %%
if tem("data_inversa"):
    d = pd.to_datetime(base["data_inversa"], errors="coerce")
    m = base.groupby(d.dt.month).agg(acidentes=("fatal", "size"), mortos=("mortos", "sum"))
    fig, ax = plt.subplots(figsize=(9, 3.8))
    ax.bar(m.index, m["acidentes"], color=COR, label="Acidentes"); ax.set_xlabel("Mês"); ax.set_ylabel("Acidentes")
    ax2 = ax.twinx(); ax2.plot(m.index, m["mortos"], color=COR_FATAL, marker="o", label="Mortos"); ax2.set_ylabel("Mortos"); ax2.grid(False)
    ax.set_xticks(range(1, 13)); plt.title("Acidentes e mortos por mês")
    salvar("x_evolucao_mensal.png")

# %% [markdown]
# ## 5. Agrupamento (precisa da coluna `grupo` do notebook 02)

# %%
if tem("grupo"):
    g = base.groupby("grupo").agg(n=("fatal", "size"), pct_fatal=("fatal", "mean"))
    g["pct_fatal"] *= 100
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    ax[0].bar(g.index.astype(str), g["n"], color=COR); ax[0].set_title("Nº de acidentes por grupo"); ax[0].set_xlabel("Grupo")
    ax[1].bar(g.index.astype(str), g["pct_fatal"], color=COR_FATAL); ax[1].set_title("% com morte por grupo"); ax[1].set_xlabel("Grupo")
    ax[1].axhline(TAXA_GERAL, color="black", ls="--", lw=1)
    salvar("x_grupos_tamanho_fatal.png")

    cols = [c for c in ["pessoas", "veiculos", "mortos", "feridos_leves", "feridos_graves"] if c in base.columns]
    media = base.groupby("grupo")[cols].mean()
    media.plot.bar(figsize=(9, 4), width=0.8, colormap="tab10"); plt.xticks(rotation=0)
    plt.title("Médias por grupo (valores reais, sem padronizar)"); plt.xlabel("Grupo"); plt.legend(loc="upper left", ncol=3, fontsize=8)
    salvar("x_grupos_medias.png")

# %% [markdown]
# ## 6. Regras de associação: top regras por lift (lê figuras/regras_fatal.csv do notebook 03)

# %%
import textwrap
csv = FIG / "regras_fatal.csv"
if csv.exists():
    r = pd.read_csv(csv)
    r = r[r["support"] >= 0.01].sort_values("lift", ascending=False).head(10).iloc[::-1]
    rot = [textwrap.fill(a.replace("_", " ").replace(" + ", "\n+ "), 48) for a in r["antecedente"]]
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.barh(rot, r["lift"], color=COR)
    ax.axvline(1, color="black", ls="--", lw=1)
    for i, (l, c) in enumerate(zip(r["lift"], r["confidence"])):
        ax.text(l, i, f" lift {l:.2f} | conf. {c*100:.0f}%", va="center", fontsize=8)
    ax.set_xlim(0, r["lift"].max() * 1.5)
    ax.tick_params(axis="y", labelsize=8)
    fig.suptitle("Top 10 regras → acidente com morte (por lift)", x=0.5); plt.xlabel("Lift (1 = igual ao acaso)")
    salvar("x_regras_top_lift.png")
else:
    print("[pulado] rode o notebook 03 antes (gera figuras/regras_fatal.csv)")
