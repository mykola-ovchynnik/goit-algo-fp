import random

import matplotlib.pyplot as plt

N = 1_000_000

theoretical = {
    2: 2.78 / 100,
    3: 5.56 / 100,
    4: 8.33 / 100,
    5: 11.11 / 100,
    6: 13.89 / 100,
    7: 16.67 / 100,
    8: 13.89 / 100,
    9: 11.11 / 100,
    10: 8.33 / 100,
    11: 5.56 / 100,
    12: 2.78 / 100,
}


def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1 + d2


def calculate_probability(num_rolls):
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(num_rolls):
        total = roll_dice()
        counts[total] += 1
    return counts


def print_probability(counts, num_rolls):
    measured_probability = {s: counts[s] / num_rolls for s in range(2, 13)}
    print("Sum  | Measured probability | Theoretical probability | Difference")
    for s in range(2, 13):
        difference = measured_probability[s] - theoretical[s]
        print(
            f"{s:4}  | {measured_probability[s]:>10.4%}       | {theoretical[s]:>10.4%}       | {difference:>10.4%}"
        )
    return measured_probability


def plot_probability(frequencies):
    sums = list(frequencies.keys())
    probabilities = list(frequencies.values())
    theoretical_probabilities = [theoretical[s] for s in sums]

    plt.bar(sums, probabilities, color="blue", alpha=0.7, label="Monte Carlo")
    plt.plot(
        sums,
        theoretical_probabilities,
        color="red",
        marker="o",
        linestyle="dashed",
        label="Theoretical",
    )
    plt.xlabel("Sum of Dice")
    plt.ylabel("Probability")
    plt.title("Monte Carlo Simulation vs Theoretical Probabilities")
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    counts = calculate_probability(N)
    probability = print_probability(counts, N)
    plot_probability(probability)


if __name__ == "__main__":
    main()
