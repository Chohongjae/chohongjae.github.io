# https://programmers.co.kr/learn/courses/30/lessons/42588
def solution(heights):
    answer = []
    for idx, i in enumerate(reversed(heights)):
        for idx2, j in enumerate(reversed(heights[:len(heights) - idx - 1])):
            if i < j:
                answer.insert(0, len(heights[:len(heights) - idx - 1]) - idx2)
                break
        else:
            # for문이 끝나고 중간에 break가 되지 않으면 실행되는 for - else 이다.
            answer.insert(0, 0)

    return answer


# 스택으로 다시 풀었음
def solution2(heights):
    answer = [0] * len(heights)
    stack = []
    for idx, i in enumerate(reversed(heights)):
        if not stack:
            stack.append(idx)
            continue
        while stack:
            if heights[len(heights) - stack[-1] - 1] < i:
                a = stack.pop()
                answer[len(heights) - a - 1] = len(heights) - idx
            else:
                break
        stack.append(idx)
    return answer


if __name__ == "__main__":
    print(solution([1, 5, 3, 6, 7, 6, 5]))
