# Processo de Trabalho

## 1. Objetivo
Definir o processo para refatorar o código do PSO Binário sem afetar o repositório original, garantindo rastreabilidade e validação.

## 2. Processo Adotado
1. **Fork do Repositório Original**:
   - Criado um repositório de cópia para preservar código original.
   - Codigo copiado: `https://github.com/Math-GSilva/PSO-Binary/tree/main`.

2. **Criação de novo repositório**:
   - Criado novo repositorio para refatoração.

3. **Fluxo de Trabalho**:
   - **Criação de Testes**: Desenvolvidos testes unitários com `pytest` antes da refatoração.
   - **Refatoração**: Aplicadas mudanças no novo código com validação contínua via testes.
   - **Documentação**: Criados arquivos `refatoracao.md` e `processo.md`. Slides gerados em Python.

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
- `slides/slides_pso.py`: Script Python para apresentação interativa.
- `fitness_evolution.png`: Gráfico gerado.

## 4. Cuidados para Preservar o Código Original
- O código original foi mantido intacto no repositório forkado, em uma branch `original`.
- Todas as alterações foram feitas na branch no novo repositório.
- Testes garantem que o software funciona kkkk.

## 5. Próximos Passos
- Apresentar resultados à equipe usando `slides_pso.py`.
- Incorporar feedback e realizar ajustes, se necessário.