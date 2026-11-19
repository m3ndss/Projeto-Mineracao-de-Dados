# Título: Perfis e padrões de acidentes em rodovias federais brasileiras
Autores: ______ e ______ | Fatec Rio Claro | 2026

## 1. Introdução
Problema (mortes e feridos em rodovias federais), objetivo (identificar perfis de acidentes e condições associadas a acidentes fatais), proposta (agrupamento + regras de associação em dados da PRF).

## 2. Justificativa
Relevância social e econômica. **[números: buscar em fonte oficial, citar - NÃO CONFIRMADO]**

## 3. Revisão da Literatura
Estudos a ABRIR E CONFERIR antes de citar (não verificados):
- Costa, Bernardini e Filho (2015), AtoZ.
- Oliveira e Borges, comparação de modelos de classificação de categorias de acidentes (SBC).
- Revista Transporte y Territorio, nº 31 (2024), regras de associação em acidentes.
- Mais 2 estudos acadêmicos e 1 notícia/relatório: **a encontrar**.

## 4. Metodologia e Resultados
### 4.1 Base de dados
Origem, site, ano, nº de registros, atributos, tabelas usadas, data do download. **[preencher com a saída do notebook 01]**
### 4.2 Agrupamento
Objetivo; dados; pré-processamento (log1p e StandardScaler, com justificativa); comparação K-Means x K-Medoids (amostra de 10.000, motivo); escolha de k (silhueta + cotovelo + interpretação); perfil dos grupos; PCA.
### 4.3 Regras de associação
Objetivo; variáveis categóricas usadas; agrupamento de categorias raras; Apriori (suporte mínimo escolhido e motivo); principais regras com suporte, confiança e lift; discussão.

## 5. Conclusão
Achados; análise crítica (limitações: um ano, só acidentes registrados pela PRF, associação não é causa, escolha de suporte, amostra no K-Medoids); relação com estudos/notícias.

## Referências (ordem alfabética)
