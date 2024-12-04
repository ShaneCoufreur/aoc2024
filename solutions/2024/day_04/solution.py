# Generated using @xavdid's Aocols Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import TextSolution, answer
import numpy as np

class Solution(TextSolution):
    _year = 2024
    _day = 4

    @answer(2534)
    def part_1(self) -> int:        
        grid = [list(line) for line in self.input.split("\n")]
        rows = len(grid)
        cols = len(grid[0])

        s = 0
        for row in grid:
            r = ''.join(row)
            s += r.count("XMAS") + r.count("SAMX")
        
        a = np.matrix(grid)        
        for c in range(cols):
            r = ''.join(a[:,c:c+1].getA1())
            s += r.count("XMAS") + r.count("SAMX")

        for i in range( rows*-1, cols):            
            r = ''.join(np.diag(a, k=i))
            s += r.count("XMAS") + r.count("SAMX")

        a = np.fliplr(a)
        for i in range( rows*-1, cols):            
            r = ''.join(np.diag(a, k=i))
            s += r.count("XMAS") + r.count("SAMX")
        return s

    @answer(1866)
    def part_2(self) -> int:        
        grid = self.input.split("\n")
        rows = len(grid)
        cols = len(grid[0])
        s = 0
        for row in range(rows):
            for col in range(cols):
                if row+2<rows and col+2<cols:
                    if grid[row][col]=='M' and grid[row+1][col+1]=='A' and grid[row+2][col+2]=='S':
                        if ((grid[row+2][col]=='M' and grid[row][col+2]=='S') or (grid[row+2][col]=='S' and grid[row][col+2]=='M')):
                            s += 1                            
                    elif grid[row][col]=='S' and grid[row+1][col+1]=='A' and grid[row+2][col+2]=='M':
                        if ((grid[row+2][col]=='M' and grid[row][col+2]=='S') or (grid[row+2][col]=='S' and grid[row][col+2]=='M')):
                            s += 1
        return s