def test(arr):
    start = 0
    end = len(arr)
    count = 0
    arr_length = len(arr)

    left_sum = sum(arr[:1])
    right_sum = sum(arr[1:])
    for pivot in range(1, arr_length):
        if left_sum > right_sum:
            count += 1
        left_sum += arr[pivot]
        right_sum -= arr[pivot]

    return count


if __name__ == "__main__":
    print(test([10, -5, 6]))
    # print([1,2,3,4,5][1:5])
