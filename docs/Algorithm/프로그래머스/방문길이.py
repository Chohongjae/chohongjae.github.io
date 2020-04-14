class TotalMap:
    DIRX = [0, 0, -1, 1]  # up, down, left, right
    DIRY = [1, -1, 0, 0]  # up, down, left, right

    def __init__(self):
        self.current = [0, 0]
        self.visited = {}
        self.new_length = 0

    def move(self, i):
        if -5 <= (self.current[0] + self.DIRX[i]) <= 5 and -5 <= (self.current[1] + self.DIRY[i]) <= 5:
            self.current[0] += self.DIRX[i]
            self.current[1] += self.DIRY[i]
            current = self.current[:]

            previous = [current[0] - self.DIRX[i], current[1] - self.DIRY[i]]

            if current not in self.visited.get(tuple(previous), []) and previous not in self.visited.get(tuple(current), []):
                self.new_length += 1

            if tuple(previous) not in self.visited:
                self.visited[tuple(previous)] = [current]
            else:
                self.visited[tuple(previous)].append(current)

            if tuple(current) not in self.visited:
                self.visited[tuple(current)] = [previous]
            else:
                self.visited[tuple(current)].append(previous)


def solution(dirs):
    total_map = TotalMap()
    for _dir in dirs:
        if _dir == 'U':
            total_map.move(0)
        elif _dir == 'D':
            total_map.move(1)
        elif _dir == 'R':
            total_map.move(3)
        elif _dir == 'L':
            total_map.move(2)
    answer = total_map.new_length
    return answer


if __name__ == "__main__":
    print(solution('ULURRDLLU'))
