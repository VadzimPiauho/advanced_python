import itertools

from package.data import ITEMS


def find_optimal_list(item, cost_total):
    max_weight = 400
    weight, value = 0, 0

    for i in item:
        weight += i.weight
        value += i.value

    if weight <= max_weight and value > cost_total:
        return value, weight


def main():
    cost_total = 0
    weight_total = 0
    result = None

    for lng in range(0, len(ITEMS) + 1):
        for item in itertools.combinations(ITEMS, lng):
            res = find_optimal_list(item, cost_total)

            if res:
                result = item
                cost_total = res[0]
                weight_total = res[1]

    for i in result:
        print(i.name)

    return f"weight {weight_total} value {cost_total}"


if __name__ == "__main__":
    print(main())
