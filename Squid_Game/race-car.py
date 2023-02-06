# https://leetcode.com/problems/race-car/


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])
        visited = set()
        while queue:
            pos, moves, speed = queue.popleft()
            
            if pos == target:
                return moves
            
            if (pos, speed) not in visited:
                visited.add( (pos, speed) )
                # accelerate
                queue.append( (pos + speed, moves + 1, speed * 2) )

                # deccelerate
                if speed > 0 and pos + speed > target:
                    queue.append( (pos, moves + 1, -1) )
                elif pos + speed < target and speed < 0:
                    queue.append( (pos, moves + 1, 1) )
