# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from re import L
from ...base import StrSplitSolution, answer
from collections import defaultdict

class Solution(StrSplitSolution):
    _year = 2024
    _day = 5

    @answer(5391)
    def part_1(self) -> int:
        order = []
        pages = []
        fillorder = True
        for string in self.input:
            if string == "":
                fillorder = False
            elif fillorder:
                order.append(string)
            else:
                pages.append(string)

        valid = []
        sortorder = defaultdict(list)
        for order in order:
            (first, second) = map(int, order.split("|"))
            sortorder[first].append(second)
        print(sortorder)
                
        for p in pages:
            invalid = False
            page_nums = [int(n) for n in p.split(",")]
            l = len(page_nums)
            for i in range(l):
                if invalid:
                    break
                for j in range(i+1, l):
                    if invalid:
                        break
                    if page_nums[i] not in sortorder or page_nums[j] not in sortorder[page_nums[i]]:
                        invalid = True
            if not invalid:
                valid.append(page_nums)
                            
        return sum([int(v[len(v)//2]) for v in valid])

    @answer(6142)
    def part_2(self) -> int:
        order = []
        pages = []
        fillorder = True
        for string in self.input:
            if string == "":
                fillorder = False
            elif fillorder:
                order.append(string)
            else:
                pages.append(string)

        sortorder = defaultdict(list)
        for order in order:
            (first, second) = map(int, order.split("|"))
            sortorder[first].append(second)
                
        notvalid = []
        for p in pages:
            invalid = False
            page_nums = [int(n) for n in p.split(",")]
            l = len(page_nums)
            for i in range(l):
                if invalid:
                    break
                for j in range(i+1, l):
                    if invalid:
                        break
                    if page_nums[i] not in sortorder or page_nums[j] not in sortorder[page_nums[i]]:
                        invalid = True
            if invalid:
                notvalid.append(page_nums)

        s = 0                  
        for p in notvalid:
            n = len(p)
            t = []
            for i in range(n):
                o = 0
                for j in range(n):
                    if p[i] in sortorder and p[j] in sortorder[p[i]]:
                        o += 1
                t.append((p[i], o))

            t.sort(key=lambda item: item[1], reverse=True)
            y = [x[0] for x in t]
            s += int(y[len(y)//2])

        return s

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
