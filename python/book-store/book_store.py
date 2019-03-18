from collections import Counter

DISCOUNTS = {
    0:0,
    1:80,
    2:240,
    3:640,
    4:1000,
}

def calculate_total(books):
    book_counts = sorted(Counter(books).values())[::-1] + [0]
    differences = [v[0] - v[1] for v in zip(book_counts[:-1],book_counts[1:])]
    cost = len(books) * 800
    for i, d in enumerate(differences):
        cost -= DISCOUNTS[i]*d

    if len(differences) == 5:
        adjust_5_3 = min(differences[2],differences[4])

        cost -= adjust_5_3 * 40

    return cost


