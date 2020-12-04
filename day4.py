from typing import Optional
from enum import Enum
import re

import colander as c
from pydantic import BaseModel, validator, ValidationError


input_str = """..."""

passports = []
for raw_passport in input_str.split("\n\n"):
    raw_passport = raw_passport.replace("\n", " ")
    passport = dict(entry.split(":") for entry in raw_passport.split(" "))
    passports.append(passport)


## Solution with colander
height_regex = re.compile(r"(\d+)(cm|in)")
height_limits = {"cm": (150, 193), "in": (59, 76)}


def height_validator(node, value):
    match = re.match(height_regex, value)
    if not match:
        raise c.Invalid(node)
    num, unit = match.groups()
    min, max = height_limits[unit]
    if not min <= int(num) <= max:
        raise c.Invalid(value)


class Passport(c.MappingSchema):
    byr = c.SchemaNode(c.Int(), validator=c.Range(min=1920, max=2002))
    iyr = c.SchemaNode(c.Int(), validator=c.Range(min=2010, max=2020))
    eyr = c.SchemaNode(c.Int(), validator=c.Range(min=2020, max=2030))
    hgt = c.SchemaNode(c.String(), validator=height_validator)
    hcl = c.SchemaNode(c.String(), validator=c.Regex(r"^#[0-9a-f]{6}$"))
    ecl = c.SchemaNode(
        c.String(), validator=c.OneOf(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    )
    pid = c.SchemaNode(c.String(), validator=c.Regex(r"^\d{9}$"))


schema = Passport()


def is_valid(passport):
    try:
        schema.deserialize(passport)
    except c.Invalid:
        return False
    return True


count = sum([1 for passport in passports if is_valid(passport)])


## Alternative solution with pydantic
class EyeColors(str, Enum):
    amb = "amb"
    blu = "blu"
    brn = "brn"
    gry = "gry"
    grn = "grn"
    hzl = "hzl"
    oth = "oth"


class Passport(BaseModel):
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: EyeColors
    pid: str
    cid: Optional[str] = None

    @validator("byr")
    def check_byr_range(cls, value):
        if not 1920 <= value <= 2002:
            raise ValueError("not valid birth year")
        return value

    @validator("iyr")
    def check_iyr_range(cls, value):
        if not 2010 <= value <= 2020:
            raise ValueError("not valid issue year")
        return value

    @validator("eyr")
    def check_eyr_range(cls, value):
        if not 2020 <= value <= 2030:
            raise ValueError("not valid expiration year")
        return value

    @validator("hgt")
    def check_height(cls, value):
        match = re.match(height_regex, value)
        if not match:
            raise ValueError("not valid height string")
        num, unit = match.groups()
        min, max = height_limits[unit]
        if not min <= int(num) <= max:
            raise ValueError("not valid height")
        return value

    @validator("hcl")
    def check_hair_color(cls, value):
        regex = r"^#[0-9a-f]{6}$"
        match = re.match(regex, value)
        if not match:
            raise ValueError("not valid hair color")
        return value

    @validator("pid")
    def check_passport_id(cls, value):
        regex = r"^\d{9}$"
        match = re.match(regex, value)
        if not match:
            raise ValueError("not valid passport ID")
        return value


def is_valid_pyd(passport):
    try:
        Passport(**passport)
    except ValidationError:
        return False
    return True


count_pyd = sum([1 for passport in passports if is_valid_pyd(passport)])
