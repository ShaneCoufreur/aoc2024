# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import TextSolution, answer
from collections import Counter

class Solution(TextSolution):
    _year = 2024
    _day = 1

    @answer(605218616)
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
        

    @answer(204826471269726238)
    def part_2(self) -> int:        
        c = [int(d) for d in self.input.split()]

        a = c[::2]
        b = c[1::2]

        # total = 0
        # for i, x in enumerate(a):
        #    #print(f"Calculating for {i} of {len(a)}")
        #    total += b.count(x) * x

        # return total

        # # return total
        c = Counter(b)

        s = 0
        for i in a:
            s += c[i] * i


        return s