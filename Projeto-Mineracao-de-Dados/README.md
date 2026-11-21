# Perfis e padrões de acidentes em rodovias federais brasileiras

Trabalho de Mineração de Dados - Fatec Rio Claro (Tecnologia em Inteligência Artificial), 2026.
Autores: Vinicius Mendes e Artur Nagasima Furlan.

## Descrição do projeto
Aplicamos agrupamento (K-Means e K-Medoids) e regras de associação (Apriori) sobre os Dados Abertos da PRF (2023) para identificar perfis de acidentes e condições associadas a acidentes com vítima fatal. As regras descrevem associações, não relações de causa.

Em 2023, a PRF registrou 67.723 sinistros em rodovias federais, com 5.621 mortos e 78.413 feridos (Anuário PRF 2023).

## Base de dados
Dados Abertos da PRF, ano de 2023: https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf
Os CSVs não estão no repositório. Detalhes da fonte em fontes_dados.md.

## Conteúdo do repositório
- Apresentação: pasta apresentacao/
- Relatório final: pasta relatorio/
- Códigos: pasta notebooks/ (01_exploracao, 02_agrupamento, 03_regras_associacao)

## Como executar
1. Instale as dependências: pip install -r requirements.txt
2. Baixe e descompacte os CSVs da PRF na pasta data/
3. Abra a pasta no VS Code e rode os notebooks na ordem 01, 02, 03
