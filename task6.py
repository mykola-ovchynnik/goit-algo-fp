products = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        for w in range(budget + 1):
            if info["cost"] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - info["cost"]] + info["calories"]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, info = item_list[i - 1]
            selected_items.append(item)
            total_cost += info["cost"]
            w -= info["cost"]

    selected_items.reverse()
    return selected_items, total_cost, total_calories


def print_output(algorithm_name, selected_items, total_cost, total_calories):
    print(f"\n{algorithm_name}:")
    print(f"Selected items: {selected_items}")
    print(f"Total cost: {total_cost}")
    print(f"Total calories: {total_calories}")


def main():
    budget = int(input("Enter your budget: "))

    selected_items, total_cost, total_calories = greedy_algorithm(products, budget)
    print_output("Greedy Algorithm", selected_items, total_cost, total_calories)

    selected_items, total_cost, total_calories = dynamic_programming(products, budget)
    print_output("Dynamic Programming", selected_items, total_cost, total_calories)


if __name__ == "__main__":
    main()
