class Luhn(object):
    def __init__(self, card_num):
        self.raw_input = card_num
        self.nums = list(reversed([int(c) for c in card_num if c in '1234567890']))

    def is_valid(self):
        odd_nums = self.nums[::2]
        even_nums = self.nums[1::2]
        transformed_even = [(num *2) for num in even_nums]
        for i, num in enumerate(transformed_even):
            if num > 9:
                transformed_even[i] -= 9
        
        filtered_input = [c for c in self.raw_input if c in '1234567890 ']
        return len(self.nums) > 1 and sum(odd_nums + transformed_even) % 10 == 0 and len(filtered_input) == len(self.raw_input)
