class TotalMap:
    DIRY = [-1, 0, 1, 0]  # up, right, down, left
    DIRX = [0, 1, 0, -1]  # up, right, down, left

    def __init__(self, office, r, c):
        self.office = office
        self.N = len(self.office[0]) - 1
        self.current_direction = 0  # 북방향으로 시작
        self.current_location = [r, c]
        self.count = 0

    def go(self):
        tmp_y_location = self.current_location[0] + self.DIRY[self.current_direction]
        tmp_x_location = self.current_location[1] + self.DIRX[self.current_direction]

        if 0 <= tmp_x_location <= self.N and 0 <= tmp_y_location <= self.N and self.office[tmp_y_location][
            tmp_x_location] != -1:
            self.current_location[0] += self.DIRY[self.current_direction]
            self.current_location[1] += self.DIRX[self.current_direction]
            self.clear(self.current_location[0], self.current_location[1])

    def clear(self, y, x):
        self.count += self.office[y][x]
        self.office[y][x] = 0

    def rotate(self, direction):
        if direction == 'right':
            self.current_direction = (self.current_direction + 1) % 4
        else:
            self.current_direction = (self.current_direction - 1) % 4


def solution(office, r, c, move):
    total_map = TotalMap(office, r, c)
    total_map.clear(r, c)  # 처음 위치한 칸 청소

    for i in move:
        if i == 'go':
            total_map.go()
        else:
            total_map.rotate(i)
    answer = total_map.count
    return answer


if __name__ == "__main__":
    print(
        solution([[5, -1, 4], [6, 3, -1], [2, -1, 1]], 1, 0, ['go', 'go', 'right', 'go', 'right', 'go', 'left', 'go']))
