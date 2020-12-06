inp = "..."

# Part 1
answers_anyone = [set(group.replace("\n", "")) for group in inp.split("\n\n")]
sum([len(answ) for answ in answers])


# Part 2
answers_everyone = [
    reduce(
        set.intersection, (set(person_answers) for person_answers in group.split("\n"))
    )
    for group in inp.split("\n\n")
]

sum([len(answ) for answ in answers_everyone])
