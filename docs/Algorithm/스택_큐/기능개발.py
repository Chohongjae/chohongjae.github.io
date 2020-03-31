from collections import deque
from math import ceil


def solution(progresses, speeds):
    answer = []
    queue = deque()
    for idx, progress in enumerate(progresses):
        tmp = 0
        remain_work = 100 - progress
        required_day = ceil(remain_work / speeds[idx])

        if not queue:
            queue.append(required_day)
        else:
            while queue:
                if queue[0] < required_day:
                    tmp += 1
                    queue.popleft()
                else:
                    break
            queue.append(required_day)
        if tmp != 0:
            answer.append(tmp)
    if queue:
        answer.append(len(queue))

    return answer


if __name__ == "__main__":
    print(solution( [5, 5, 5], speeds=[21, 25, 20]))
