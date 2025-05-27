# Processo de Trabalho

## 1. Objetivo
Definir o processo para refatorar o código do PSO Binário sem afetar o repositório original, garantindo rastreabilidade e validação.

## 2. Processo Adotado
1. **Fork do Repositório Original**:
   - Criado um fork do repositório original para preservar o código inicial.
   - Repositório forkado: `github.com/equipe/refatoracao-pso-mochila`.

2. **Criação de Branch Específica**:
   - Criada a branch `feature/refactor` no fork para as alterações de refatoração.
   - Commits realizados com mensagens claras, descrevendo cada mudança (ex.: "Adiciona classe KnapsackProblem", "Implementa testes unitários").

3. **Fluxo de Trabalho**:
   - **Análise Inicial**: Executados `flake8` e `pylint` no código original para identificar problemas.
   - **Criação de Testes**: Desenvolvidos testes unitários com `pytest` antes da refatoração.
   - **Refatoração**: Aplicadas mudanças no branch `feature/refactor`, com validação contínua via testes.
   - **Validação Final**: Reexecutados testes e ferramentas de qualidade. Comparados resultados do algoritmo refatorado com o original.
   - **Documentação**: Criados arquivos `refatoracao.md` e `processo.md`. Slides gerados em HTML.

4. **Ferramentas de Controle**:
   - **Git**: Usado para controle de versão, com commits atômicos.
   - **GitHub**: Hospedagem do fork e branch. Pull request planejado para revisão.
   - **Pytest**: Validação do comportamento.
   - **Flake8/Pylint**: Garantia de qualidade do código.

## 3. Repositório Estrutura
- `src/knapsack_pso_refatorado.py`: Código refatorado.
- `tests/test_knapsack_pso.py`: Testes unitários.
- `docs/refatoracao.md`: Documentação da refatoração.
- `docs/processo.md`: Este arquivo.
- `slides/index.html`: Slides da apresentação.
- `fitness_evolution.png`: Gráfico gerado.

## 4. Cuidados para Preservar o Código Original
- O código original foi mantido intacto no repositório forkado, em uma branch `original`.
- Todas as alterações foram feitas na branch `feature/refactor`.
- Testes garantem que o comportamento do algoritmo não foi alterado.

## 5. Próximos Passos
- Submeter pull request para revisão.
- Apresentar resultados à equipe.
- Incorporar feedback e realizar ajustes, se necessário.