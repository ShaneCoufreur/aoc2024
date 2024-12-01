# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 1

    @answer(2192892)
    def part_1(self) -> int:
        
        c = []
        for d in self.input.split():
            c.append(int(d))

        a = c[::2]
        b = c[1::2]
        a.sort()
        b.sort()
        
        total = []
        for i, _ in enumerate(a):
            total.append( abs(a[i]-b[i]) )

        return sum(total)
        

    @answer(22962826)
    def part_2(self) -> int:        
        c = []
        for d in self.input.split():
            c.append(int(d))

        a = c[::2]
        b = c[1::2]
        total = []
        for x in a:
            total.append(b.count(x) * x)
        return sum(total)