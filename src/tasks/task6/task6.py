class Item:
    def __init__(self, name, cost, calories):
        self.cost = cost
        self.calories = calories
        self.ratio = calories/cost
        self.name = name

    def __str__(self) -> str:
        return (f"{self.name}: {self.cost}$ {self.calories}kcal")


def greedy_algorythm(new_items: list[Item], max: int) -> dict:
    items = new_items
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    dish_composition = []
    for item in items:
        if max >= item.cost:
            max -= item.cost
            total_calories += item.calories
            dish_composition.append(item)
    dish_composition = [str(item) for item in dish_composition]
    return {'dish': dish_composition, 'total': total_calories}


def dynamic_programming(W, wt, val, n):
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                val1 = val[i - 1] + K[i - 1][w - wt[i - 1]]
                val2 = K[i - 1][w]
                K[i][w] = val1 if val1 > val2 else val2
            else:
                K[i][w] = K[i - 1][w]

    w = W
    selected_items = []
    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:  # Це означає, що предмет i був вибраний
            selected_items.append(i - 1)  # Додаємо індекс предмета
            w -= wt[i - 1]  # Віднімаємо вагу предмета

    # Оскільки ми проходили таблицю з кінця, треба перевернути список
    selected_items.reverse()

    # Повертаємо саму таблицю та список вибраних предметів
    return K[n][W], selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
names = [item for item in items.keys()]
cost = [item['cost'] for item in items.values()]
calories = [item['calories'] for item in items.values()]

n = len(cost)

items = [Item(names[i], cost[i], calories[i]) for i in range(n)]

max = 120

total, selected_items = dynamic_programming(max, cost, calories, n)

values = greedy_algorythm(items, max)

print(f"Maximum cost: {max}\n-------------------------------------\nGreedy algortythm\n-------------------------------------")
print(f'Dish: {[val for val in values['dish']]}\nTotal: {values['total']}')
print("-------------------------------------\nDynamic programming\n-------------------------------------")
print(f"Dish: {[str(Item(names[i], cost[i], calories[i]))
      for i in selected_items]}\nTotal: {total}")
