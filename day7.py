import re

input_str = "..."

regex = re.compile(r"(\d+) ([\w ]+) (?:bags|bag)[\.,]+[ ]?")

rules = {}
for line in input_str.split("\n"):
    bag, contains = line.split(" bags contain ")
    rules[bag] = {
        inner_bag: int(count) for count, inner_bag in re.findall(regex, contains)
    }


def contains_bag(bag, desired_bag):
    return desired_bag in rules[bag] or any(
        contains_bag(inner_bag, desired_bag) for inner_bag in rules[bag]
    )


sum(1 for bag in rules if contains_bag(bag, "shiny gold"))


def num_contents(bag):
    return sum(
        count * (1 + (num_contents(inner_bag)) if rules[inner_bag] else 1)
        for inner_bag, count in rules[bag].items()
    )


num_contents("shiny gold")
