# Perfis e padrões de acidentes em rodovias federais brasileiras

Trabalho de Mineração de Dados - Fatec Rio Claro (Inteligência Artificial).
Autores: **PREENCHER nomes da dupla**.

## Descrição
Aplicamos **agrupamento (K-Means e K-Medoids)** e **regras de associação (Apriori)** sobre dados abertos da PRF (ano 2023) para identificar perfis de acidentes e condições associadas a acidentes com vítimas fatais. As regras descrevem **associações**, não relações de causa.

## Base de dados
Dados Abertos da PRF (ver `fontes_dados.md`): acidentes por ocorrência (1 linha por acidente) e por pessoa. Os CSVs **não** estão no repositório (pasta `data/` no `.gitignore`).

## Técnicas
- Pré-processamento: limpeza, log1p, StandardScaler
- Agrupamento: K-Means e K-Medoids, k de 2 a 10, silhueta e cotovelo, PCA para visualização
- Regras de associação: Apriori (mlxtend), suporte/confiança/lift, consequente fixo = acidente com vítima fatal

## Estrutura
- `notebooks/` 01_exploracao, 02_agrupamento, 03_regras_associacao
- `relatorio/` relatório final
- `apresentacao/` slides
- `figuras/` gráficos gerados

## Como executar
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
# baixe e descompacte os CSVs da PRF em data/
# abra a pasta no VS Code, selecione o kernel .venv e rode os notebooks na ordem 01, 02, 03
```
