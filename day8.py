from copy import deepcopy

input_str = "..."

instructions = [
    [function, int(value)]
    for line in input_str.split("\n")
    for function, value in [line.split(" ")]
]


def execute_boot(instructions):
    accumulator = 0
    executed = set()
    i = 0
    while i < len(instructions):
        executed.add(i)
        function, value = instructions[i]
        if function == "acc":
            accumulator += value
            i += 1
        elif function == "jmp":
            i += value
        else:  # nop
            i += 1
        if i in executed:
            raise RuntimeError(f"infinite loop detected [accumulator: {accumulator}].")
    return accumulator


# Part 1
execute_boot(instructions)

# Part 2 - Bruteforce (too lazy to find a better solution and this just works ahah)
for i in range(len(instructions)):
    function, value = instructions[i]
    if function == "acc":
        continue
    new_instructions = deepcopy(instructions)
    new_instructions[i][0] = "jmp" if function == "nop" else "nop"
    try:
        acc = execute_boot(new_instructions)
        print(
            f"Boot code fixed, replaced `{function}` at line {i}.\n"
            f"Accumulator value after successfull boot: {acc}."
        )
        break
    except RuntimeError:
        continue
