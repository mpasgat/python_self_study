from collections import defaultdict

purchases = [
    {"user": "alice", "amount": 100, "category": "food"},
    {"user": "bob", "amount": 50, "category": "books"},
    {"user": "alice", "amount": 200, "category": "food"},
    {"user": "alice", "amount": 30, "category": "books"},
]

def total_by_user_purchases(purchases) -> dict[str, int]:
    total_by_user: dict[str, int] = defaultdict(int)
    for user in purchases:
        total_by_user[user['user']] += user['amount']
    return dict(total_by_user)


def total_by_category(purchases) -> dict[str, int]:
    total_by_food: dict[str, int] = defaultdict(int)
    for category in purchases:
        total_by_food[category['category']] += category['amount']
    return dict(total_by_food)

def top_spenders(purchases, n) -> dict[str, int]:
    total_purchases = total_by_user_purchases(purchases)
    return dict(sorted(total_purchases.items(), key=lambda pair: pair[1], reverse=True)[:n])


print(total_by_user_purchases(purchases))
print(total_by_category(purchases))
print(top_spenders(purchases, 2))