import random
import matplotlib.pyplot as plt


def theoretical_probabilities():
    counts = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    theory = {}
    s = 2
    for c in counts:
        theory[s] = c / 36
        s += 1
    return theory


def simulate_throws(num_throws):
    results = {s: 0 for s in range(2, 13)}
    for _ in range(num_throws):
        s = random.randint(1, 6) + random.randint(1, 6)
        results[s] += 1
    return results


def calculate_probabilities(counts, num_throws):
    probs = {}
    for s in range(2, 13):
        probs[s] = counts[s] / num_throws
    return probs


def print_comparison_table(counts, mc_probs, th_probs, num_throws):
    print(f"\nTrials: {num_throws}")
    print("Sum | Count     | Monte Carlo | Theoretical | Difference")
    print("---------------------------------------------------------")
    for s in range(2, 13):
        mc = mc_probs[s]
        th = th_probs[s]
        diff = abs(mc - th)
        print(f"{s:3} | {counts[s]:9} | "
              f"{mc:11.4f} | {th:11.4f} | {diff:10.4f}")


def plot_probabilities(all_mc_probs, th_probs, trial_counts):
    sums = list(range(2, 13))

    for probs, n in zip(all_mc_probs, trial_counts):
        values = [probs[s] for s in sums]
        plt.plot(sums, values, marker="o", label=f"Monte Carlo ({n})")

    theory_vals = [th_probs[s] for s in sums]
    plt.plot(sums, theory_vals,
             linestyle="--", marker="s", label="Theoretical")

    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.title("Two Dice Probabilities (Monte Carlo vs Theoretical)")
    plt.xticks(sums)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    trial_counts = [1000, 10000, 100000]
    th_probs = theoretical_probabilities()
    all_mc_probs = []

    print("Monte Carlo Simulation of Two Dice Rolls")

    for n in trial_counts:
        counts = simulate_throws(n)
        mc_probs = calculate_probabilities(counts, n)
        all_mc_probs.append(mc_probs)
        print_comparison_table(counts, mc_probs, th_probs, n)

    plot_probabilities(all_mc_probs, th_probs, trial_counts)


main()
