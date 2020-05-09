phone = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]


class CurrentHand:
    def __init__(self):
        self.left = [3, 0]
        self.right = [3, 2]


def solution(numbers, hand):
    answer = []

    left = [1, 4, 7]
    right = [3, 6, 9]
    current_hand = CurrentHand()

    for number in numbers:
        if number in left:
            answer.append('L')
            if number == 1:
                current_hand.left = [0, 0]
            elif number == 4:
                current_hand.left = [1, 0]
            else:
                current_hand.left = [2, 0]
        elif number in right:
            answer.append('R')
            if number == 3:
                current_hand.right = [0, 2]
            elif number == 6:
                current_hand.right = [1, 2]
            else:
                current_hand.right = [2, 2]
        else:
            if number == 2:
                diff_with_left = abs(current_hand.left[0] - 0) + abs(current_hand.left[1] - 1)
                diff_with_right = abs(current_hand.right[0] - 0) + abs(current_hand.right[1] - 1)

            elif number == 5:
                diff_with_left = abs(current_hand.left[0] - 1) + abs(current_hand.left[1] - 1)
                diff_with_right = abs(current_hand.right[0] - 1) + abs(current_hand.right[1] - 1)
            elif number == 8:
                diff_with_left = abs(current_hand.left[0] - 2) + abs(current_hand.left[1] - 1)
                diff_with_right = abs(current_hand.right[0] - 2) + abs(current_hand.right[1] - 1)
            else:
                diff_with_left = abs(current_hand.left[0] - 3) + abs(current_hand.left[1] - 1)
                diff_with_right = abs(current_hand.right[0] - 3) + abs(current_hand.right[1] - 1)

            if diff_with_left == diff_with_right:
                if hand == "right":
                    answer.append('R')
                    if number == 2:
                        current_hand.right = [0, 1]
                    elif number == 5:
                        current_hand.right = [1, 1]
                    elif number == 8:
                        current_hand.right = [2, 1]
                    else:
                        current_hand.right = [3, 1]
                else:
                    answer.append('L')
                    if number == 2:
                        current_hand.left = [0, 1]
                    elif number == 5:
                        current_hand.left = [1, 1]
                    elif number == 8:
                        current_hand.left = [2, 1]
                    else:
                        current_hand.left = [3, 1]
            elif diff_with_left > diff_with_right:
                answer.append('R')
                if number == 2:
                    current_hand.right = [0, 1]
                elif number == 5:
                    current_hand.right = [1, 1]
                elif number == 8:
                    current_hand.right = [2, 1]
                else:
                    current_hand.right = [3, 1]
            else:
                answer.append('L')
                if number == 2:
                    current_hand.left = [0, 1]
                elif number == 5:
                    current_hand.left = [1, 1]
                elif number == 8:
                    current_hand.left = [2, 1]
                else:
                    current_hand.left = [3, 1]

    return ''.join(answer)


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
