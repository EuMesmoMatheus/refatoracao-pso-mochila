import random
import math
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
import numpy as np

class KnapsackProblem:
    """Encapsula o problema da mochila 0/1."""
    
    CAPACITY_PERCENTAGE = 0.4
    MIN_ITEM_VALUE = 10
    MAX_ITEM_VALUE = 100
    MIN_ITEM_WEIGHT = 1
    MAX_ITEM_WEIGHT = 50

    def __init__(self, weights: List[int], values: List[int], capacity: int):
        if len(weights) != len(values):
            raise ValueError("Lists of weights and values must have the same length.")
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")
        self.weights = weights
        self.values = values
        self.capacity = capacity

    @classmethod
    def generate_instance(cls, n_items: int = 100, capacity_percentage: float = CAPACITY_PERCENTAGE) -> 'KnapsackProblem':
        """Gera uma instância do problema da mochila."""
        weights = [random.randint(cls.MIN_ITEM_WEIGHT, cls.MAX_ITEM_WEIGHT) for _ in range(n_items)]
        values = [random.randint(cls.MIN_ITEM_VALUE, cls.MAX_ITEM_VALUE) for _ in range(n_items)]
        capacity = int(sum(weights) * capacity_percentage)
        return cls(weights, values, capacity)

    def calculate_fitness(self, solution: List[int]) -> int:
        """Calcula o valor total da solução, penalizando se o peso exceder a capacidade."""
        if len(solution) != len(self.weights):
            raise ValueError("Solution length must match number of items.")
        total_weight = sum(self.weights[i] for i, selected in enumerate(solution) if selected == 1)
        if total_weight > self.capacity:
            return 0
        return sum(self.values[i] for i, selected in enumerate(solution) if selected == 1)

    def get_total_weight(self, solution: List[int]) -> int:
        """Calcula o peso total da solução."""
        return sum(self.weights[i] for i, selected in enumerate(solution) if selected == 1)

class BinaryPSO:
    """Implementa o algoritmo PSO Binário para o problema da mochila."""
    
    def __init__(self, problem: KnapsackProblem, n_particles: int = 30, n_iterations: int = 50,
                 inertia: float = 0.8, cognitive_coeff: float = 1.5, social_coeff: float = 1.5,
                 seed: Optional[int] = None, verbose: bool = False):
        self.problem = problem
        self.n_particles = n_particles
        self.n_iterations = n_iterations
        self.inertia = inertia
        self.cognitive_coeff = cognitive_coeff
        self.social_coeff = social_coeff
        self.verbose = verbose
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        self.n_items = len(self.problem.weights)
        self.particles = None
        self.velocities = None
        self.personal_best = None
        self.personal_best_values = None
        self.global_best = None
        self.global_best_value = 0
        self.fitness_history = []

    def _sigmoid(self, x: float) -> float:
        """Função sigmoide robusta para binarização."""
        try:
            x = max(min(x, 20), -20)  # Limita x entre -20 e 20
            if x == 20:
                return 1.0
            if x == -20:
                return 0.0
            return 1 / (1 + math.exp(-x))
        except OverflowError:
            return 0 if x < 0 else 1

    def _initialize(self):
        """Inicializa partículas e velocidades."""
        self.particles = [[random.randint(0, 1) for _ in range(self.n_items)] for _ in range(self.n_particles)]
        self.velocities = [[random.uniform(-1, 1) for _ in range(self.n_items)] for _ in range(self.n_particles)]
        self.personal_best = [particle[:] for particle in self.particles]
        self.personal_best_values = [self.problem.calculate_fitness(p) for p in self.particles]
        best_idx = np.argmax(self.personal_best_values)
        self.global_best = self.personal_best[best_idx][:]
        self.global_best_value = self.personal_best_values[best_idx]

    def _update_particles(self):
        """Atualiza velocidades e posições das partículas."""
        r1 = np.random.random((self.n_particles, self.n_items))
        r2 = np.random.random((self.n_particles, self.n_items))
        for i in range(self.n_particles):
            for j in range(self.n_items):
                self.velocities[i][j] = (
                    self.inertia * self.velocities[i][j] +
                    self.cognitive_coeff * r1[i][j] * (self.personal_best[i][j] - self.particles[i][j]) +
                    self.social_coeff * r2[i][j] * (self.global_best[j] - self.particles[i][j])
                )
                prob = self._sigmoid(self.velocities[i][j])
                self.particles[i][j] = 1 if random.random() < prob else 0
            fitness = self.problem.calculate_fitness(self.particles[i])
            if fitness > self.personal_best_values[i]:
                self.personal_best[i] = self.particles[i][:]
                self.personal_best_values[i] = fitness
        best_idx = np.argmax(self.personal_best_values)
        if self.personal_best_values[best_idx] > self.global_best_value:
            self.global_best = self.personal_best[best_idx][:]
            self.global_best_value = self.personal_best_values[best_idx]

    def run(self) -> Tuple[List[int], int, List[int]]:
        """Executa o algoritmo PSO Binário."""
        self._initialize()
        for iteration in range(self.n_iterations):
            self._update_particles()
            self.fitness_history.append(self.global_best_value)
            if self.verbose:
                print(f"Iteration {iteration + 1} | Best Fitness: {self.global_best_value}")
        return self.global_best, self.global_best_value, self.fitness_history

def run_experiments(n_executions: int = 5, seed: Optional[int] = None, verbose: bool = False) -> dict:
    """Executa múltiplos experimentos e retorna estatísticas."""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    problem = KnapsackProblem.generate_instance()
    results = []
    best_solutions = []
    best_fitness_history = None
    best_global_value = 0
    best_global_solution = None

    for i in range(n_executions):
        if verbose:
            print(f"\nExecution {i + 1}/{n_executions}")
        pso = BinaryPSO(problem, seed=seed + i if seed is not None else None, verbose=verbose)
        solution, fitness, history = pso.run()
        weight = problem.get_total_weight(solution)
        if verbose:
            print(f"→ Best Fitness: {fitness} | Weight: {weight}")
        results.append(fitness)
        best_solutions.append(solution)
        if fitness > best_global_value:
            best_global_value = fitness
            best_global_solution = solution
            best_fitness_history = history

    stats = {
        "mean_fitness": np.mean(results),
        "max_fitness": max(results),
        "min_fitness": min(results),
        "best_solution": best_global_solution,
        "best_fitness": best_global_value,
        "best_weight": problem.get_total_weight(best_global_solution),
        "fitness_history": best_fitness_history
    }
    
    if verbose:
        print("\nExperiment Statistics:")
        print(f"Mean Fitness: {stats['mean_fitness']:.2f}")
        print(f"Best Fitness: {stats['max_fitness']}")
        print(f"Worst Fitness: {stats['min_fitness']}")
        print(f"\nBest Global Solution:")
        print(f"Fitness: {stats['best_fitness']} | Weight: {stats['best_weight']}")
        print(f"Solution: {stats['best_solution']}")
        
        plt.plot(stats['fitness_history'])
        plt.title("Fitness Evolution (Best Execution)")
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.grid(True)
        plt.savefig("fitness_evolution.png")
        plt.close()
    
    return stats

if __name__ == "__main__":
    run_experiments(n_executions=5, seed=42, verbose=True)