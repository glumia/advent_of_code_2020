input_str = """..."""


def get_id(position):
    row, col = position
    return row * 8 + col


def get_position(boarding_pass):
    a, b = (0, 128)
    for i in range(7):
        c = int((a + b) / 2)
        a, b = (a, c) if boarding_pass[i] == "F" else (c, b)
    row = a

    a, b = (0, 8)
    for i in range(7, 10):
        c = int((a + b) / 2)
        a, b = (a, c) if boarding_pass[i] == "L" else (c, b)
    col = a

    return row, col


boarding_passes = {
    boarding_pass: get_position(boarding_pass)
    for boarding_pass in input_str.split("\n")
}

# Part 1
print(
    "Max boarding ID: "
    + str(max([get_id(position) for position in boarding_passes.values()]))
)


# Part 2
ROWS = 128
COLS = 8
positions = {row * 8 + col for row in range(ROWS) for col in range(COLS)}

available_pos = [
    pos
    for pos in positions
    if pos not in {get_id(bpass) for bpass in boarding_passes.values()}
]

# We know the flight is full and that we have 1 person before us and one after, hence
# we need to find the only 'jump' between consecutive values greater than 1.
for i in range(1, len(available_pos)):
    if not available_pos[i] == available_pos[i - 1] + 1:
        print("Your seat ID is: " + str(available_pos[i]))
        break
