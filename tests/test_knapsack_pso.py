import pytest
from src.knapsack_pso_refatorado import KnapsackProblem, BinaryPSO

def test_knapsack_problem_initialization():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    problem = KnapsackProblem(weights, values, capacity)
    assert problem.weights == weights
    assert problem.values == values
    assert problem.capacity == capacity

def test_knapsack_problem_invalid_input():
    with pytest.raises(ValueError, match="Lists of weights and values must have the same length."):
        KnapsackProblem([10, 20], [60], 50)
    with pytest.raises(ValueError, match="Capacity cannot be negative."):
        KnapsackProblem([10], [60], -1)

def test_calculate_fitness_valid_solution():
    problem = KnapsackProblem([10, 20, 30], [60, 100, 120], 50)
    solution = [1, 1, 0]
    assert problem.calculate_fitness(solution) == 160
    solution = [1, 0, 1]
    assert problem.calculate_fitness(solution) == 180

def test_calculate_fitness_over_capacity():
    problem = KnapsackProblem([10, 20, 30], [60, 100, 120], 40)
    solution = [1, 1, 1]
    assert problem.calculate_fitness(solution) == 0

def test_get_total_weight():
    problem = KnapsackProblem([10, 20, 30], [60, 100, 120], 50)
    solution = [1, 1, 0]
    assert problem.get_total_weight(solution) == 30

def test_sigmoid():
    pso = BinaryPSO(KnapsackProblem([10], [60], 50))
    assert 0 <= pso._sigmoid(0) <= 1
    assert pso._sigmoid(20) == 1
    assert pso._sigmoid(-20) == 0

def test_binary_pso_initialization():
    problem = KnapsackProblem([10, 20], [60, 100], 30)
    pso = BinaryPSO(problem, n_particles=2, n_iterations=2, seed=42)
    pso._initialize()
    assert len(pso.particles) == 2
    assert len(pso.velocities) == 2
    assert len(pso.personal_best) == 2
    assert len(pso.personal_best_values) == 2
    assert len(pso.global_best) == 2

def test_binary_pso_run():
    problem = KnapsackProblem([10, 20], [60, 100], 30)
    pso = BinaryPSO(problem, n_particles=2, n_iterations=2, seed=42)
    solution, fitness, history = pso.run()
    assert len(solution) == 2
    assert isinstance(fitness, int)
    assert len(history) == 2
    assert all(0 <= x <= sum(problem.values) for x in history)

def test_generate_instance():
    problem = KnapsackProblem.generate_instance(n_items=5, capacity_percentage=0.4)
    assert len(problem.weights) == 5
    assert len(problem.values) == 5
    assert problem.capacity > 0