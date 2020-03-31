from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)

    load = [0] * bridge_length

    current_length = 0
    current_weight = 0

    while True:
        if load[0] != 0:
            current_weight -= load[0]
            current_length -= 1
        load = load[1:]

        if queue and current_weight + queue[0] <= weight and current_length + 1 <= bridge_length:
            truck = queue.popleft()
            load.append(truck)

            current_weight += truck
            current_length += 1
        else:
            load.append(0)

        answer += 1

        if not queue and current_weight == 0:
            break
    return answer


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
