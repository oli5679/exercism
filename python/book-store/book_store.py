from collections import Counter
def calculate_total(books):
    book_counts = Counter(books)
    gross_cost = len(books)*800
    ranked_counts = list(sorted(book_counts.values()))
    ranked_counts.append(0)
    print(ranked_counts)
    discount_vals = [0, 80, 240,  640, 1000]
    discount_sum = sum([(ranked_counts[i] - ranked_counts[i+1]) * \
                            discount_vals[i] for i in range(len(ranked_counts)-1)])

    return gross_cost - discount_sum