from itertools import combinations

input_str = "..."

numbers = [int(line) for line in input_str.split("\n")]

# Part 1
for i in range(25, len(numbers)):
    if any(sum(comb) == numbers[i] for comb in combinations(numbers[i - 25 : i], 2)):
        continue
    print(
        f"Number {numbers[i]} at position {i} is not the sum of any pair of the "
        "previous 25 numbers."
    )
    break


# Part 2
b = 616  # Position of my invalid number
invalid_number = numbers[b]
while True:
    a = b
    s = 0
    while s < invalid_number:
        a -= 1
        s += numbers[a]
    if s == invalid_number:
        print(
            f"Found contiguous set, start at position {a} and end at {b-1}.\n"
            f"Encryption weakness: {sum((min(numbers[a:b]),max(numbers[a:b])))}."
        )
        break
    b -= 1
