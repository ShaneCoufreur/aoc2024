# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 2
    def is_safe(self, level):
        diff = [level[i + 1] - level[i] for i in range(len(level) - 1)]
        return all([d in (3, 2, 1) for d in diff]) or all([d in (-3, -2, -1) for d in diff])

    @answer(421)
    def part_1(self) -> int:
        lines = [s.split() for s in self.input.split("\n")]
        num_safe_reports = 0
        for line in lines:
            values = [int(x) for x in line]
            #self.debug(values)
            safe = self.is_safe(values)
            if safe:
                num_safe_reports += 1
            #self.debug(safe)

        return num_safe_reports

    @answer(476)
    def part_2(self) -> int:
        lines = [s.split() for s in self.input.split("\n")]
        num_safe_reports = 0
        for line in lines:
            values = [int(x) for x in line]
            #self.debug(values)
            checks = [self.is_safe(values[:i] + values[i + 1:]) for i in range(len(values))]
            safe = any(checks)            
            #self.debug(safe)
            if safe:
                num_safe_reports += 1

        return num_safe_reports