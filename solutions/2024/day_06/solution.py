# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 6

    @answer(5269)
    def part_1(self) -> int:
        sr = -1
        sc = -1

        inp = self.input.split("\n")
        grid = []

        rowsize = len(inp)
        colsize = len(inp[0])
        for i, line in enumerate(inp):
            grid.append([])
            if "^" in line:
                sr = i
            for j, c in enumerate(line):
                grid[i].append(c)
                if c == "^":
                    sc = j
        x = sr
        y = sc
        dir = "n"
        distinct_locations = set()
        distinct_locations.add( (x, y) )
        grid[x][y] = "X"
        while(x >= 0 and x < rowsize and y >= 0 and y < colsize):
            #print(dir, (x, y) )
            distinct_locations.add( (x, y) )

            grid[x][y] = "X"
            if dir == "n":
                if( x-1 >= 0 and inp[x-1][y] == "#" ):
                    dir = "e"
                else:
                    x -= 1
            elif dir == "e":
                if( y+1 < colsize and inp[x][y+1] == "#" ):
                    dir = "s"
                else:
                    y += 1
            elif dir == "s":
                if( x+1 < rowsize and inp[x+1][y] == "#" ):
                    dir = "w"
                else:
                    x += 1                    
            elif dir == "w":
                if( y-1 >= 0 and inp[x][y-1] == "#" ):
                    dir = "n"
                else:
                    y -= 1
        return len(distinct_locations)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
