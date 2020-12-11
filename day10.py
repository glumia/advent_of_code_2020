from collections import Counter

input_str = "..."


adapters = [0] + sorted(int(line) for line in input_str.split("\n"))
adapters.append(max(adapters) + 3)  # Add phone adapter

# Part 1
jolt_differences = Counter(
    [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
)
print(
    f"1-jolt differences: {jolt_differences[1]}.\n"
    f"3-jolt differences: {jolt_differences[3]}.\n"
    f"Product: {jolt_differences[1]*jolt_differences[3]}."
)

# Part 2
# Each element of this array represents in how many ways we can arrive at adapter[i]
in_paths = [0] * len(adapters)
in_paths[0] = 1
for i in range(0, len(adapters) - 1):
    in_paths[i + 1] += in_paths[i]
    if i + 2 < len(adapters) and (adapters[i + 2] - adapters[i]) < 4:
        in_paths[i + 2] += in_paths[i]
    if i + 3 < len(adapters) and (adapters[i + 3] - adapters[i]) < 4:
        in_paths[i + 3] += in_paths[i]

print(f"Number of valid combinations of the adapters: {in_paths[-1]}")
