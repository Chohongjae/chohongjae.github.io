from collections import deque


def solution(prices):
    answer = deque()
    queue = deque()

    for price in reversed(prices):
        if not queue:
            queue.appendleft(price)
            answer.appendleft(0)
        else:
            for idx, i in enumerate(queue):
                if i < price:
                    answer.appendleft(idx + 1)
                    queue.appendleft(price)
                    break
            else:
                answer.appendleft(len(queue))
                queue.appendleft(price)

    return list(answer)


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
    # 3 2 3 2 1
    #
    # 1
    # 2
    # 3
    # 2
    # 3
