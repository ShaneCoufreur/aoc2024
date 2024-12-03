# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import TextSolution, answer
import re
from operator import mul


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(157621318)
    def part_1(self) -> int:
        matches = re.findall("mul\\([0-9]{1,9},[0-9]{1,9}\\)", self.input)
        s = 0
        for m in matches:
            s += eval(m)
        return s

    @answer(79845780)
    def part_2(self) -> int:
        matches = re.findall("mul\\([0-9]{1,9},[0-9]{1,9}\\)|don\\'t|do", self.input)
        print(matches)
        s = 0
        enabledMul = True
        for m in matches:
            if m == "do":
                enabledMul = True
                continue
            if m == "don't":
                enabledMul = False
                continue
            if enabledMul:
                s += eval(m)
        return s
