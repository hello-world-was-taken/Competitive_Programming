# https://leetcode.com/problems/robot-bounded-in-circle/


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, direction = 0, 0, 'N'
        n = len( instructions )
        
        for instruction in instructions:
            if instruction == 'G':
                if direction == 'N':
                    y += 1
                elif direction == 'W':
                    x -= 1
                elif direction == 'S':
                    y -= 1
                elif direction == 'E':
                    x += 1

            elif instruction == 'L':
                if direction == 'N':
                    direction = 'W'
                elif direction == 'W':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'E'
                elif direction == 'E':
                    direction = 'N'
            
            elif instruction == 'R':
                if direction == 'N':
                    direction = 'E'
                elif direction == 'W':
                    direction = 'N'
                elif direction == 'S':
                    direction = 'W'
                elif direction == 'E':
                    direction = 'S'
                
        return x == 0 and y == 0 or direction != 'N'
