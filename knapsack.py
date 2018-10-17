import collections
import itertools


MAX_WEIGHT = 400
COST_TOTAL = 0
WEIGHT_TOTAL = 0
RESULT = None

ITEM = [
    ('map', 9, 150),
    ('compass', 13, 35),
    ('water', 153, 200),
    ('sandwich', 50, 160),
    ('glucose', 15, 60),
    ('tin', 68, 45),
    ('banana', 27, 60),
    ('apple', 39, 40),
    ('cheese', 23, 30),
    ('beer', 52, 10),
    ('suntan cream', 11, 70),
    ('camera', 32, 30),
    ('T-shirt', 24, 15),
    ('trousers', 48, 10),
    ('umbrella', 73, 40),
    ('waterproof trousers', 42, 70),
    ('waterproof overclothes', 43, 75),
    ('note-case', 22, 80),
    ('sunglasses', 7, 20),
    ('towel', 18, 12),
    ('socks', 4, 50),
    ('book', 30, 10),
]


Item = collections.namedtuple('Item', [
    'name',
    'weight',
    'value'
    ])

ITEMS = [Item(name, weight, value) for name, weight, value in ITEM]


def find_optimal_list(item, COST_TOTAL):
    weight, value = 0, 0

    for i in item:
        weight += i.weight
        value += i.value

    if weight <= MAX_WEIGHT and value > COST_TOTAL:
        return value, weight


for lng in range(0, len(ITEMS) + 1):
    for item in itertools.combinations(ITEMS, lng):
        res = find_optimal_list(item, COST_TOTAL)

        if res:
            RESULT = item
            COST_TOTAL = res[0]
            WEIGHT_TOTAL = res[1]

for i in RESULT:
    print(i.name)

print(f"weight {WEIGHT_TOTAL} value {COST_TOTAL}")
