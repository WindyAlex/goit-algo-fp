def greedy_algorithm(items: dict, budget: int):
    sorted_items = sorted(
        items.items(),
        key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
        reverse=True
    )

    chosen = []
    total_cost = 0
    total_cal = 0

    for name, data in sorted_items:
        cost = data["cost"]
        cal = data["calories"]
        if total_cost + cost <= budget:
            chosen.append(name)
            total_cost += cost
            total_cal += cal

    return chosen, total_cost, total_cal


def dynamic_programming(items: dict, budget: int):
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    cals = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost_i = costs[i - 1]
        cal_i = cals[i - 1]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost_i <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost_i] + cal_i)

    chosen = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen.append(names[i - 1])
            b -= costs[i - 1]

    chosen.reverse()
    total_cost = sum(items[name]["cost"] for name in chosen)
    total_cal = sum(items[name]["calories"] for name in chosen)

    return chosen, total_cost, total_cal


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hotdog": {"cost": 30, "calories": 200},
        "juice": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    g_items, g_cost, g_cal = greedy_algorithm(items, budget)
    d_items, d_cost, d_cal = dynamic_programming(items, budget)

    print(f"Budget: {budget}\n")

    print("Greedy algorithm:")
    print("Chosen:", g_items)
    print("Total cost:", g_cost)
    print("Total calories:", g_cal)

    print("\nDynamic programming (optimal):")
    print("Chosen:", d_items)
    print("Total cost:", d_cost)
    print("Total calories:", d_cal)


if __name__ == "__main__":
    main()
